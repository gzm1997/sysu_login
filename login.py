"""
login模块，负责登陆和获取选课结果
"""

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from PIL import Image
from urllib import parse
from icode import get_icode_from_img as get_icode
from encryption import sysu_entryption
#登陆页面url
login_url = "http://uems.sysu.edu.cn/elect/index.html?_t=1496741964444"
#验证码下载url
icode_url = "http://uems.sysu.edu.cn/elect/login/code"
#登陆提交表单url
post_url = "http://uems.sysu.edu.cn/elect/login"

"""
headers = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2",
	"Cache-Control":"max-age=0",
	"Content-Length":"104",
	"Content-Type":"application/x-www-form-urlencoded",
	"Cookie":"JSESSIONID=CDCA5110EBCB6C28E87FE71057CE0D21",
	"Host":"uems.sysu.edu.cn",
	"Origin":"http://uems.sysu.edu.cn",
	"Proxy-Connection":"keep-alive",
	"Referer":"http://uems.sysu.edu.cn/elect/index.html?_t=1496741964444",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
"""
#登陆和各种请求的cookie
cookies = {
	"JSESSIONID": "CDCA5110EBCB6C28E87FE71057CE0D21"
}

#使用代理
proxies = {
	"http": "http://127.0.0.1:1080",
	"https": "http://127.0.0.1:1080"
}

#创建session对话
s = requests.Session()
#对登陆页面发送get请求
r = s.get(login_url)

#下载验证码
r = s.get(icode_url)
content = r.content
print(content)
#保存验证码到本地
f = open("icode.png", "wb")
f.write(content)
f.close()

#使用icode模块获取验证码图片中的数字
jcode = get_icode()
print(jcode)

#使用encryption模块对密码进行加密
password = sysu_entryption("01254834")
print(password)

#准备登陆表单
data = {
	"username":"15331094",
	"password":password,
	"j_code":jcode,
	"lt":"",
	"_eventId":"submit",
	"gateway":"true"
}
#提交表单登陆
r = s.post(post_url, data = data, cookies = cookies)
print(r.text)

#获取选课结果的url，这个url每次都不一样，要注意
bobj = BeautifulSoup(r.text, "html.parser")
info_url = "http://uems.sysu.edu.cn/elect/s/" + bobj.find("a", {"class": "btn"})["href"]

#获取选课结果页面
r = s.get(info_url, cookies = cookies)
print(r.text)

#把选课结果页面保存到本地
f = open("after_login.html", "wb")
f.write(r.content)
f.close()
