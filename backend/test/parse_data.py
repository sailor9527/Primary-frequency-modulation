#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 接收 DPU 数据(DIP)并解析, 把前端界面中的点值放入池中

import json
import socket
import struct
import threading

# 绑定接收端即本机的 IP
HOST = "192.168.1.201"
# 绑定本机的端口, DIP 默认发送到 9010 端口
PORT = 9010


class Dip_data(object):
    """接收并解析DIP数据
    """
    def __init__(self, host, port):
        # 初始化，建立 UDP 连接
        self.SOCKETSERVER = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.SOCKETSERVER.bind((host,port))

        # 用作返回的数据
        self.DATA = None
    
    def parse_dip_data(self):
        while True:
            data = self.SOCKETSERVER.recv(2048)
            print('----------receive data------------')

            # 解析数据部分
            pnt_num = struct.unpack_from('BBBBIHHI', data)[6]       # 接收包中点的数量
            # receive_time = float(struct.unpack_from('BBBBIHHI', data)[4])  # 接收到数据包的时间:到秒级
            print('pnt_num', pnt_num)

            for i in range(pnt_num):
                self.DATA = struct.unpack_from('f',data[i * 12 + 16 + 8 : i * 12 + 16 + 12])[0]
                self.DATA = json.dumps(self.DATA)
                # print "pnt_value------------->", format_data

    def start(self):
        threading.Thread(target= self.parse_dip_data).start()


dip_data = Dip_data(HOST, PORT)
dip_data.start()
    
    
