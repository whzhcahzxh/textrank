#-*- coding:UTF-8 -*-
'''
Created on Dec 27, 2013

加入了否定词库，将否定词和其后的非否定词合并为同一个词，如果否定词接否定词，则合并并等待下一个非否定词

@author: administrator
'''

import jieba
def cut(content):
    #     否定词
    fp = open('/home/administrator/Python/dicLibrary/negator.dic','r')
    negator=[]
    for word in fp:
        word = word.strip()
        word=word.replace("\n","")
        negator.append(word)
    fp.close()
    
    outTemp = list(jieba.cut(content))
    out = []
    temp = ""
    for word in outTemp:
        if word in negator:
            temp = word+temp
        else:
            word = temp+word
            temp=""
            out.append(word)
    if len(temp)>0:
        out.append(temp)
    return out

def load_userdict(path):
    jieba.initialize()
    jieba.load_userdict(path)

if __name__=="__main__":
    out=cut("不不喜欢我")
    for i in out:
        print i+"|"
