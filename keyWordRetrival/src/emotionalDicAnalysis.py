# -*- coding:UTF-8 -*-
'''
Created on Dec 27, 2013

@author: administrator
'''
class emotionAnalysis():
    def __init__(self):
        self.negativeWordList = []
        self.positiveWordList = []
        
        fp = open('/home/administrator/Python/dicLibrary/sentimentalWord/negativeEmotion.dic')
        for word in fp:
            word = word.strip()
            word=word.replace("\n","")
            self.negativeWordList.append(word)
        fp.close()
        
        fp = open('/home/administrator/Python/dicLibrary/sentimentalWord/negativeJudgement.dic')
        for word in fp:
            word = word.strip()
            word=word.replace("\n","")
            self.negativeWordList.append(word)
        fp.close()
        
        fp = open('/home/administrator/Python/dicLibrary/sentimentalWord/positiveEmotion.dic')
        for word in fp:
            word = word.strip()
            word=word.replace("\n","")
            self.positiveWordList.append(word)
        fp.close()
        
        fp = open('/home/administrator/Python/dicLibrary/sentimentalWord/positiveJudgement.dic')
        for word in fp:
            word = word.strip()
            word=word.replace("\n","")
            self.positiveWordList.append(word)
        fp.close()
    
    def calculateSentiment(self,content):
        result=0
        for doc in content:
            if doc[0] in self.negativeWordList:
                result -= doc[1]
            elif doc[0] in self.positiveWordList:
                result += doc[1]
        return result
                
if __name__=="__main__":
    a=emotionAnalysis()
    print a.calculateSentiment([("鄙", 0.24096385528129585)])
    
    
    
    
    