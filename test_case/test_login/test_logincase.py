import requests
import pytest
import allure
from test_case.conftest import test_data

#参数写死的方法
# test_data=[
#         ({"userAccount":"15167168967","userPwd":"123456"},{"rcode":0,"scode":0}),
#         ({"userAccount":"15167168967","userPwd":"1234567"},{"rcode":1,"scode":104}),
#         ({"userAccount":"15167168967","userPwd":""},{"rcode":1,"scode":100}),
#         ({"userAccount":"","userPwd":"123456"},{"rcode":1,"scode":100}),
#         ({"userAccount":"","userPwd":""},{"rcode":1,"scode":100}),
#         ({"userAccount":"None","userPwd":"None"},{"rcode":1,"scode":104})
# ]

for key, value in test_data.items():
    if key == 'test_login':
        logger.info("获取的登录参数为：{}".format(value))
    body = value

@allure.story("---登录用例---")
@pytest.mark.parametrize("test_input,expect",body)
def test_loginfunc(test_input,expect):
    url = "http://www.fhd001.com/loginAccount.do"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
                  "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                  "Referer":"http://www.fhd001.com/" }   # get方法其它加个ser-Agent就可以了
    body = {"userAccount":test_input['userAccount'],
                "userPwd":test_input['userPwd']
    } #参数存字典
    s = requests.session()
    request = s.post(url=url,data=body,headers=header)
    r   =  request.json()  #解析json
    assert r["rcode"] == expect["rcode"] and r["scode"] == expect["scode"]

if __name__ == "__main__":

     pytest.main(["-s","-v","test_logincase.py"])
