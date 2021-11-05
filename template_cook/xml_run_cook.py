import convXML as MakeLine
import cookpad_date

c = cookpad_date.html()
#c = ["タイトル", "要約", "材料", "手順(作り方)" ,"アドバイス", "歴史"]
for i in c[3]:
    print("手順"+i)

print(c[2])
l= c[2].split(" ")
print(l)

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

make("mary", {
    "line": "どーも、あいちゃんです",
    "balloon": "どーも、あいちゃんです"
})

make("bob", {
    "line": "どーも、ゴンタです",
    "balloon": "どーも、ゴン太です"
})

# volume, pitch, speed調整
"""
volume:声量，pitch:声の高さ，speed:声の速さ
を設定できる．
また，複数指定もできる．
100%が標準．
"""

make("bob", {
    "line": "こっそり喋ります",
    "balloon": "こっそり喋ります(20%)"
},
    {"line": {
        "volume": "20%",
    }}
)

make("bob", {
    "line": "ああああああ",
    "balloon": "無音にもできます(0%)"
},
    {"line": {
        "volume": "0%",
    }}
)

make("mary", {
    "line": "ピッチを高くしています",
    "balloon": "ピッチを高くしています(150%)"
},
    {"line": {
        "pitch": "150%",
    }}
)

make("bob", {
    "line": "超早口で喋ってもええんやないやろか",
    "balloon": "超早口で喋ってもええんやないやろか(150%)"
},
    {"line": {
        "speed": "150%",
    }}
)

make("mary", {
    "line": "だめ",
    "balloon": "だめ(20%)"
},
    {"line": {
        "speed": "20%",
    }}
)

make("bob", {
    "line": "ピッチを高く，スピードを早く，ボリュームを控えめに喋っています",
    "balloon": "ピッチを高く(130%)，スピードを早く(130%)，ボリュームを控えめ(80%)に喋っています"
},
    {"line": {
        "pitch": "130%",
        "speed": "130%",
        "volume": "80%",
    }}
)

##########################################
#               漫才台本出力
##########################################
MakeLine.makeScript(OUTPUT_FILE_PATH)
