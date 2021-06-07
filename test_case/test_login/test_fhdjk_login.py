# import requests
# import pytest
#
# def loginfunc(userAccount,userPwd):
#     url = "http://www.fhd001.com/loginAccount.do"
#     header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
#                   "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#                   "Referer":"http://www.fhd001.com/" }   # get方法其它加个ser-Agent就可以了
#     body = {"userAccount":userAccount,
#                 "userPwd":userPwd} #参数存字典
#     s = requests.session()
#     request = s.post(url=url,data=body,headers=header)
#     r   =  request.json()  #解析json
#     print("返回的结果:%s"% request.text)
#     return r
#
# def test_login_normal():  # 测试用例
#     '''正例:正确入参'''
#     result = loginfunc(userAccount="15167168967",userPwd="123456")
#
#     #期望结果 "rcode":0,"scode":0
#     expect_result = {"rcode":0,"scode":0}
#
#     #实际结果
#     rcode = result["rcode"]
#     print("返回的rcode:%s"%rcode)
#     scode = result["scode"]
#     print("返回的scode:%s"%scode)
#
#     #断言
#     assert result["rcode"] == expect_result["rcode"] and result["scode"] == expect_result["scode"]
#
# def test_login_pwd_error():  # 测试用例
#     '''反例:密码错误'''
#     result = loginfunc(userAccount="15167168967",userPwd="1234567")
#
#     #期望结果 "rcode":1,"scode":104
#     expect_result = {"rcode":1,"scode":104}
#
#     #实际结果
#     rcode = result["rcode"]
#     print("返回的rcode:%s"%rcode)
#     scode = result["scode"]
#     print("返回的scode:%s"%scode)
#
#     #断言
#     assert result["rcode"] == expect_result["rcode"] and result["scode"] == expect_result["scode"]
#
#
# if __name__ == "__main__":
#
#      pytest.main(["-s","-v","test_fhdjk_login.py"])
