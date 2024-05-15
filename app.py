import hashlib
import json

from aiohttp import web

from constants import STRING_FIELD_EMPTY_ERROR

routes = web.RouteTableDef()


@routes.get('/healthcheck')
async def healthcheck(request):
    return web.json_response({})


@routes.post('/hash')
async def hash(request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return web.json_response(
            {'validation_errors': STRING_FIELD_EMPTY_ERROR}, status=400)
    string_to_hash = data.get('string')
    if not string_to_hash:
        return web.json_response(
            {'validation_errors': STRING_FIELD_EMPTY_ERROR}, status=400)
    hash_object = hashlib.sha256(string_to_hash.encode())
    hex_dig = hash_object.hexdigest()
    return web.json_response({'hash_string': hex_dig})


def create_app():
    app = web.Application()
    app.add_routes(routes)
    return app

def main():
    web.run_app(create_app())

if __name__ == '__main__':
    main()
