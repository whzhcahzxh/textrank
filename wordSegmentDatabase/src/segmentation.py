# -*- coding: UTF-8 -*-
'''
Created on Dec 26, 2013

@author: administrator
'''
import pymongo
import jieba
import time
t=time.clock()
conn = pymongo.Connection('localhost',27017)
db = conn.test
dbCollection = db.purecontent
wordCollection = db.word

# 去除停用词
stopwordList=[]
fp=open("/home/administrator/Python/dicLibrary/stopword.dic",'r')
for line in fp:
    line = line.strip()
    line = line.replace('\n',"")
    stopwordList.append(line)

cursor = dbCollection.find()
wordDic = []
sentenceCount=0
for sentencePiece in cursor:
    sentence = sentencePiece['content']
    words = jieba.cut(sentence)
    sentenceCount+=1
    for word in words:
        # 去除停用词
        if word.encode("UTF-8") not in stopwordList:
            wordDic.append(word)

print "insert"
wordList = {}.fromkeys(wordDic).keys()
for i in range(len(wordList)):
    word = wordList[i]
    newcount = wordDic.count(word)
    wordCollection.insert({"word":word,"count":newcount})

t=time.clock()-t
print "time: "+str(t)+"s"




