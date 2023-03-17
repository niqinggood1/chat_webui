from flask import Flask,  render_template, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename
import os
from datetime import timedelta
import urllib
import requests
import json

app = Flask(__name__)

@app.route('/')  # 匹配路由
def hello():
    return render_template('index.html')

# 进入主页
@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')


from knowledge_graph_search import chat

@app.route('/returnMessage',methods=['GET','POST'])
def returnMessage():
    ip_addr      = request.remote_addr
    send_message = request.values.get("send_message")
    print( str(ip_addr) + "发送的消息：" + send_message)
    # url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(send_message))
    # html = requests.get(url)
    # if len(send_message)>100:
    #     print('in put',send_message)
    #     return json.dumps({'message': 'Ok', 'success': 1, 'content': "输入过长，可以考虑重新组织输入"})

    #违规内容，容内规违
    for k in ['国家','习近平','近平','大大','党','政府','中国经济','李克强','毛泽东','江泽民','军队']:
        if k in send_message :
            return 'wgnrnrwg'

    ret     = ''
    if '症状' in send_message or '怎么办'in send_message or '吃什么' in send_message or '药' in send_message:
        ret = chat( send_message )

    if ret in ['','##知识谱图暂未有答案' ]:

        json_data = json.dumps({'text': urllib.parse.quote(send_message) ,
                                'username': ip_addr.replace('.','-') })                        # 本次请求request_id
        html = requests.post('http://112.47.35.97:28648//gpt_chat', data=json_data)
        print("自动回复消息："+ html.json()["content"])
        html_content    = html.json()["content"]
        ret             = html_content
    #违规内容，容内规违
    for k in ['习近平','近平','大大','党','李克强','毛泽东','江泽民','军队']:
        if k in ret :
            return 'wgnrnrwg'
    return  ret

@app.route('/feedback',methods=['GET','POST'])
def feedback():
    ip_addr     = request.remote_addr
    send_message = request.values.get("send_message")
    feedback     = request.values.get("feedback")
    print(str(ip_addr) +'  feedback:'+ feedback + "   收到的消息：" + send_message)
    json_data = json.dumps({'text': urllib.parse.quote(send_message),
                            'feedback':feedback,
                            'username': ip_addr.replace('.', '-')})  # 本次请求request_id
    html = requests.post('http://112.47.35.97:28648//feedback', data=json_data)
    print("自动回复消息：" + str(html) )
    return ''

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--risk_identify',  action='store_false', required=False, help='')
    parser.add_argument('--host', default='0.0.0.0', type=str, required=False, help='')
    parser.add_argument('--port', default=6006, type=int, required=False, help='')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=True)
    app.run(debug=True)