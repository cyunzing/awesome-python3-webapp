#!/user/bin/env python3
# -*- coding: utf-8 -*-


'''
createtime: 2016-8-21 15:02:30
'''


import logging; logging.basicConfig(level=logging.INFO)


import asyncio, os, json, time
from datetime import datetime


from aiohttp import web


def index(request):
    return web.Response(body=bytes('<h1>Awesome...你好！</h1>', encoding='utf-8'), headers={'Content-Type': 'text/html; charset=utf-8'})


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9393)
    logging.info('server started at http://127.0.0.1:9393...')
    return srv
    

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
