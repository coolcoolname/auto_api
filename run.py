#  -*- coding:utf-8 -*-
# @Time   :  2023.10
# @Author :  秦资鸿
# @Note   :
from common import logging
from my_script import shop_cart

def run():
    log = logging.myLogger()
    shop_cart.ShopCart.info_simple_cart()
    log.debug("-------执行完成-------")
run()