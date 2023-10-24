#  -*- coding:utf-8 -*-
# @Time   :  2023.10
# @Author :  秦资鸿
# @Note   :
import requests
import hashlib
import json
import time
import urllib3
base_url = 'http://testgwec.dmall-os.com'
base_headers ={
    "Host":"testgwec.dmall-os.com",
    "User-Agent":"ECDmallTest/1.0.0 (iPhone; iOS 16.3.1; Scale/2.00)",
    "requestFrom":"APP",
    "dmall-locale":"en_US",
    "orgId":"5503",
    "deviceTime":"1679313151",
    "versionName":"1.0.0",
    "uuid":"0435705452e32fbd13529632fdb195fe3610e063",
    "appTypeEnum":"1",
    "appBuildNumber":"1",
    "sysVersion":"16.3.1",
    "dmall-timezone":"UTC+8",
    "Content-Length":"58",
    "platform":"IOS",
    "Connection":"keep-alive",
    "Accept-Language":"zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8",
    "dmall-tenant-id":"100002",
    "gw-trace-id":"EC61FDC4D8344142A7FF9F279E6241C3",
    "Accept":"application/json",
    "Content-Type":"application/x-www-form-urlencoded",
    "Accept-Encoding":"gzip, deflate, br",
    "loginType":"3",
    "device":"iPhone10,1"
}



def deviceTime():
    """

    :return: 返回当前时间戳
    """
    current_milli_time = str(int(round(time.time() * 1000)))
    print(f'当前时间戳为：{current_milli_time}')
    return current_milli_time


def queryAccouuntList():
    """
    输入账号验证
    :return:
    """
    url = base_url + "/api/single/member/queryAccountList"
    # 格式化当前入参
    params = [{"deviceId": "6c350420f1b58777", "email": "31392140@qq.com"}]
    print(params)
    params = json.dumps(params)
    print(params)
    params = {"parmas": params}
    print(params)
    # 格式化请求头
    base_headers["deviceTime"] = deviceTime()
    # print(base_headers)
    response = requests.post(headers=base_headers, url=url, data=params).json()
    print(response)

if __name__ == '__main__':
    queryAccouuntList()