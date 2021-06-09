import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse
import os


from urllib3 import encode_multipart_formdata
class DingDingWebHook():
    def __init__(self):
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=cbc99fa1f9401d73fdf11fac01b3db54b78f51280d1f94e48107069abb4e13c0'
        #self.data = recycle.cancelWaybillCode()
        self.access_token = 'cbc99fa1f9401d73fdf11fac01b3db54b78f51280d1f94e48107069abb4e13c0'
        self.secret = 'SECbe48725f2e15147e6dffdac51dabba7be70078cefee5448636065235d06e0b05'
    def get_url(self):
        timestamp = str(round(time.time() * 1000))
        secret = self.secret
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        # print(timestamp)
        # print(sign)
        url = self.url+'&timestamp='+timestamp+'&sign='+sign
        # print(url)
        return url

    # def get_token(self):
    #     params = {
    #         # "appkey": self.appkey,
    #         "appsecret": self.secret
    #     }
    #     try:
    #         res = requests.get("https://oapi.dingtalk.com/gettoken", params=params)
    #         access_token = res.json().get("access_token")
    #         print(access_token)
    #         return access_token
    #     except Exception as e:
    #         print(e)
    # def get_media_id(self):
    #     '''上传文件并且返回对应的media_id'''
    #     url_post = "https://oapi.dingtalk.com/media/upload?access_token="+self.get_token()+'&type=file'
    #     headers = {}
    #     data = {'access_token': self.access_token,'type': 'file'}
    #     #获取路径
    #     path = os. path.dirname(os.path.dirname(__file__))+ '/data/cookies.yaml'
    #     # files = {'media':open(path,'rb')}
    #     file_name = 'cookies.yaml'
    #     data['media'] = (file_name, open(path, 'rb').read())  # 说明：file_name,不支持中文，必须为应为字符
    #     print(data['media'])
    #     encode_data = encode_multipart_formdata(data)
    #     data = encode_data[0]
    #     headers['Content-Type'] = encode_data[1]
    #     r = requests.post(url_post,headers=headers, data=data)
    #     print(r.text,r.status_code)
    #     media_id = json.loads(r.text)["media_id"]
    #     print(media_id)
    #     return media_id
    def dingTalk(self):

        headers={
            "Content-Type": "application/json",
            "Charset": "UTF-8"
                }
        send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data = {
            "actionCard": {
                "title": "测试",
                "text":"%s \n\n更新时间：%s \n\n报告地址 %s" % ('测试报告', send_time,"http://localhost:8080/jenkins/job/jkdemo/allure/"),
                "hideAvatar": "0",
                "btnOrientation": "0"
            },
            "msgtype": "actionCard"
        }
        r = requests.post(self.get_url(), data=json.dumps(data), headers=headers)
        print(r.text)
        return json.loads(r.text)

    # def get_urltext(self):
    #     path = os.path.dirname(os.path.dirname(__file__))
    #     yamlpath = path + 'HTML/login.html'
    #
    #     option = webdriver.ChromeOptions()
    #     option.add_argument('--headless')
    #     driver = webdriver.Chrome(chrome_options=option)

if __name__ == '__main__':
    a =DingDingWebHook()
    a.dingTalk()

