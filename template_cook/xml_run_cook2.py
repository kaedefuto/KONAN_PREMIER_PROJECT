import convXML as MakeLine
import xml.etree.ElementTree as ET
from xml.dom import minidom
import queue


# 出力ファイルパス
OUTPUT_FILE_PATH = "./output_test.xml"


def ToMinidom(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    return minidom.parseString(rough_string)


def Fairing(rootN):
    R = ToMinidom(rootN).toprettyxml(indent="\t", newl="\n", encoding="UTF-8")
    # R=R.replaceex("?>","?>"+XSL,1)
    return R


ret = []


def make(name, line):
    global ret
    ret.append(MakeLine.Make(name, line))


# 初期化
MakeLine.Reset()
ret.append(MakeLine.Refresh())

##########################################
#               漫才台本部分
##########################################

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
    "line": "**です。",
    "balloon": "肉じゃが（ソースを入れない和食）です。",
    "face": "like"
})

make("bob", {
    "line": "**はママのあじー",
    "balloon": "肉じゃがはママのあじー",
    "face": "happy"
})

make("mary", {
    "line": "おかあさん以外も作るし字余りなんよ。",
    "balloon": "お母さん以外も作るし、字余りなんよ。",
    "face": "pity"
})

make("mary", {
    "line": "ところで、**ってどうやって作るっけ",
    "balloon": "ところで、肉じゃがってどうやって作るっけ",
    "face": "shame"
})

make("bob", {
    "line": "(**のレシピを途中まで読む)",
    "balloon": "(肉じゃがのレシピを途中まで読む)",
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
    "line": "(**のレシピを2,3行読む)",
    "balloon": "(肉じゃがのレシピを2,3行読む)",
    "face": "idyllic"
})

make("mary", {
    "line": "しゃくを取りすぎるからみじかくできる？",
    "balloon": "尺を取りすぎるから短く出来る？",
    "face": "disagreeable"
})

make("bob", {
    "line": "(**のレシピのうち材料の名前を単語区切りに読む)",
    "balloon": "(肉じゃがのレシピのうち材料の名前を単語区切りに読む)",
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
