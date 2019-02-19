#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用于测试能否接收到 DPU 发送的数据，经测试可以从 DPU 接收到数据并解析

import socket
import web
import json
import struct
import time
from backend import Text


# 绑定接收端即本机的 IP
HOST = "192.168.1.201"
# 绑定本机的端口, DIP 默认发送到 9010 端口
PORT = 9010
SOCKETSERVER = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SOCKETSERVER.bind((HOST,PORT))

# web.py 搭建 web 服务器
# urls = (
#     '/text/', 'Text'
# )
# text = Text
# app = web.application(urls, globals())
# app.run()


while True:
    print('---------> start')
    data = SOCKETSERVER.recv(2048)
    print('---------receive data---------', time.time())
    

    
    # 解析数据部分
    pnt_num = struct.unpack_from('BBBBIHHI', data)[6]       # 接收包中点的数量
    receive_time = float(struct.unpack_from('BBBBIHHI', data)[4])  # 接收到数据包的时间:到秒级
    print('pnt_num', pnt_num)

    for i in range(pnt_num):
        pnt_value = struct.unpack_from('f',data[i * 12 + 16 + 8 : i * 12 + 16 + 12])[0]
        print "pnt_value------------->", pnt_value





    
