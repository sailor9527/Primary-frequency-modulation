#!/usr/bin/env python
# -*- coding:utf-8 -*-
# webpy服务器, 用于提供 web 服务器功能

import web
import json
import threading
# from parse_data import Dip_data
from parse_data import dip_data

# 绑定接收端即本机的 IP
HOST = "192.168.1.201"
# 绑定本机的端口, DIP 默认发送到 9010 端口
PORT = 9010

# web.py 服务器
urls = (
    '/text/', 'Text'
)

class Text:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        
        print('---------receive data---------')

        print "data--------> :",dip_data.DATA
        return json.dumps(dip_data.DATA)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    # threading.Thread(target=parse_data).start()

