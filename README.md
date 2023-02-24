# web_chatbot

安装下flask 框架 运行`flask_main.py`,打开本地浏览器访问`127.0.0.1:5000/index`就可以了

```
def qingyunke(msg):
    url = 'http://******/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]
msg = '我好看吗'
print("原话>>", msg)
res = qingyunke(msg)
print("res>>", res)
```

