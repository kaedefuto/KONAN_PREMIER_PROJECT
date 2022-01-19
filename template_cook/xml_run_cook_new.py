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
text1, word,word2 = w2v.w2v(c_word[3][2][1:])



# 出力ファイルパス
OUTPUT_FILE_PATH = "./script/{}.xml".format(cook_word)


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
    "line": "ゴンタはすきなわしょくのこんだてってあるか？",
    "balloon": "ゴンタは好きな和食の献立ってあるか？",
    "face": "pleasant"
})

make("bob", {
    "line": "とうぜんながらバッテリーです。",
    "balloon": "当然ながらバッテリーです。",
    "face": "sad"
})

make("bob", {
    "line": "あ、わしょくだからなまりちくでんちか。",
    "balloon": "あ、和食だから鉛蓄電池か。",
    "face": "haughty"
})

make("mary", {
    "line": "かなしいロボットのさがやな。",
    "balloon": "悲しいロボットの性やな。",
    "face": "sad"
})

make("mary", {
    "line": "じゃあ食べてみたいものは？",
    "balloon": "じゃあ食べてみたいものは？",
    "face": "neutral"
})

make("bob", {
    "line": cook_word+"です。",
    "balloon": cook_word+"です。",
    "face": "neutral"
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

make("bob", {
    "line": "ほんまや気がつかなかったわ",
    "balloon": "ほんまや気がつかなかったわ",
    "face": "happy"
})
#---------------------------------------------------------------
#料理1
make("mary", {
    "line": "ところで、"+cook_word+"ってどうやって作るか知ってるか？",
    "balloon": "ところで、"+cook_word+"ってどうやって作るか知ってるか？",
    "face": "idyllic"
})

make(
    "bob", {
        "line": "知らんから、人工知能で調べたるわ。",
        "balloon": "知らんから、人工知能で調べたるわ。",
        "face": "idyllic"
    })

make("mary", {
    "line": "さすがゴンザレス!",
    "balloon": "さすがゴンザレス!",
    "face": "neutral"
})

make("bob", {
        "line": "材料は"+c_word[2].replace("   ","，")+"です。",
        "balloon": "材料は"+c_word[2].replace("   ","，")+"です。",
        "face": "idyllic"
})

make("mary", {
    "line": "長いなー",
    "balloon": "長いなー",
    "face": "neutral"
})

make("mary", {
    "line": "作り方は？",
    "balloon": "作り方は？",
    "face": "idyllic"
})


make("bob", {
    "line": "えーと、まずは、"+c_word[2].replace("   ", "，").split("，")[0].replace(" ","")+"を作ります。",
    "balloon": "えーと、まずは、"+c_word[2].replace("   ", "，").split("，")[0].replace(" ","")+"を作ります。",
    "face": "neutral"
})

make("mary", {
    "line": "ちょっと待て、どんだけかかるねん。",
    "balloon": "ちょっと待て、どんだけかかるねん。",
    "face": "surprise"
})

make("bob", {
    "line": "5年くらいかかりますわ。",
    "balloon": "5年くらいかかりますわ。",
    "face": "neutral"
})

make("mary", {
    "line": "おいおい、生産者になりたいわけじゃないねん。",
    "balloon": "おいおい、生産者になりたいわけじゃないねん。",
    "face": "anger"
})

make("mary", {
    "line": cook_word+"の作り方を説明してくれよ。",
    "balloon": cook_word+"の作り方を説明してくれよ。",
    "face": "anger"
})
make("bob", {
        "line": "御意",
        "balloon": "御意",
        "face": "pleasant"
    })

make( "bob", {
        "line": "えーと、" + wiki.wiki_content(cook_word).split("。")[0] + "",
        "balloon": "えーと、" + wiki.wiki_content(cook_word).split("。")[0] + "",
        "face": "neutral"
    })

make("mary", {
        "line": "ちょっとまって、",
        "balloon": "ちょっとまって、",
        "face": "surprise"
    })

make("mary", {
        "line": "作り方じゃなくて"+cook_word+"の説明やん。",
        "balloon": "作り方じゃなくて"+cook_word+"の説明やん。",
        "face": "surprise"
    })

make("mary", {
        "line": "その情報のソースはどこから持ってきたんや？",
        "balloon": "その情報のソースはどこから持ってきたんや？",
        "face": "disagreeable"
    })

make("bob", {
        "line": wiki.wiki_url(cook_word),
        "balloon": wiki.wiki_url(cook_word),
        "face": "pleasant"
    })

make("mary", {
        "line": "いや、urlじゃわからんのよ。",
        "balloon": "いや、urlじゃわからんのよ。",
        "face": "angry"
    })

make("mary", {
        "line": "しかも、顔隠れとるやん。",
        "balloon": "しかも、顔隠れとるやん。",
        "face": "angry"
    })

make("mary", {
        "line": "今見ているじょうほうげんを聞いとるねん。",
        "balloon": "今見ている情報源を聞いとるねん。",
        "face": "angry"
    })

make("bob", {
        "line": "我らが大先生、wikipediaに決まってマッスル!",
        "balloon": "我らが大先生、wikipediaに決まってまっする!",
        "face": "pleasant"
    })

make("mary", {
        "line": "嘘情報も多いし、大先生ではないんよ。",
        "balloon": "嘘情報も多いし、大先生ではないんよ。",
        "face": "disagreeable"
    })

make("mary", {
    "line": "もうええわ、レシピの手順、最初から読んでくれ",
    "balloon": "もうええわ、レシピの手順、最初から読んでくれ",
    "face": "anger"
})

make("bob", {
        "line": "御意",
        "balloon": "御意",
        "face": "pleasant"
    })

make("bob", {
        "line": "" + c_word[3][0][1:] + "",
        "balloon": "" + c_word[3][0][1:] + "",
        "face": "neutral"
    })

make("mary", {
    "line": "ふむふむ、次は？",
    "balloon": "ふむふむ、次は？",
    "face": "idyllic"
})

make("bob", {
        "line": "" + c_word[3][1][1:] + "",
        "balloon": "" + c_word[3][1][1:] + "",
        "face": "neutral"
    })

make("mary", {
    "line": "なるほど、ほんで？",
    "balloon": "なるほど、ほんで？",
    "face": "idyllic"
})

make("bob", {
    "line": ""+text1+"",
    "balloon": ""+text1+"",
    "face": "neutral"
})
#ぼけ1
make("mary", {
    "line": "おいおい、"+word+"じゃなくて"+word2+"やろ",
    "balloon": "おいおい、"+word+"じゃなくて"+word2+"やろ",
    "face": "anger"
})

make("bob", {
    "line": "お、うっかりしてもう太郎",
    "balloon": "お、うっかりしてもう太郎",
    "face": "surprise"
})

make(
    "mary", {
        "line": "ちゃんと説明もできへんのかいな、最近の人工知能は衰えたなー",
        "balloon": "ちゃんと説明もできへんのかいな、最近の人工知能は衰えたなー",
        "face": "sad"
    })
#-------------------------------------------------------------
#料理2
make("bob", {
    "line": "ちなみに、あいちゃんが好きな食べ物は何？",
    "balloon": "ちなみに、あいちゃんが好きな食べ物は何？",
    "face": "happy"
})

make("mary", {
    "line": "そうやなー、特にないなー。",
    "balloon": "そうやなー、特にないなー。",
    "face": "idyllic"
})

make("mary", {
    "line": "本日のおすすめの料理はなんや？",
    "balloon": "本日のおすすめの料理はなんや？",
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
    "line": "美味しそうやなー",
    "balloon": "美味しそうやなー",
    "face": "idyllic"
})

make("mary", {
    "line": "作り方は？",
    "balloon": "作り方は？",
    "face": "idyllic"
})

make("bob", {
    "line": "えーと，まずは"+c_new[4],
    "balloon": "えーと，まずは"+c_new[4],
    "face": "neutral"
})

make("bob", {
    "line": "完成です。",
    "balloon": "完成です。",
    "face": "happy"
})

make("mary", {
        "line": "そんな簡単に作れるわけないやろ。",
        "balloon": "そんな簡単に作れるわけないやろ。",
        "face": "anger"
    })

make("mary", {
        "line": "アドバイスはええから、ちゃんとよめや、ポンコツ太郎!",
        "balloon": "アドバイスはええから、ちゃんとよめや、ポンコツ太郎!",
        "face": "anger"
    })

make("bob", {
    "line": "失礼、" + c_new[3][0][1:],
    "balloon": "失礼、" + c_new[3][0][1:],
    "face": "neutral"
})

make("mary", {
    "line": "ほんで？",
    "balloon": "ほんで？",
    "face": "idyllic"
})

make("bob", {
    "line": c_new[3][1][1:],
    "balloon": c_new[3][1][1:],
    "face": "neutral"
})

make("mary", {
    "line": "ふむふむ、次は？",
    "balloon": "ふむふむ、次は？",
    "face": "idyllic"
})
#ボケ2
make("bob", {
    "line": "『"+text_ro.replace("▁", "")[1:]+"』",
    "balloon": "『"+text_ro.replace("▁", "")[1:]+"』",
    "face": "neutral"
})

make("mary", {
    "line": "何言ってるねん、頭おかしなったか。",
    "balloon": "何言ってるねん、頭おかしなったか。",
    "face": "anger"
})

make("bob", {
    "line": "おっと，読み間違えたわわわわ",
    "balloon": "おっと，読み間違えたわわわわ",
    "face": "surprise"
})

make("bob", {
    "line": "正しくは『"+c_new[3][2][1:]+"』、でした。",
    "balloon": "正しくは『"+c_new[3][2][1:]+"』、でした。",
    "face": "happy"
})

make("mary", {
    "line": "いい加減にしろよ",
    "balloon": "いい加減にしろよ",
    "face": "anger"
})

make("mary", {
    "line": "ペッパー君の方が優秀やぞ",
    "balloon": "ペッパー君の方が優秀やぞ",
    "face": "anger"
})

make("bob", {
    "line": "おい、ペッパーよりは優秀や",
    "balloon": "おい、ペッパーよりは優秀や",
    "face": "anger"
})

#--------------------------------------------------------------
#オチ

make("mary", {
    "line": "もうええわ",
    "balloon": "もうええわ",
    "face": "anger"
})

make("bob", {
    "line": "最後に挽回するチャンスをください。",
    "balloon": "最後に挽回するチャンスをください。",
    "face": "pleasant"
})

make(
    "mary", {
        "line": "ペッパー君、より優秀なら、"+c_new[0]+"の作り方を簡単に要約してや",
        "balloon": "ペッパー君より優秀なら、"+c_new[0]+"の作り方を簡単に要約してや",
        "face": "pity"
    })

#(レシピのうち材料の名前を単語区切りに読む)

make("bob", {
    "line": "朝飯前や",
    "balloon": "朝飯前や",
    "face": "pleasant"
})

make("bob", {
    "line": ""+c_new[1]+"や、どうや",
    "balloon": ""+c_new[1]+"や、どうや",
    "face": "pleasant"
})

make("mary", {
    "line": "もうええわ、どうもありがとうございました。",
    "balloon": "もうええわ、どうもありがとうございました。",
    "face": "neutral"
})

make("bob", {
    "line": "どうも、グノーシスしゅぎしゃ、ゴンザレスいや。",
    "balloon": "どうも、グノーシス主義者、ゴンザレスいや。",
    "face": "happy"
})

make("bob", {
    "line": "ごんたでした。",
    "balloon": "ゴン太でした。",
    "face": "happy"
})

##########################################
#               漫才台本出力
##########################################
MakeLine.makeScript(OUTPUT_FILE_PATH)
print("完了")
