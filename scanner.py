from aiohttp import web
import json


async def handle(request):
    ip = request.match_info.get('ip')
    begin_port = request.match_info.get('begin_port')
    end_port = request.match_info.get('end_port')
    response_obj = \
        {'data':
            {
                'ip': ip,
                'begin_port': begin_port,
                'end_port': end_port
            }
        }

    return web.Response(text=json.dumps(response_obj), status=200)


app = web.Application()
app.router.add_get('/scan/{ip}/{begin_port}/{end_port}', handle)

if __name__ == '__main__':
    web.run_app(app)
