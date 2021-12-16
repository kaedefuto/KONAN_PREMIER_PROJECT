import convXML as MakeLine
import cookpad_date
import boke.Roberta
import boke.wiki as wiki
import datetime
import random


dt_now = datetime.datetime.now()
day=dt_now.strftime('%m%d')

day_old=str(int(day)-1)

with open("./food/foodname.txt", "r", encoding="utf-8") as f:
    l = f.readlines()
    text = random.choice(l)
    cook_word = text.replace("\n", "")
    #print(text.replace("\n",""))

c_new= cookpad_date.html(day)
#c_old= cookpad_date.html(day_old)
c_word = cookpad_date.html_word(cook_word)
print(c_new)
#c_word2 = cookpad_date.html_word("天津飯")
#print(c_word[2].replace("   ","，"))

#c = ["タイトル", "要約", "材料", "手順(作り方)" ,"アドバイス", "歴史"]
#print(c_new[3][0])




# 出力ファイルパス
OUTPUT_FILE_PATH = "./volume_test.xml"


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
    "line": "ところで、"+cook_word+"ってどうやって作るっけ",
    "balloon": "ところで、"+cook_word+"ってどうやって作るっけ",
    "face": "shame"
})

make(
    "bob", {
        "line": "楽勝や，人工知能で調べたるわ",
        "balloon": "楽勝や，人工知能で調べたるわ",
        "face": "idyllic"
    })

make("mary", {
    "line": "さすがゴンザレス",
    "balloon": "さすがゴンザレス",
    "face": "shame"
})

make("bob", {
    "line": "料理名は"+c_word[0]+"だよ",
    "balloon": "料理名は"+c_word[0]+"だよ",
    "face": "idyllic"
})

make(
    "bob", {
        "line": "材料は"+c_word[2].replace("   ","，")+"です",
        "balloon": "材料は"+c_word[2].replace("   ","，")+"です",
        "face": "idyllic"
})

make("mary", {
    "line": "長いなー",
    "balloon": "長いなー",
    "face": "idyllic"
})


make("bob", {
    "line": "えーと，まず，"+c_word[2].replace("   ", "，").split("，")[0].replace(" ","")+"を作ります",
    "balloon": "えーと，まず，"+c_word[2].replace("   ", "，").split("，")[0].replace(" ","")+"を作ります",
    "face": "idyllic"
})

make("mary", {
    "line": "ちょっと待て，どんだけかかるねん",
    "balloon": "ちょっと待て，どんだけかかるねん",
    "face": "idyllic"
})

make("bob", {
    "line": "5年くらいかかりますわ",
    "balloon": "5年くらいかかりますわ",
    "face": "idyllic"
})

make("mary", {
    "line": "生産者になりたいわけじゃないねん",
    "balloon": "生産者になりたいわけじゃないねん",
    "face": "idyllic"
})

make("mary", {
    "line": "料理の手順を教えてくれよ",
    "balloon": "料理の手順を教えてくれよ",
    "face": "idyllic"
})
make(
    "bob", {
        "line": "まず，" + wiki.wiki_content(cook_word).split("。")[0] + "",
        "balloon": "まず，" + wiki.wiki_content(cook_word).split("。")[0] + "",
        "face": "idyllic"
    })


make("mary", {
    "line": "ちょっとまって、その情報のソースは",
    "balloon": "ちょっとまって、その情報のソースは？",
    "face": "disagreeable"
})

make("bob", {
    "line": wiki.wiki_url(cook_word),
    "balloon": wiki.wiki_url(cook_word),
    "face": "idyllic"
})

make("mary", {
    "line": "いや、urlじゃわからんのよ。今見ているじょうほうげんを聞いとるねん",
    "balloon": "いや、urlじゃわからんのよ。今見ている情報源を聞いとるねん",
    "face": "angry"
})

make(
    "bob", {
        "line": "我らが大先生、wikipediaに決まってます",
        "balloon": "我らが大先生、wikipediaに決まってます",
        "face": "disagreeable"
    })

make("mary", {
    "line": "嘘情報も多いし，大先生ではないんよ",
    "balloon": "嘘情報も多いし，大先生ではないんよ",
    "face": "disagreeable"
})

make("mary", {
    "line": "もうええわ、レシピ、最初から、よめ",
    "balloon": "もうええわ、レシピ、最初から、よめ",
    "face": "idyllic"
})

make("bob", {
    "line": ""+c_word[3][0]+"",
    "balloon": ""+c_word[3][0]+"",
    "face": "idyllic"
})

