import convXML as MakeLine
import cookpad_date

import datetime
dt_now = datetime.datetime.now()
day=dt_now.strftime('%m%d')

day_old=str(int(day)-1)

c_new= cookpad_date.html(day)
c_old= cookpad_date.html(day_old)
#c = ["タイトル", "要約", "材料", "手順(作り方)" ,"アドバイス", "歴史"]
print(c_new[3][0])
    


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
    "line": c_new[0]+"です。",
    "balloon": c_new[0]+"です。",
    "face": "like"
})

make("bob", {
    "line": c_new[0]+"はママのあじー",
    "balloon": c_new[0]+"はママのあじー",
    "face": "happy"
})

make("mary", {
    "line": "おかあさん以外も作るし字余りなんよ。",
    "balloon": "お母さん以外も作るし、字余りなんよ。",
    "face": "pity"
})

make("mary", {
    "line": "ところで、"+c_new[0]+"ってどうやって作るっけ",
    "balloon": "ところで、"+c_new[0]+"ってどうやって作るっけ",
    "face": "shame"
})

make("bob", {
    "line": "まず，"+c_new[3][0]+"",
    "balloon": "まず，"+c_new[3][0]+"",
    "face": "idyllic"
})

make("mary", {
    "line": "ちょっとまって、情報のソースは",
    "balloon": "ちょっとまって、情報のソースは？",
    "face": "disagreeable"
})

make("bob", {
    "line": "＋＋ソース",
    "balloon": "どろソース",
    "face": "idyllic"
})

make("mary", {
    "line": "いや、**に普通ソース入れへんやろ。今見ているじょうほうげんを聞いとるねん",
    "balloon": "いや、**に普通ソース入れへんやろ。今見ている情報源を聞いとるねん",
    "face": "angry"
})

make("bob", {
    "line": "オクシリンコス・パピルスに決まっています",
    "balloon": "オクシリンコス・パピルスにきまっています",
    "face": "disagreeable"
})

make("mary", {
    "line": "こだいエジプトにそんなもんあるわけないやん",
    "balloon": "古代エジプトにそんなもんあるわけないやん",
    "face": "disagreeable"
})

make("mary", {
    "line": "レシピ、つづき、よめ",
    "balloon": "レシピ、つづき、よめ",
    "face": "idyllic"
})

make("bob", {
    "line": ""+c_new[3][1]+"",
    "balloon": ""+c_new[3][1]+"",
    "face": "idyllic"
})

make("mary", {
    "line": "ふむふむ",
    "balloon": "ふむふむ",
    "face": "idyllic"
})

make("bob", {
    "line": ""+c_new[3][2]+"",
    "balloon": ""+c_new[3][2]+"",
    "face": "idyllic"
})

make("mary", {
    "line": "しゃくを取りすぎるからみじかくできる？",
    "balloon": "尺を取りすぎるから短く出来る？",
    "face": "disagreeable"
})

#(肉じゃがのレシピのうち材料の名前を単語区切りに読む)
make("bob", {
    "line": ""+c_new[2]+"",
    "balloon": ""+c_new[2]+"",
    "face": "idyllic"
})

make("mary", {
    "line": "しょうりゃくしすぎやろ",
    "balloon": "省略しすぎやろ",
    "face": "disagreeable"
})

make("bob", {
    "line": "それと、とかげのしっぽ、りゅうのなみだ、**",
    "balloon": "それと、とかげのしっぽ、りゅうのなみだ、**",
    "face": "idyllic"
})

make("mary", {
    "line": "**作るのに**いるのかよ、一生できへんやん。",
    "balloon": "**作るのに**いるのかよ、一生できへんやん。",
    "face": "relief"
})
make("mary", {
    "line": "しかも材料てきにくろまじゅつかよ、なんかもうつかれたわ　どうもありがとうございました。",
    "balloon": "しかも材料的に黒魔術かよ、なんかもうつかれたわ　どうもありがとうございました。",
    "face": "relief"
})

make("bob", {
    "line": "どうも、グノーシスしゅぎしゃ、ごんたでした。",
    "balloon": "どうも、グノーシス主義者、ゴン太でした。",
    "face": "happy"
})

##########################################
#               漫才台本出力
##########################################
MakeLine.makeScript(OUTPUT_FILE_PATH)
