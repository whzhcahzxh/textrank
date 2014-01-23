# -*- coding: UTF-8 -*-
import cProfile as profile
import pstats
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import pydot

import networkx as nx

import combineNegatorSeg
import jieba.analyse as analyser

def wordAdd(path):
    combineNegatorSeg.load_userdict(path)
    
def textrank(content):
    sents = list(combineNegatorSeg.cut(content))
#     停用词
    fp = open('/home/administrator/Python/dicLibrary/stopword.dic','r')
    stopwordList=[]
    for word in fp:
        stopwordList.append(word[:-1])
    fp.close()

    
    for word in sents:
        if word in stopwordList:
            sents.remove(word)
    if len(sents)<=4:
        print "short sentence"
        return []
    vect = TfidfVectorizer(min_df=1)
#     vect.fit(big_corpus)
    try:
        tfidf = vect.fit_transform(sents)
        tfidf_graph = tfidf*tfidf.T
    except ValueError:
        print "vocabulary error"
        return []
    
    nx_graph = nx.from_scipy_sparse_matrix(tfidf_graph)
    scores = nx.pagerank(nx_graph)
    res = sorted(((scores[i],i) for i,s in enumerate(sents)), reverse=True)
    wordRankList = sorted(res, key=lambda x:x[0], reverse=True)
    summary=[]
    count=0
    for score,i in wordRankList:
        if sents[i] not in summary:
            summary.append((sents[i],score))
            count+=1
        if count>=5:
            break
    
#     print 'text_rank', u'|'.join(summary).replace('\r','').replace('\n','')
    return summary


def tf_idf(content):
    print "TF-IDF:"+"|".join(analyser.extract_tags(content, 5))
    return list(analyser.extract_tags(content, 5))


if __name__=="__main__":
    text="八一双鹿电池没喜欢吃不想"
    wordAdd('/home/administrator/Python/dicLibrary/user.dic')
    summary = textrank(text)
    for doc in summary:
        print doc
#     tf_idf(text)