
import convXML as MakeLine
import xml.etree.ElementTree as ET
from xml.dom import minidom
import queue

import MeCab
#from gensim.models import word2vec
#from gensim.models import KeyedVectors
import pandas as pd
import numpy as np



# 出力ファイルパス
OUTPUT_FILE_PATH = "./output_test_1.xml"


def ToMinidom(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    return minidom.parseString(rough_string)


def Fairing(rootN):
    R = ToMinidom(rootN).toprettyxml(indent="\t", newl="\n", encoding="UTF-8")
    # R=R.replaceex("?>","?>"+XSL,1)
    return R


ret = []


def make(name, line,command={}):
    global ret
    ret.append(MakeLine.Make(name, line, command))


# 初期化
MakeLine.Reset()
ret.append(MakeLine.Refresh())

##########################################
#               漫才台本部分
##########################################

#ニュース漫才用テンプレート
title="一括回収でリサイクル強化、プラごみ削減、新法成立"
sentence="プラスチックごみのリサイクル強化と排出削減に向けた新法「プラスチック資源循環促進法」が4日の参院本会議で、全会一致で可決、成立した。家庭から出る食品トレーやおもちゃなどを市区町村が一括回収するよう要請。使い捨てスプーンやストローを多く提供する事業者には、有料化を含めた削減策を義務付ける。2022年4月の施行を目指す。海洋汚染の一因ともされるプラごみ削減と地球温暖化対策を進めるのが狙い。ただ一括回収は市区町村の負担増につながり、全国各地に広がるかどうか見通せない。有料化には、事業者や消費者の反発も予想される。"


#形態素解析
def mecab(text):
    m = MeCab.Tagger("Ochasen")
    text=m.parse(text)
    return text


#簡単な言葉遊びボケ
result=[]
noun=[]
text_split=[]

#記事を「。」で区切る
#text=sentence.split("。")

text=title

#テキストを形態素解析する
for i in text:
    t=mecab(i)
    t=t.strip()
    result.append(t)
#print(result)

#形態素解析した文をリストにしてあつかいやすいようにする
for detail in result:
    detail=detail.replace("\t",",")
    detail=detail.replace(","," ")
    res = detail.split("\n")
    noun.append(res)
#print(noun)

#名詞をとる
"""
for item in noun:
    text1=[]
    for i in item:
        i=i.split(" ",10)
        if i[0]=="EOS":
            break
        if i[1]=="名詞":
            text1.append(i[0])
    text_split.append(text1)
print(text_split)
"""

#言葉遊びボケ例
#名詞を
#文を変える
text1=[]
for item in noun:
    for i in item:
        i=i.split(" ",10)
        #print(i)
        if i[0]=="EOS":
            break
        if i[1]=="名詞":
            text1.append(i[0])
    #print(text1)
for i in range(5):  
    text=text.replace("{}".format(text1[i]),"{}".format(text1[1]))
    #print(text)
#print(text)
title1=text




#ニュース漫才用テンプレート
"""
<基本説明>
"mary": あいちゃん，"bob": ゴン太
line: 発話部分(合成音声の仕様により読み間違える場合はひらがな指定をする)
"ballon": 表示部分
"""

make("mary", {
    "line": "どーも、あいちゃんです",
    "balloon": "どーも、あいちゃんです"
})

make("bob", {
    "line": "どーも、ゴンタです",
    "balloon": "どーも、ゴン太です"
})

# 表情調整

make("mary", {
    "line": "テレビのニュースキャスターはすごいよね",
    "balloon": "テレビのニュースキャスターは凄いよね",
    "face": "neutral"
})

make("mary", {
    "line": "ニュースをしょうかいしながらしかいもできるし",
    "balloon": "ニュースを紹介しながら司会もできるし",
    "face": "neutral"
})

make("bob", {
    "line": "そそそんなのかんたんだよよよ、じじじんこうちのうを使えばおれにだってできるわわわわ",
    "balloon": "そそそんなのかんたんだよよよ、じじじ人工知能を使えばおれにだってできるわわわわ",
    "face": "neutral"

},
    {"line": {
        "volume": "20%",
    }
})

make("mary", {
    "line": "おいおいかみすぎや、きみにはむいてないぞ",
    "balloon": "おいおい噛みすぎや、きみにはむいてないぞ",
    "face": "neutral"
},
    {"line": {
        "pitch": "300%",
    }
})

make("bob", {
    "line": "おおおっと、ねねねじが一本たりてなかった",
    "balloon": "おおおっと、ねねねじが一本たりてなかった",
    "face": "neutral"
},
    {"line": {
        "pitch": "130%",
        "speed": "200%",
        "volume": "80%"
    }
})

make("bob", {
    "line": "よいしょ、もとのもどったぜ",
    "balloon": "よいしょ、元に戻ったぜ",
    "face": "neutral"
})

make("mary", {
    "line": "メンテナンスはまいにちしなはれ",
    "balloon": "メンテナンスは毎日しなはれ",
    "face": "neutral"
},
    {"line": {
        "volume": "800%",
    }
})

make("bob", {
    "line": "きをつけます",
    "balloon": "気を付けます",
    "face": "neutral"
})

#本題
#-------------------------------------------------------------
make("mary", {
    "line": "もとにもどったことだし、ニュースキャスターとしてきじでもよんでもらおうか、ほれ",
    "balloon": "元に戻ったことだし、ニュースキャスターとして記事でも読んでもらおうか、ほれ",
    "face": "neutral"
},
    {"line": {
        "speed": "150%",
    }
})

make("mary", {
    "line": "タイトルは"+title+"や",
    "balloon": "タイトルは『"+title+"』や",
    "face": "neutral"
})
#ボケ1
make("bob", {
    "line": "タイトルは"+title1+"か、これならいけるわ",
    "balloon": "タイトルは『"+title1+"』か、これならいけるわ",
    "face": "neutral"
})

make("mary", {
    "line": "おいおい、いきなりまちがっとるやないか",
    "balloon": "おいおい、いきなりまちがっとるやないか",
    "face": "anger"
})

make("bob", {
    "line": "おっとすまん、コンタクトをつけてなかったわ",
    "balloon": "おっとすまん、コンタクトをつけてなかったわ",
    "face": "neutral"
})

make("mary", {
    "line": "ロボットにこんたくとはいらんやろ、しっかりせいや",
    "balloon": "ロボットにこんたくとはいらんやろ、しっかりせいや",
    "face": "anger"
})

make("bob", {
    "line": "ほなよんでいくで",
    "balloon": "ほな読んでいくで",
    "face": "neutral"
})
make("bob", {
    "line": ""+sentence+"",
    "balloon": ""+sentence+"",
    "face": "neutral"
})

make("mary", {
    "line": "ほむほむ",
    "balloon": "ほむほむ",
    "face": "happy"
})
#ボケ2
make("bob", {
    "line": ""+sentence+"",
    "balloon": ""+sentence+"",
    "face": "haughty"
})

make("mary", {
    "line": "おいおい、ちょっとまて",
    "balloon": "おいおい、ちょっとまて",
    "face": "happy"
})

make("mary", {
    "line": "そうなんですね～",
    "balloon": "そうなんですね～",
    "face": "idyllic"
})

#ニュース記事を読み終えて
#-------------------------------------------------
#おち
make("mary", {
    "line": "もうええわ、ロボットなのにニュース記事もろくに読めないのかよ、ロボットやめたほうがええで",
    "balloon": "もうええわ、ロボットなのにニュース記事もろくに読めないのかよ、ロボットやめたほうがええで",
    "face": "idyllic"
})

make("bob", {
    "line": "最後に挽回するチャンスをください",
    "balloon": "最後に挽回するチャンスをください",
    "face": "haughty"
})

make("mary", {
    "line": "ほな、今回のニュース記事を要約してもらおうか",
    "balloon": "ほな、今回のニュース記事を要約してもらおうか",
    "face": "idyllic"
})
#ボケ3
make("bob", {
    "line": "なな",
    "balloon": "なな",
    "face": "haughty"
})
make("mary", {
    "line": "もうええわ",
    "balloon": "もうええわ",
    "face": "idyllic"
})


############################
#       台本生成部分
############################
rootN = ET.Element("manzai")
metaD = ET.SubElement(rootN, "meta")
metaD.set("content", "HeadlineNews")
script = ET.SubElement(rootN, "script")
Q = queue.Queue()
# PlaceManzai.make(logger,Q,Pref,City)
[Q.put(E) for E in ret]
while not Q.empty():
    script.append(Q.get())
R = Fairing(rootN)
with open(OUTPUT_FILE_PATH, "wb" if isinstance(R, bytes) else "w") as f:
    f.write(R)

