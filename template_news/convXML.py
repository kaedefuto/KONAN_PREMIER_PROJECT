
"""
2021年度ハッカソン用
チャットアプリケーション生成プログラム
"""
import csv
import os
import xml.etree.ElementTree as ET
import re
import random
from logging import getLogger
logging = getLogger(__name__)

Escape = [
    # (re.compile(ur"\([^\)]*\)"),lambda x:u""),
    (re.compile(r"<([^>]*)>"), lambda x:x.group(1)),
    (re.compile(r"&"), lambda x:"＆")
]
Init = {
    "position": "audience",
    "face": "neutral"
}
Shake = ["little_l", "little_r"]
Audience = "audience"
Pose = {}


def Make(target, args={}, attrs={}, Reset=[]):
    """行を作成

:param target: 対象の名前
:param args: 作成するコマンド
:param attrs: 作成するコマンドに用いる引数
:param Reset: 位置を初期化する対象
:return: 作成されたコマンド(ElementTree型)
"""
    SetS = set()
    E = ET.Element("command")
    for k, v in list(args.items()):
        C = ET.SubElement(E, k)
        C.text = v
        C.set("target", target)
        SetS.add(k)
        if k in attrs:
            for ak, av in list(attrs[k].items()):
                C.set(ak, av)
    if ("line" in args) and ("balloon" not in args):
        C = ET.SubElement(E, "balloon")
        C.text = args["line"]
        C.set("target", target)
        SetS.add("balloon")
    if "line" in args:
        l = args["line"]
        for ptn, rep in Escape:
            n = 1
            while n > 0:
                l, n = ptn.subn(rep, l)
        args["line"] = l
    for r in Reset:
        # logging.debug("状態初期化 : {}".format(r))
        for k, v in list(Init.items()):
            if r == target and k in SetS:
                continue
            C = ET.SubElement(E, k)
            C.text = v
            C.set("target", r)
    if "position" not in args:
        if target not in Reset:
            if Pose[target] in Shake:
                C = ET.SubElement(E, "position")
                C.text = Audience
                C.set("target", target)
                Pose[target] = C.text
            elif Pose[target] == Audience:
                C = ET.SubElement(E, "position")
                C.text = random.choice(Shake)
                C.set("target", target)
                Pose[target] = C.text
    else:
        Pose[target] = args["position"]
    return E


def Refresh(Name=["mary", "bob"]):
    """初期化するためのコマンドを作成

:param Name: 対象の名前
:return: 作成されたコマンド(ElementTree型)
"""
    E = ET.Element("command")
    for r in Name:
        logging.debug("状態初期化 : {}".format(r))
        for k, v in list(Init.items()):
            C = ET.SubElement(E, k)
            C.text = v
            C.set("target", r)
    return E


def Template(item):
    """テンプレート行の作成

:param item: テンプレートの名前
:return: 作成されたコマンド(ElementTree型)
"""
    logging.debug("テンプレートの使用 : {}".format(item))
    T = ET.Element("template")
    T.text = "head"
    return T


def Reset():
    Pose["mary"] = "little_l"
    Pose["bob"] = "little_l"


def xmltemplatereader(Queue, filename, changedic=None):
    """
    xmlTemplateを読み込みセリフを生成
    Parameters
        Queue : queue
        filename : str 読み込むxmlテンプレートファイル
        changedi : Dict of str 置き換える文字列の辞書 ない場合テンプレートファイルそのまま読み込む
    Returns
        NoReturn Queueにつむだけ
    """
    root = ET.parse(filename).getroot()
    for command in root.findall("./script/command"):
        line = ""
        balloon = ""
        target = ""
        face = ""
        Data = {}
        line_Sub = {}
        for com in command.findall(".//"):
            if com.tag == "line":
                target = com.attrib["target"]
                if "pitch" in com.attrib:
                    line_Sub["pitch"] = com.attrib["pitch"]
                if "range" in com.attrib:
                    line_Sub["range"] = com.attrib["range"]
                line = com.text
                if changedic != None:
                    for k in changedic.keys():
                        if k in line:
                            line = line.replace(k, changedic[k])
                Data["line"] = line
            elif com.tag == "type":
                Data["type"] = com.text
            elif com.tag == "balloon":
                balloon = com.text
                if changedic != None:
                    for k in changedic.keys():
                        if k in balloon:
                            balloon = balloon.replace(k, changedic[k])
                Data["balloon"] = balloon
            elif com.tag == "face":
                face = com.text
                if changedic != None:
                    for k in changedic.keys():
                        if k in face:
                            face = face.replace(k, changedic[k])
                Data["face"] = face
            elif com.tag == "position":
                Data["position"] = com.text
        assert target != ""
        if len(line_Sub) != 0:
            E = MakeLine.Make(target, Data, {"line": line_Sub})
        else:
            E = MakeLine.Make(target, Data)
        Queue.put(E)


