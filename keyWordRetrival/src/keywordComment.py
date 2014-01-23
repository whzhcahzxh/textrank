#-*- coding:UTF-8 -*-
'''
Created on Dec 26, 2013

@author: administrator
'''
import testTextrank
import pymongo
from emotionalDicAnalysis import emotionAnalysis

a = emotionAnalysis()

conn=pymongo.Connection('localhost',27017)
db=conn.test
dbCollecton = db.purecontent

cursor = dbCollecton.find().limit(100)
testTextrank.wordAdd('/home/administrator/Python/dicLibrary/user.dic')
for sentence in cursor:
    print sentence['content']
    summary = testTextrank.textrank(sentence["content"])
    if len(summary)>1:
        print "分数："+ str(emotionAnalysis.calculateSentiment(a,summary))