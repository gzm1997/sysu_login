# 破解中山大学选课系统验证码自动登陆

标签（空格分隔）： 验证码破解 模拟登陆

----------

[此项目github地址][1]

----------
## 使用 ##
1，下载本项目到本地
2，进入主目录，输入以下命令安装相关依赖：

    pip install -r requirements.txt

3，在如下59和64行输入你的账号和密码：
![输入账号密码][2]
4，输入一下命令运行代码：

    python login.py

运行之后打印不少内容：
第一个是一个byte,内容就是下载下来的验证码：
![验证码][3]
第二个是登陆后的页面：
![登陆之后][4]
第三个是我的选课结果：
![选课结果][5]


----------

最后可以发现本地生成了一个after_login.html的html文件，打开之后发现你的选课结果被下载下来了：
![选课结果][6]
## 功能 ##

 - icode模块负责图片去噪和识别验证码
 - entryption模块负责加密密码
 - login模块负责登陆和抓取一些页面


  [1]: https://github.com/15331094/sysu_login
  [2]: https://github.com/15331094/sysu_login/blob/master/screenshots/input.png?raw=true
  [3]: https://github.com/15331094/sysu_login/blob/master/screenshots/icode.png?raw=true
  [4]: https://github.com/15331094/sysu_login/blob/master/screenshots/after_login.png?raw=true
  [5]: https://github.com/15331094/sysu_login/blob/master/screenshots/my_lesson.png?raw=true
  [6]: https://github.com/15331094/sysu_login/blob/master/screenshots/lession.png?raw=true