def splitXml(file_pass):
    """
    漫才チャットアプリケーション用に音声合成
    ！音声合成ファイルがないと動きません
    @param
        file_pass: 漫才台本XML
    """
    # ディレクトリの作成場所のパスの取得
    # dir = './'+tstr
    folder_name = file_pass.replace(".xml", "")
    made_pass = "./made/"
    target_pass = made_pass + folder_name

    # # ニュースタイトルディレクトリの作成
    # if os.path.isdir(target_pass) == False:
    #     os.makedirs(target_pass)
    # # xmlディレクトリの作成
    x_dir = target_pass+'/xml'
    # x_dir = "made"
    if os.path.isdir(x_dir) == False:
        os.makedirs(x_dir)
    # 発話内容の取得変数
    str_line = []
    str_balloon = []
    # Bob,Maryの取得変数
    str_target = []
    # Bob,Maryの表情情報
    str_face = []

    # ボリューム，ピッチ，スピード情報
    str_volume = []
    str_pitch = []
    str_speed = []

    # XMLファイル読み込み
    # tree = ET.parse(made_pass + file_pass)
    tree = ET.parse(file_pass)
    print("read xml")
    # XMLファイルルートの取得
    root = tree.getroot()

    # 表情情報の取得
    for face in root.findall(".//command"):
        if face.find(".//line") != None:
            if face.find(".//face") != None:
                str_face.append(face.find(".//face").text)
            else:
                str_face.append("neutral")

    # 発話表情情報の取得
    for voice in root.findall(".//command"):
        if voice.find(".//line") != None:
            # volume
            if voice.find(".//line").get("volume") != None:
                str_volume.append(voice.find(".//line").get("volume"))
            else:
                str_volume.append("100%")
            # pitch
            if voice.find(".//line").get("pitch") != None:
                str_pitch.append(voice.find(".//line").get("pitch"))
            else:
                str_pitch.append("100%")
            # speed
            if voice.find(".//line").get("speed") != None:
                str_speed.append(voice.find(".//line").get("speed"))
            else:
                str_speed.append("100%")

    # 発話、Bob、Maryの取得
    for balloon in root.findall(".//command"):
        if balloon.find(".//line") != None:
            str_line.append(balloon.find(".//line").text)
            if balloon.find(".//balloon") != None:
                str_balloon.append(balloon.find(".//balloon").text)
                str_target.append(balloon.find(".//balloon").get('target'))
            else:
                str_balloon.append(balloon.find(".//line").text)
                str_target.append(balloon.find(".//line").get('target'))

    # CSVファイル作成
    with open(target_pass + '/chat.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, lineterminator='\n')

        for i in range(len(str_line)):
            writer.writerow([str_target[i], str_balloon[i], str_face[i]])

    # XMLファイルの作成
    New_root = ET.Element("manzai")
    script = ET.SubElement(New_root, "script")
    command = ET.SubElement(script, "command")
    line = ET.SubElement(command, "line")

    for i in range(len(str_line)):
        line.text = str_line[i]

        # targetがBob,Maryを判別し属性を与える
        if str_target[i] == "bob":
            line.set('target', 'bob')
        else:
            line.set('target', 'mary')

        #volume, pitch and speed
        line.set("volume", str_volume[i])
        line.set("pitch", str_pitch[i])
        line.set("speed", str_speed[i])

        tree = ET.ElementTree(New_root)

        # 作成したディレクトリにXMLファイルを保存
        tree.write(x_dir + '/'+str(i)+'.xml', 'utf-8', True)

    # xmlからサウンドファイルも生成
    try:
        os.system("python Sound -aw " + x_dir)
    except:
        print("--sound warning--")
        pass
