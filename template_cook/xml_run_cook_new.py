import convXML as MakeLine
import cookpad_date
import boke.Roberta as Ro
import boke.wiki as wiki
import boke.w2v_wakamiya as w2v
import datetime
import random

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

#今日の日付からスクレイピング
dt_now = datetime.datetime.now()
day=dt_now.strftime('%m%d')
c_new,url_new= cookpad_date.html(day)
c_old,url_old= cookpad_date.html(str(int(day)-1))
#print(c_new)

#料理名辞書からランダムに料理名を取得し，cookpadからスクレイピング
day_old=str(int(day)-1)
while(True):
    with open("./food/foodname.txt", "r", encoding="utf-8") as f:
        l = f.readlines()
        text = random.choice(l)
        cook_word = text.replace("\n", "")
        try:
            c_word = cookpad_date.html_word(cook_word)
            break
        except:
            continue
        #print(text.replace("\n",""))
"""
c_word2 = cookpad_date.html_word("天津飯")
print(c_word[2].replace("   ","，"))
c = ["タイトル", "要約", "材料", "手順(作り方)" ,"アドバイス", "歴史"]
print(c_new[3][0])
"""

#bertによるボケの生成
text_ro, word_ro= Ro.roberta(c_new[3][2])
#print(c_new[3][2][1:])
#print(text_ro.replace("▁", "")[1:])

#word2vecによるボケの生成
#print(c_word[3][1][1:])
text1, text2 = w2v.w2v(c_word[3][1][1:])



# 出力ファイルパス
OUTPUT_FILE_PATH = "./script/volume_test.xml"


# 初期化
MakeLine.init()
make = MakeLine.make


##########################################
#               漫才台本部分
##########################################

"""
<基本説明>
"mary": あいちゃん，"bob": ゴン太
line: 発話部分(合成音声の仕様により読み間違える場合はひらがな指定をする)
"ballon": 表示部分
"""

"""
<基本説明>
"mary": あいちゃん，"bob": ゴン太
line: 発話部分(合成音声の仕様により読み間違える場合はひらがな指定をする)
"ballon": 表示部分
title:

# 補足:  ** ++に単語を入れるようなフレームワークです。また、レシピのapiがあればいい感じになります。

"""
#-------------------------------------------
#はじめ
make("mary", {
    "line": "あいちゃんやで",
    "balloon": "あいちゃんやで",
    "face": "idyllic"
})

make("bob", {
    "line": "ゴンザレス。",
    "balloon": "ゴンザレス。",
    "face": "haughty"
})

make("mary", {
    "line": "ゴン太はすきなわしょくのこんだてってあるか？",
    "balloon": "ゴン太は好きな和食の献立ってあるか？",
    "face": "pleasant"
})

make("bob", {
    "line": "とうぜんながらバッテリーです。あ、わしょくだからなまりちくでんちか。",
    "balloon": "当然ながらバッテリーです。あ、和食だから鉛蓄電池か。",
    "face": "sad"
})

make("mary", {
    "line": "かなしいロボットのさが、やな。",
    "balloon": "悲しいロボットの性やな。",
    "face": "sad"
})

make("mary", {
    "line": "じゃあ食べてみたいものは？",
    "balloon": "じゃあ食べてみたいものは？",
    "face": "sad"
})

make("bob", {
    "line": cook_word+"です。",
    "balloon": cook_word+"です。",
    "face": "like"
})

make("bob", {
    "line": cook_word+"はママのあじー",
    "balloon": cook_word+"はママのあじー",
    "face": "happy"
})

make("mary", {
    "line": "おかあさん以外も作るし字余りなんよ。",
    "balloon": "お母さん以外も作るし、字余りなんよ。",
    "face": "pity"
})
#---------------------------------------------------------------
#料理1
make("mary", {
    "line": "ところで、"+cook_word+"ってどうやって作るっけ？",
    "balloon": "ところで、"+cook_word+"ってどうやって作るっけ？",
    "face": "shame"
})

make(
    "bob", {
        "line": "楽勝や、人工知能で調べたるわ。",
        "balloon": "楽勝や、人工知能で調べたるわ。",
        "face": "idyllic"
    })

make("mary", {
    "line": "さすがゴンザレス!",
    "balloon": "さすがゴンザレス!",
    "face": "shame"
})

