# -*- coding: utf-8 -*-
#@Time    : 2/25/21 4:25 PM
#@Author  : SHAUN-coyote
#@Email   : coyotezxy@163.com
#@File    : app.py

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers = {"content-type": "text/html"})
#不传header，会变成下载一个文件，待确认问题？


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    apprunner = web.AppRunner(app)
    await apprunner.setup()
    srv = await loop.create_server(apprunner.server, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()