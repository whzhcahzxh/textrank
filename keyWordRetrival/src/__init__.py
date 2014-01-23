# -*- coding:UTF-8 -*-

import pymongo
import testTextrank
import filterWeibo
from emotionalDicAnalysis import emotionAnalysis

a = emotionAnalysis()

conn = pymongo.Connection('localhost',27017)
dbCollection = conn.test.database

cursor = dbCollection.find({"lanmu":"我是歌手"})
testTextrank.wordAdd('/home/administrator/Python/dicLibrary/user.dic')
for doc in cursor:
    neirong = filterWeibo.filtering(doc['content'])
    print "内容: "+neirong
    summary = testTextrank.textrank(neirong)
    if len(summary)>1:
        print "分数："+ str(a.calculateSentiment(summary))