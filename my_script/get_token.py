#  -*- coding:utf-8 -*-
# @Time   :  2023.10
# @Author :  秦资鸿
# @Note   : 获取用户token
import json
import time
import yaml

import dependencies as dd
from common import logging


base_url = 'http://testgwec.dmall-os.com'

log = logging.myLogger()

base_headers ={
    "sysversion":"Android-13",
    "apptypeenum":"1",
    "accept":"application/json, text/plain, */*",
    "gw-trace-id":"fc32303a-88f0-4de1-bd6a-551bc38a805a",
    "dmall-tenant-id":"589337",
    "dmall-locale":"n_US",
    "versionname":"1.0.3",
    "devicetime":" 697779788471",
    "uuid":"291de9e317ee235de81f30004e2a91ee2",
    "platform":"ANDROID",
    "orgid":"542483",
    "dmall-timezone":"Europe/Warsaw",
    "dmall-group-id":"100138",
    "appbuildnumber":"Android-13",
    "device":"realmeRMX3708",
    "user-agent":"ECDmall/1.0.3",
    "requestfrom":"PP",
    "content-type":"application/x-www-form-urlencoded",
    "content-length":"92",
    "accept-encoding":"gzip",
}


class BasicToolAcquisition:
    def __init__(self):
        self.log = logging.myLogger()
        self.read_yaml()

    def device_time(self):
        """
        :return: 返回当前时间戳
        """
        current_timestamp = str(int(round(time.time() * 1000)))
        # self.log.debug('返回当前时间戳为：{}'.format(current_timestamp))
        log.debug('返回当前时间戳为：{}'.format(current_timestamp))
        return current_timestamp

    import yaml

    def read_yaml(self):
        with open("../data/user_info.yaml", 'r', encoding='utf-8') as f:
            self.yaml = yaml.safe_load(f)
        log.debug('读取到的会员信息:{}'.format(self.yaml))

    def query_account_list(self):
        """
        查询当前会员是否有效
        :return:
        """
        path = "/api/single/member/queryAccountList"
        url = base_url + path
        base_headers["deviceTime"] = self.device_time()

        phone_number = self.yaml[0]['phone_number']
        device_id = self.yaml[0]['device_id']
        params = [{'phone': phone_number,'device_id': device_id}]
        print(params)
        params = json.dumps(params)
        print(params)
        params = {"params":params}
        print(params)


        log.debug(f'请求地址:{url}  请求体:{params}  请求头:{base_headers}  ')
        res = dd.requests.post(url=url,headers=base_headers,json=params).json()
        log.info('响应结果{}'.format(res))


if __name__ == '__main__':
    tool = BasicToolAcquisition()
    # tool.device_time()
    tool.query_account_list()