make("mary", {
    "line": "ふむふむ、次は",
    "balloon": "ふむふむ、次は",
    "face": "idyllic"
})

make("bob", {
    "line": ""+c_word[3][1]+"",
    "balloon": ""+c_word[3][1]+"",
    "face": "idyllic"
})
#ぼけ1
make("mary", {
    "line": "おいおい、"+c_word[0]+"に"+c_word[0]+"は入れんやろ",
    "balloon": "おいおい、"+c_word[0]+"に"+c_word[0]+"は入れんやろ",
    "face": "idyllic"
})

make("bob", {
    "line": "",
    "balloon": "",
    "face": "idyllic"
})

#-------------------------------------------------------------
#料理2
make("bob", {
    "line": "あいちゃんが好きな食べ物は何?",
    "balloon": "あいちゃんが好きな食べ物は何?",
    "face": "happy"
})

make("mary", {
    "line": "私は何でもかんでもいけるわ、本日のおすすめの料理は",
    "balloon": "私は何でもかんでもいけるわ、本日のおすすめの料理は",
    "face": "idyllic"
})

make("bob", {
    "line": "ゴンザレスが調べたるわ",
    "balloon": "ゴンザレスが調べたるわ",
    "face": "happy"
})

make("bob", {
    "line": "本日のオヌヌメ料理は"+c_new[0]+"です",
    "balloon": "本日のオヌヌメ料理は"+c_new[0]+"です",
    "face": "happy"
})

make("mary", {
    "line": "美味しそうやなー，作り方は？",
    "balloon": "美味しそうやなー，作り方は？",
    "face": "idyllic"
})

make("bob", {
    "line": "えーと，まずは"+c_new[5],
    "balloon": "えーと，まずは"+c_new[5],
    "face": "happy"
})

make("mary", {
    "line": "それって、あなたの感想ですよね",
    "balloon": "それって、あなたの感想ですよね",
    "face": "idyllic"
})

make("bob", {
    "line": "そうですけど、何か問題でもありますか",
    "balloon": "そうですけど、何か問題でもありますか",
    "face": "happy"
})

make("mary", {
    "line": "開き直るなや、料理の作り方を読めや",
    "balloon": "開き直るなや、料理の作り方を読めや",
    "face": "idyllic"
})

make("bob", {
    "line": "ういー、えーっと"+c_new[4],
    "balloon": "ういー、えーっと"+c_new[4],
    "face": "happy"
})

make("mary", {
    "line": "それって、あなたのコツですよね",
    "balloon": "それって、あなたのコツですよね",
    "face": "idyllic"
})

make("bob", {
    "line": "そのツッコミはもうええわ、ロボットにも間違いはあるねん",
    "balloon": "そのツッコミはもうええわ、ロボットにも間違いはあるねん",
    "face": "happy"
})

make("mary", {
    "line": "ほな、続きよめや",
    "balloon": "ほな、続きよめや",
    "face": "idyllic"
})

make("bob", {
    "line": ""+c_new[3][0],
    "balloon": ""+c_new[3][0],
    "face": "happy"
})

make("mary", {
    "line": "次、",
    "balloon": "次、",
    "face": "idyllic"
})

make("bob", {
    "line": ""+c_new[3][1],
    "balloon": ""+c_new[3][1],
    "face": "happy"
})

make("mary", {
    "line": "次、次、次----",
    "balloon": "次、次、次----",
    "face": "idyllic"
})
#ボケ2
make("bob", {
    "line": ""+c_new[3][1],
    "balloon": ""+c_new[3][1],
    "face": "happy"
})

make("mary", {
    "line": "なんでやんん",
    "balloon": "何でやねん",
    "face": "idyllic"
})

#--------------------------------------------------------------
#オチ

make("mary", {
    "line": "もうええわ、作り方なんもわからんから最後に簡単に説明してや",
    "balloon": "もうええわ、作り方なんもわからんから最後に簡単に説明してや",
    "face": "idyllic"
})

#(レシピのうち材料の名前を単語区切りに読む)
make("bob", {
    "line": ""+c_new[1]+"や、どうや",
    "balloon": ""+c_new[1]+"や、どうや",
    "face": "idyllic"
})

make("mary", {
    "line": "しょうりゃくしすぎやろ",
    "balloon": "省略しすぎやろ",
    "face": "disagreeable"
})

make("mary", {
    "line": "しかもそれなんかキャッチコピーみたいやん、なんかもうつかれたわ　どうもありがとうございました。",
    "balloon": "しかもそれなんかキャッチコピーみたいやん、なんかもうつかれたわ　どうもありがとうございました。",
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
