import yaml
import requests
import os
import sys
class Get_data():

    def get_cookies(self):
        self.url = "http://www.fhd001.com/loginAccount.do"
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
          "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
          "Referer":"http://www.fhd001.com/",
          "Cookie":"CNZZDATA1263048142=51987825-1583297402-null%7C1583313201; CNZZDATA1276886889=1211049750-1581389138-%7C1586500912; _pati=dceabddd4793a92e54b1f429d2dddc8b; fhdpdd_user_info_nick=cyccyccyc; fhdpdd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLRrXUnQ7n5vG2bXPMooFQYxyGw4vadia79F5plrgQdkrwBA3d2ObyDcpiaNYII98sBUIVxAqQmmKJA/132; fhd_user_info_nick=sunking; fhd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJiaGdSuKpkrLN4tlrze2OOHwicfS73TJKAScS9toziaicpjWUySrxgickrERnSicVbVtHJSC3Nx2EC5dyA/132; fhdcooperation_id=10086; fhdcooperation_username=%E5%AD%99%E5%BD%AA; fhdcooperation_isAdmin=false; fhdcooperation_isManage=false; fhdcooperation_departmentId=15; fhdcooperation_departmentName=%E7%A0%94%E5%8F%91%E4%B8%AD%E5%BF%83; fhdcooperation_postNo=10; fhdcooperation_postName=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88; fhdcooperation_token=%7EAwwTIwJBeHVHXVxHclFAJicdcHQZXgJdRFZKUAdfQFMbBQNKEiEOFCNUQFsDQSBRRgB3EAwJRnQDFiQOQ3J3E3IBEyRxQQECTlVVThIhU0EhDRQNdx0mCRJyIBNfBhZzAhF0URIlDBQnU0AjD0FdJkZ9BBB3AEYJDx9XA18HAwYHAw9fG1UJAVpSVVE%3D%7E1%7E; userHeadImgUrl=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTIdbOjlPgbBtWarETJdX2wSHQNx9icjrG2mpoTuUX6Uobk73BJq6Qh1pB84xC8DBURHfsqQeohlDVA%2F132; yunxu_username=%E5%AD%99%E5%BD%AA; yunxu_token=%7EClPWnK7QjstICAEPA1JSBwFTAE5QAQc%3D%7E1%7E; yunxu_chooseProjectCookieKey=123; JSESSIONID=538A8A21B4CBFD9CCBDF4490F852DE08.fap1-fhdcommon"
        }
        self.body = {
            "userAccount":"15167168967",
            "userPwd":"123456"
        }
        self.s = requests.session()
        request = self.s.post(url=self.url,data=self.body,headers=self.header,verify = False)
        cookies = requests.utils.dict_from_cookiejar(request.cookies)#转换cookies格式
        commonpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))#获取上级目录
        yamlpath = commonpath+'\data\cookies.yaml'#创建路径文件
        tokenValue = {
            'cookies':cookies
        }

        with open (yamlpath,"w",encoding='utf-8')as f:
            yaml.dump(tokenValue,f,Dumper=yaml.Dumper)

if __name__ == '__main__':
    a = Get_data()
    a.get_cookies()