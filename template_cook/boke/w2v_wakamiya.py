#import MeCab
#from gensim.models import word2vec
#from gensim.models import KeyedVectors
import gensim
import pandas as pd
import numpy as np
from janome.tokenizer import Tokenizer
import random

from gensim.models import word2vec
from gensim.models import KeyedVectors


def w2v(text):
    #モデルの読み込み
    #model = word2vec.Word2Vec.load("./.w2v")
    model = KeyedVectors.load_word2vec_format("./../../entity_vector/entity_vector.model.bin",binary=True)
    #model = gensim.models.KeyedVectors.load_word2vec_format('./model.vec', binary=False)
    
    t = Tokenizer()
    #text = '弱火にして焼き肉のタレを入れて、絡める。火を止めて、3cm長さに切った、万能ねぎを散らす。蓋をして蒸らす。'
    noun_list=[]
    noun_list=[token.surface for token in t.tokenize(text)if token.part_of_speech.startswith('名詞')]

    #類義語の発見
    #コサイン類似度が高い順に並ぶ
    #学習にない単語を入れるとエラーが出る
    for noun in noun_list:
        if len(noun)==1:
            noun_list.remove(noun)

    #print(noun_list)
    synonyms=[]
    count=0
    while(count==0):
        try:
            word=random.choice(noun_list)
            results = model.most_similar(positive=word, topn=10)
            count=1
        except:
            count=0

    #print("変化前：" + word)
    for result in results:
        synonyms.append(result[0])
        #print(result[0], '\t', result[1])

    word2=random.choice(synonyms)
    #print("変化後："+word2)

    text1=text.replace(word,"『"+word+"』")
    text2=text.replace(word,"『"+word2+"』")
    return text1,word,word2

def main():
    text = "大根は一口大にカットし、竹串が通るくらいまで下ゆでします。大根の葉は小口切りにしておきます。"
    #text1,text2= w2v(text)
    #print(text)
    #print(text2)


if __name__ == "__main__":
    main()


#-----------------------------------------------------------------------------------
#王様＋女-男＝？？？の例
#results = model.most_similar(positive=[u"王様",u"女"], negative=[u"男"],topn=10)
#results = model.most_similar(positive=[u"千葉",u"台風"])

#for result in results:
#    print(result[0], '\t', result[1])