make("bob", {
        "line": "材料は"+c_word[2].replace("   ","，")+"です。",
        "balloon": "材料は"+c_word[2].replace("   ","，")+"です。",
        "face": "idyllic"
})

make("mary", {
    "line": "長いなー",
    "balloon": "長いなー",
    "face": "idyllic"
})


make("bob", {
    "line": "えーと、まずは、"+c_word[2].replace("   ", "，").split("，")[0].replace(" ","")+"を作ります。",
    "balloon": "えーと、まずは、"+c_word[2].replace("   ", "，").split("，")[0].replace(" ","")+"を作ります。",
    "face": "idyllic"
})

make("mary", {
    "line": "ちょっと待て、どんだけかかるねん。",
    "balloon": "ちょっと待て、どんだけかかるねん。",
    "face": "idyllic"
})

make("bob", {
    "line": "5年くらいかかりますわ。",
    "balloon": "5年くらいかかりますわ。",
    "face": "idyllic"
})

make("mary", {
    "line": "おいおい、生産者になりたいわけじゃないねん。",
    "balloon": "おいおい、生産者になりたいわけじゃないねん。",
    "face": "idyllic"
})

make("mary", {
    "line": "料理の手順を教えてくれよ。",
    "balloon": "料理の手順を教えてくれよ。",
    "face": "idyllic"
})
try:
    make(
        "bob", {
            "line": "まずは、" + wiki.wiki_content(cook_word).split("。")[0] + "",
            "balloon": "まずは、" + wiki.wiki_content(cook_word).split("。")[0] + "",
            "face": "idyllic"
        })

    make("mary", {
    "line": "ちょっとまって、その情報のソースは？",
    "balloon": "ちょっとまって、その情報のソースは？",
    "face": "disagreeable"
    })

    make("bob", {
        "line": wiki.wiki_url(cook_word),
        "balloon": wiki.wiki_url(cook_word),
        "face": "idyllic"
    })

    make("mary", {
        "line": "いや、urlじゃわからんのよ。今見ているじょうほうげんを聞いとるねん。",
        "balloon": "いや、urlじゃわからんのよ。今見ている情報源を聞いとるねん。",
        "face": "angry"
    })

    make(
        "bob", {
            "line": "我らが大先生、wikipediaに決まってます!",
            "balloon": "我らが大先生、wikipediaに決まってます!",
            "face": "disagreeable"
        })

    make("mary", {
        "line": "嘘情報も多いし、大先生ではないんよ。",
        "balloon": "嘘情報も多いし、大先生ではないんよ。",
        "face": "disagreeable"
    })
except:

    make(
        "bob", {
            "line": "まず、" +c_old[5] + "",
            "balloon": "まず、" + c_old[5]+ "",
            "face": "idyllic"
        })


    make("mary", {
        "line": "ちょっとまって、説明やん、その情報のソースは",
        "balloon": "ちょっとまって、説明やん、その情報のソースは？",
        "face": "disagreeable"
    })

    make("bob", {
        "line": url_old,
        "balloon": "url省略",
        "face": "idyllic"
    })

    make("mary", {
        "line": "いや、urlじゃわからんのよ。今見ているじょうほうげんを聞いとるねん",
        "balloon": "いや、urlじゃわからんのよ。今見ている情報源を聞いとるねん",
        "face": "angry"
    })

    make(
        "bob", {
            "line": "我らが大先生、cookpadに決まってます",
            "balloon": "我らが大先生、cookpadに決まってます",
            "face": "disagreeable"
        })

    make("mary", {
        "line": "料理情報しかないし，大先生ではないんよ",
        "balloon": "料理情報しかないし，大先生ではないんよ",
        "face": "disagreeable"
    })

make("mary", {
    "line": "もうええわ、レシピの手順、最初から読んでくれ",
    "balloon": "もうええわ、レシピ手順、最初から読んでくれ",
    "face": "idyllic"
})

make(
    "bob", {
        "line": "" + c_word[3][0][1:] + "",
        "balloon": "" + c_word[3][0][1:] + "",
        "face": "idyllic"
    })

make("mary", {
    "line": "ふむふむ、次は？",
    "balloon": "ふむふむ、次は？",
    "face": "idyllic"
})

make("bob", {
    "line": ""+text1+"",
    "balloon": ""+text1+"",
    "face": "idyllic"
})
#ぼけ1
make("mary", {
    "line": "おいおい、"+text1+"やろ",
    "balloon": "おいおい、"+text2+"やろ",
    "face": "idyllic"
})

