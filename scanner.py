from aiohttp import web
import json


async def handle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj), status=200)


app = web.Application()
app.router.add_get('/scan', handle)

if __name__ == '__main__':
    web.run_app(app)
