#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：chat_webui 
@File    ：knowledge_graph_search.py
@IDE     ：PyCharm 
@Author  ：patrick
@Date    ：2023/3/17 19:13 
'''
from question_classifier import *
from question_parser import *
from answer_search import *
class ChatBotGraph:
    def __init__(self, host="127.0.0.1",http_port=7474,user="neo4j",password="neo4j"):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher( host=host ,http_port=http_port,user=user,password= password )

    def chat_main(self, sent):
        answer = '##知识谱图暂未有答案'
        res_classify = self.classifier.classify(sent)   #get question_types, and  query node
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)

global handler
handler= ChatBotGraph()
def chat( request ):
    global handler
    ret = handler.chat_main( request )
    return ret


if __name__ == '__main__':
    ret = chat(  '感冒了吃什么药')
    print('ret:',ret)
    exit()
    
  
  