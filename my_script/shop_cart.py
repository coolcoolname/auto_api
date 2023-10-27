#  -*- coding:utf-8 -*-
# @Time   :  2023.10
# @Author :  秦资鸿
# @Note   : 添加购物车
import json
import ddt
import yaml

import get_token

import dependencies as dd
from common import logging

# @ddt.ddt()
class  ShopCart:
    log = logging.myLogger()

    def __init__(self):
        # self.log = logging.myLogger()
        # 获得登录的ticket和token
        login = get_token.BasicToolAcquisition()
        self.ticket,self.token = login.get_token()
        #获得服务器地址
        self.url = get_token.base_url
        #获得请求头
        self.headers = get_token.base_headers
        self.headers["ticket"] = self.ticket
        self.headers["token"] = self.token
        self.__add_cart()  # 在初始化时直接调用 __add_cart 方法

    # @ddt.file_data("../data/SKU.yaml")
    def __add_cart(self,**kwargs):
        path = "/api/single/shopcart/addCart"
        url = self.url + path

        with open("../data/SKU.yaml",'r',encoding='utf-8') as file:
            data  = yaml.safe_load(file)

        count = 0
        for item in data:
            sku_id = item["sku_id"]
            self.log.debug("这是sku：{}".format(sku_id))
            params = [{"needQueryFlag":False,"cartOrgWareRpcReqs":[{"skuId":sku_id,"count":1,"checked":True,"wareSaleType":1}]}]
            params = json.dumps(params)
            params = {"params":params}
            self.log.debug((f'添加购物车请求地址:{url}  请求体:{params}  请求头:{self.headers}'))
            response = dd.requests.post(url=url, headers=self.headers,data=params).json()
            self.log.info('响应结果{}'.format(response))
            if response["code"] == '0000':
                count += 1
                self.log.debug("商品加购成功第{}次".format(count))
            else:
                self.log.debug("商品加购失败，错误信息{}".format(response))

    def info_simple_cart(self):
        if not self.__add_cart():
            self.__add_cart() # 初始化购物车之前检查商品加购没有，没有就先调用加车方法

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
            for item in simpleWareRpcRespList:
                skuId = item["skuId"]
                count = item["count"]
                self.log.debug(f"购物车中skuId：{skuId}，加购数量：{count}")
            return simpleWareRpcRespList
        else:
            self.log.debug("购物车初始化失败，错误信息{}".format(response))

if __name__ == '__main__':
    shop = ShopCart()
    # shop.add_cart()
    shop.info_simple_cart()