make("bob", {
    "line": "お、うっかりしてもう太郎",
    "balloon": "お、うっかりしてもう太郎",
    "face": "idyllic"
})

make("mary", {
    "line": "ちゃんと説明もできへんのかいな、最近の人工知能は衰えたなー",
    "balloon": "ちゃんと説明もできへんのかいな、最近の人工知能は衰えたなー",
    "face": "idyllic"
})
#-------------------------------------------------------------
#料理2
make("bob", {
    "line": "ちなみに、あいちゃんが好きな食べ物は何？",
    "balloon": "ちなみに、あいちゃんが好きな食べ物は何？",
    "face": "happy"
})

make("mary", {
    "line": "私は何でもかんでもいけるわ、本日のおすすめの料理は何？",
    "balloon": "私は何でもかんでもいけるわ、本日のおすすめの料理は何？",
    "face": "idyllic"
})

make("bob", {
    "line": "ゴンザレスが調べたるわ。",
    "balloon": "ゴンザレスが調べたるわ。",
    "face": "happy"
})

make("bob", {
    "line": "本日のオヌヌメ料理は"+c_new[0]+"です!",
    "balloon": "本日のオヌヌメ料理は"+c_new[0]+"です!",
    "face": "happy"
})

make("mary", {
    "line": "美味しそうやなー、作り方は？",
    "balloon": "美味しそうやなー、作り方は？",
    "face": "idyllic"
})

make("bob", {
    "line": "えーと，まずは"+c_new[4]+"完成です。",
    "balloon": "えーと，まずは"+c_new[4]+"完成です。",
    "face": "happy"
})

make(
    "mary", {
        "line": "そんな簡単に作れるわけないやろ。アドバイスはええから、ちゃんとよめや、ポンコツ!",
        "balloon": "そんな簡単に作れるわけないやろ。アドバイスはええから、ちゃんとよめや、ポンコツ!",
        "face": "idyllic"
    })

make("bob", {
    "line": "失礼、" + c_new[3][0][1:],
    "balloon": "失礼、" + c_new[3][0][1:],
    "face": "happy"
})

make("mary", {
    "line": "ほんで？",
    "balloon": "ほんで？",
    "face": "idyllic"
})

make("bob", {
    "line": "" + c_new[3][1][1:],
    "balloon": "" + c_new[3][1][1:],
    "face": "happy"
})

make("mary", {
    "line": "次、次!",
    "balloon": "次、次!",
    "face": "idyllic"
})
#ボケ2
make("bob", {
    "line": ""+text_ro.replace("▁", "")[1:],
    "balloon": ""+text_ro.replace("▁", "")[1:],
    "face": "happy"
})

make("mary", {
    "line": "なんでやねん、それはおかしいやろ。",
    "balloon": "何でやねん、それはおかしいやろ。",
    "face": "idyllic"
})

make("bob", {
    "line": "おっと，読み間違えたわ"+c_new[3][2][1:]+"やったわ",
    "balloon": "おっと，読み間違えたわ"+c_new[3][2][1:]+"やったわ",
    "face": "happy"
})

make("mary", {
    "line": "いい加減にしろよ、ぽつこん",
    "balloon": "いい加減にしろよ、ぽつこん",
    "face": "idyllic"
})

#--------------------------------------------------------------
#オチ

make("mary", {
    "line": "もうええわ、作り方なんもわからんから最後に簡単に要約してや",
    "balloon": "もうええわ、作り方なんもわからんから最後に簡単に要約してや",
    "face": "idyllic"
})

#(レシピのうち材料の名前を単語区切りに読む)
make("bob", {
    "line": ""+c_new[1]+"や、どうや",
    "balloon": ""+c_new[1]+"や、どうや",
    "face": "idyllic"
})

make("mary", {
    "line": "もうええわ、どうもありがとうございました。",
    "balloon": "もうええわ、どうもありがとうございました。",
    "face": "relief"
})

make("bob", {
    "line": "どうも、グノーシスしゅぎしゃ、ゴンザレスいや、ごんたでした。",
    "balloon": "どうも、グノーシス主義者、ゴンザレスいや、ゴン太でした。",
    "face": "happy"
})

##########################################
#               漫才台本出力
##########################################
MakeLine.makeScript(OUTPUT_FILE_PATH)
print("完了")
