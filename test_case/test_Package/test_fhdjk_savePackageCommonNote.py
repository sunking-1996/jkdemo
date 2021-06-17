import requests
import pytest
import allure
from urllib import parse
from test_case.conftest import test_data
from common.read import get_cookies,get_headers


@allure.story("---保存包裹常用备注用例---")
@pytest.mark.parametrize("packageNote,rcode,scode",test_data["packageNote"])
def test_savepackNote(packageNote,rcode,scode):
    s = get_headers()
    #decode解码
    fhd_token=parse.unquote(get_cookies()[1])
    url = "http://typapi.fhd001.com/api/package/savePackageCommonNote.do"
    body =  {"packageNote":packageNote,
             "token":fhd_token
    } #参数存字典
    s = requests.session()
    request = s.post(url=url,data=body)
    r   =  request.json()  #解析json

    ##实际结果
    assert r["rcode"] == rcode and r["scode"] == scode

if __name__ == "__main__":

     pytest.main(["-s","-v","test_fhdjk_savePackageCommonNote.py"])
