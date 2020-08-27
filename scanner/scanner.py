from aiohttp import web
import systemd.journal
import logging
import json
import asyncio


def catch_exception(func):
    async def decorated_function(ip, port, scan_loop):
        try:
            await func(ip, port, scan_loop)
            return [{"port": str(port), "state": "open"}]
        except asyncio.TimeoutError:
            return [{"port": str(port), "state": "close"}]
    return decorated_function


@catch_exception
async def check_port(ip, port, scan_loop):
    conn = asyncio.open_connection(ip, port, loop=scan_loop)
    await asyncio.wait_for(conn, timeout=3)


async def run(ip, begin_port, end_port, scan_loop):
    tasks = [asyncio.ensure_future(check_port(ip, p, scan_loop)) for p in range(begin_port, end_port)]
    responses = await asyncio.gather(*tasks)
    return responses


async def handle(request):
    ip = request.match_info.get('ip')
    begin_port = int(request.match_info.get('begin_port'))
    end_port = int(request.match_info.get('end_port'))

    loop = asyncio.get_event_loop()
    results = await asyncio.ensure_future(run(ip, begin_port, end_port, loop))
    print(results)
    response_obj = {'data': results}

    return web.Response(text=json.dumps(response_obj), status=200)


def get_app():
    new_app = web.Application()
    new_app.router.add_get('/scan/{ip}/{begin_port}/{end_port}', handle)
    return new_app


# _________________________ pytest _____________________________________

def create_app(loop):
    test_app = get_app()
    return test_app


async def test_hello(aiohttp_client):
    client = await aiohttp_client(create_app)
    resp = await client.get('/scan/192.168.0.1/1/10')
    assert resp.status == 200
    data = await resp.text()
    dict_data = json.loads(data)
    assert type(dict_data['data']) is list

# _________________________ pytest _____________________________________


logger = logging.getLogger('aiohttp.access')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logger.addHandler(systemd.journal.JournalHandler())

if __name__ == '__main__':
    print('Starting!')
    web.run_app(get_app())
