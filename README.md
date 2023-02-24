# web_chatbot
网页版的聊天机器人，基于flask，无聊之作，图一乐

在线demo：[http://www.yhqiao.xyz:5000/index](http://www.yhqiao.xyz:5000/index)

用的青云客智能聊天机器人免费api（不用注册申请直接可以用）

安装下flask 框架 运行`flask_main.py`,打开本地浏览器访问`127.0.0.1:5000/index`就可以了

```
def qingyunke(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]
msg = '我好看吗'
print("原话>>", msg)
res = qingyunke(msg)
print("青云客>>", res)
```
![image](https://github.com/YhQIAO/blog_images/blob/main/chatbot.png)
