import requests
import pytest
import allure
from urllib import parse
from common.read import get_cookies,get_headers


@allure.feature("删除包裹常用备注模块")
class TestDelpackage:
    @allure.step("---获取第一个包裹常用备注id---")
    def obtain_packageNote(self):
        s = get_headers()
        #decode解码
        fhd_token=parse.unquote(get_cookies()[1])
        url = "http://typapi.fhd001.com/api/package/getPackageCommonNoteList.do"
        body = {
                "token": fhd_token

        } #参数存字典
        request = s.post(url=url,data=body)
        r = request.json()
        pid = r['data'][0]['id']

        print("获取第一个包裹常用备注id %s"%(pid))

        i = [pid,fhd_token]
        return i

    @allure.story("---删除包裹备注---")
    def test_delete_packageNote(self):
        s = get_headers()
        i = self.obtain_packageNote()
        url = "http://typapi.fhd001.com/api/package/deletePackageCommonNote.do"
        body = {"id":i[0],
                "token": i[1]
        } #参数存字典
        request = s.post(url=url,data=body)
        r = request.json()
        print("删除包裹备注接口返回结果:%s"% request.text)

        #期望结果 "rcode":0,"scode":0
        expect_result = {"rcode":0,"scode":0}

        #实际结果
        assert r["rcode"] == expect_result["rcode"] and r["scode"] == expect_result["scode"]

if __name__ == "__main__":
    pytest.main(["-s","-v","test_fhdjk_deletePackageCommonNote.py"])
