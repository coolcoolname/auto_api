#  -*- coding:utf-8 -*-
# @Time   :  2023.10
# @Author :  秦资鸿
# @Note   : 初始化购物车，用于结算业务
import json

import get_token
import dependencies as dd
from common import logging
class InfoSimpleCart:
    log = logging.myLogger()
    def __init__(self):
        # 获得登录的ticket和token
        login = get_token.BasicToolAcquisition()
        self.ticket,self.token = login.get_token()
        #获得服务器地址
        self.url = get_token.base_url
        #获得请求头
        self.headers = get_token.base_headers
        self.headers["ticket"] = self.ticket
        self.headers["token"] = self.token

    def info_simple_cart(self):
        path = "/api/single/shopcart/infoSimpleCart"
        url = self.url + path
        params = []
        params = json.dumps(params)
        params = {"params":params}
        self.log.debug((f'初始化购物车请求地址:{url}  请求体:{params}  请求头:{self.headers}'))
        response = dd.requests.post(url=url,headers=self.headers,data=params).json()
        self.log.info('响应结果{}'.format(response))
        if response["code"] == '0000':
            simpleWareRpcRespList = response["data"][0]["simpleWareRpcRespList"]
            self.log.debug("提取到购物车商品列表{}".format(simpleWareRpcRespList))
            return simpleWareRpcRespList
        else:
            self.log.debug("购物车初始化失败，错误信息{}".format(response))



if __name__ == '__main__':
    shop = InfoSimpleCart()
    shop.info_simple_cart()
