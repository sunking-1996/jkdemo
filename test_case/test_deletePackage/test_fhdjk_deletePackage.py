import requests
import pytest
import allure
from urllib import parse
from common.read import get_cookies,get_headers

@allure.step("---待打列表查询---")
def queryPackage_daida():        #待打包裹列表
    '''待打包裹列表'''
    s = get_headers()
    #decode解码
    fhd_token=parse.unquote(get_cookies()[1])
    # print(fhd_token)
    url = "http://typapi.fhd001.com/api/package/queryPackage.do"
    body = {"page":"1",
            "pageSize":"1000",
            "status":"0",
            "token": fhd_token

    } #参数存字典
    request = s.post(url=url,data=body)
    r = request.json()
    print("待打包裹列表查询返回结果:%s"% r)
    pid = r['data']['list'][-1]['packageId']

    print("获取待打包裹列表第一个包裹的ID %s"%(pid))

    i = [pid,fhd_token]
    return i

@allure.story("---删除自定义包裹---")
def test_delete_package_normal():        #删除自定义包裹
    u'''删除自定义包裹'''
    s = get_headers()
    i = queryPackage_daida()
    url = "https://typapi.fhd001.com/api/package/deletePackage.do"
    body = {"packageIds":i[0],
            "token": i[1]
    } #参数存字典
    request = s.post(url=url,data=body)
    r = request.json()
    print("删除自定义包裹接口返回结果:%s"% request.text)

    #期望结果 "rcode":0,"scode":0
    expect_result = {"rcode":0,"scode":0}

    #实际结果
    rcode = r['rcode']
    print("返回的rcode:%s"%rcode)
    scode = r['scode']
    print("返回的scode:%s"%scode)

if __name__ == "__main__":
    # pytest.main(["-s","-v","test_fhdjk_deletePackage.py::test_delete_package_normal"])
    pytest.main(["-s","-v","test_fhdjk_deletePackage.py"])
