#import MeCab
#from gensim.models import word2vec
#from gensim.models import KeyedVectors
import gensim
import pandas as pd
import numpy as np
from janome.tokenizer import Tokenizer
import random

def w2v():
    #モデルの読み込み
    #model = word2vec.Word2Vec.load("./.w2v")
    #model = KeyedVectors.load_word2vec_format("./entity_vector/entity_vector.model.bin",binary=True)
    model = gensim.models.KeyedVectors.load_word2vec_format('./model.vec', binary=False)
    #形態素解析
    '''
    def mecab(text):
        mt = MeCab.Tagger('')
        mt.parse('')
        text = mt.parseToNode(text)
        return text
    '''
    t = Tokenizer()
    text = '弱火にして焼き肉のタレを入れて、絡める。火を止めて、3cm長さに切った、万能ねぎを散らす。蓋をして蒸らす。'

    noun_list=[]
    noun_list=[token.surface for token in t.tokenize(text)if token.part_of_speech.startswith('名詞')]

    #print(noun_list)
    #print(token.infl_form)

    # テキストのベクトルを計算
    """
    def get_vector(text):
        sum_vec = np.zeros(200)
        word_count = 0
        node = mecab(text)
        while node:
            fields = node.feature.split(",")
            # 名詞、動詞、形容詞に限定
            #print(fields)
            if fields[0] == '名詞' or fields[0] == '動詞' or fields[0] == '形容詞':
                #print(sum_vec)
                sum_vec += model.wv[node.surface]
                #print(sum_vec)
                word_count += 1
            node = node.next
        return sum_vec / word_count
    """
    # cos類似度を計算
    #def cos_sim(v1, v2):
    #    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    #------------------------------------------------------------------------------------
    #テキスト間の類似度を測る
    #学習にない単語があるとエラーが出る
    """
    v1 = get_vector("昨日、お笑い番組を見た。")
    v2 = get_vector("昨夜、テレビで漫才をやっていた。")
    v3 = get_vector("昨日、公園に行った。")

    print(cos_sim(v1, v2))
    print(cos_sim(v1, v3))
    """
    #------------------------------------------------------------------------------------
    #類義語の発見
    #コサイン類似度が高い順に並ぶ
    #学習にない単語を入れるとエラーが出る

    for noun in noun_list:
        if len(noun)==1:
            noun_list.remove(noun)

    synonyms=[]
    results = model.most_similar(positive=random.choice(noun_list), topn=10)
    for result in results:
        synonyms.append(result[0])
        #print(result[0], '\t', result[1])

    print(random.choice(synonyms))

    return random.choice(synonyms)




#-----------------------------------------------------------------------------------
#王様＋女-男＝？？？の例
#results = model.most_similar(positive=[u"王様",u"女"], negative=[u"男"],topn=10)
#results = model.most_similar(positive=[u"千葉",u"台風"])

#for result in results:
#    print(result[0], '\t', result[1])
