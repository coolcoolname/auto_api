#  -*- coding:utf-8 -*-
# @Time   :  2023.10
# @Author :  秦资鸿
# @Note   : 获取用户token
import json
import time
import yaml
import hashlib

import dependencies as dd
from common import logging


log = logging.myLogger()

base_url = 'http://testgwec.dmall-os.com'
base_headers ={
"sysversion":"Android-13",
"apptypeenum":"1",
"accept":"application/json,text/plain,*/*",
"gw-trace-id":"0fc2fb53-1071-4ca8-a5cd-8dd90a5b751a",
"dmall-tenant-id":"589337",
"dmall-locale":"en_US",
"versionname":"1.0.3",
"devicetime":"1698128332923",
"uuid":"291de9e317ee235de81f30004e2a91ee2",
"platform":"ANDROID",
"orgid":"542483",
"dmall-timezone":"Europe/Warsaw",
"dmall-group-id":"100138",
"appbuildnumber":"Android-13",
"device":"realmeRMX3708",
"user-agent":"ECDmall/1.0.3",
"requestfrom":"APP",
"content-type":"application/x-www-form-urlencoded",
"content-length":"92",
"accept-encoding":"gzip",
}


class BasicToolAcquisition():
    # log = logging.myLogger()
    def __init__(self):
        pass
        # self.log = logging.myLogger()
        # file_path = "../data/user_info.yaml"
        # self.read_yaml(file_path)
        # self.base_headers["deviceTime"] = self.device_time()

    def device_time(self):
        """
        :return: 返回当前时间戳
        """
        current_timestamp = str(int(round(time.time() * 1000)))
        # self.log.debug('返回当前时间戳为：{}'.format(current_timestamp))
        log.debug('返回当前时间戳为：{}'.format(current_timestamp))
        return current_timestamp

    def read_yaml(self,file_path):
        """
        :param file_path: 传入文件路径
        :return: 返回yaml文件读取结果
        """
        with open(file=file_path, mode='r', encoding='utf-8') as f:
            self.yaml = yaml.safe_load(f)
            return self.yaml
        log.debug('读取到的会员信息:{}'.format(self.yaml))

    def encrypt_string(self,string):
        """
        给账号加密使用
        :param string:
        :return: 返回密文
        """
        md5 = hashlib.md5()
        md5.update(string.encode('utf-8'))
        encrypt_string = md5.hexdigest()
        return encrypt_string

    def query_account_list(self):
        """
        查询当前会员是否有效
        :return:
        """
        path = "/api/single/member/queryAccountList"
        url = base_url + path
        base_headers["deviceTime"] = self.device_time()

        read_file = self.read_yaml( "../data/user_info.yaml")
        phone = read_file[0]['phone']
        deviceId = read_file[0]['deviceId']
        params = [{'phone': phone,'deviceId': deviceId}]

        params = json.dumps(params)
        params = {"params":params}
        # print(params)
        log.debug(f'请求地址:{url}  请求体:{params}  请求头:{base_headers} ')
        res = dd.requests.post(url=url,headers=base_headers,data=params).json()
        log.info('响应结果{}'.format(res))
        return res["code"]

    def login_by_password(self):
        path = '/api/single/member/loginByPassword'
        url = base_url + path
        base_headers["deviceTime"] = self.device_time()

        read_file = self.read_yaml("../data/user_info.yaml")
        password = self.encrypt_string(read_file[0]['password'])
        phone = read_file[0]['phone']
        countryCode = read_file[0]['countryCode']
        deviceId = read_file[0]['deviceId']
        params = [{"password":password,"phone":phone,"countryCode":countryCode,"deviceId":deviceId}]

        params = json.dumps(params)
        params = {"params": params}

        log.debug(f'请求地址:{url}  请求体:{params}  请求头:{base_headers}')
        res = dd.requests.post(url=url, headers=base_headers, data=params).json()
        log.info('响应结果{}'.format(res))
        log.info(f'获得ticket：{res["data"]["ticket"]} \n 获得token：{res["data"]["token"]}')
        ticket = res["data"]["ticket"]
        token = res["data"]["token"]
        return ticket,token

    def  get_token(self):
        if self.query_account_list() == '0000':
            return self.login_by_password()
        else:
            log.info("会员查询失败")

# if __name__ == '__main__':
#     tool = BasicToolAcquisition()
#     # tool.device_time()
#     tool.get_token()