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

    # @ddt.file_data("../data/SKU.yaml")
    def add_cart(self,**kwargs):
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


if __name__ == '__main__':
    shop = ShopCart()
    shop.add_cart()