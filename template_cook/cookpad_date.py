# -*- coding: utf-8 -*-
#BeautifulSoupとutllibをインポート
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
#コマンドライン引数指定 (1つのみ)
import sys
import csv
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import datetime
dt_now = datetime.datetime.now()
day=dt_now.strftime('%m%d')


links = [] #ページにあるリンク10個*5ページを格納する
maintexts = [] #txtファイルに書き込む文章
nextlink = []
#html抽出関数
def htmlExtraction(url):
    # HTML を取得
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    html = opener.open(url)
    soup = BeautifulSoup(html,"html.parser")

    for url in soup.find_all("div",{"class":"text"}):
        try:
            links.extend([url.a.get("href")])
            nextlink.extend([soup.find("div",{"class":"next"}).a.get("href")])
        except:
            import traceback
            traceback.print_exc()

def html():
    querytxt = "ピックアップ" + " " + day#txtファイル名
    #querytxt = "ピックアップ" + " " + str(sys.argv[1]) #txtファイル名

    #https://cookpad.com/pickup_recipes?date=1030
    url1 = 'https://cookpad.com/'
    #nextlink.extend(["pickup_recipes?date=" + sys.argv[1].zfill(4)])
    nextlink.extend(["pickup_recipes?date=" + day.zfill(4)])
    for i in range(1):
        url = url1 + nextlink[i]
        #print("Date = " + str(i+1))
        htmlExtraction(url)

    cnt = 0
    #本文抽出
    #print(links[0])
    links2=[]
    links2.append(links[0])
    for link in links2:
        cnt += 1

        try:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            html = opener.open("https://cookpad.com" + link)
            soup = BeautifulSoup(html, "html.parser")

            ##########################################################################
            title = (soup.find("h1",{"class":"recipe-title fn clearfix"}).get_text()).replace("\n","")  #タイトル
            summary = (soup.find("div",{"class":"description_text"}).get_text()).replace("\n","")#.splitlines()  #要約
            material = (soup.find("div",{"id":"ingredients_list"}).get_text()).replace("\n"," ")#.splitlines()
            method = []
            for dl in soup.find_all("dl"):
                #print(str(dl.get_text()).replace("\n", ""))
                method.append(str(dl.get_text()).replace("\n", ""))
            advice = (soup.find("div",{"id":"advice"}).get_text()).replace("\n","")#.splitlines() #ワンポイントアドバイス
            history = (soup.find("div",{"id":"history"}).get_text()).replace("\n","")#.splitlines()
            ##########################################################################

            maintexts.append(title)
            maintexts.append(summary)
            maintexts.append(material)
            maintexts.append(method)
            maintexts.append(advice)
            maintexts.append(history)

            #print(maintexts[3][1])
            #columns = ["タイトル", "要約", "材料", "方法" ,"アドバイス", "歴史"]
            #df = pd.DataFrame(maintexts)
            #print(df[0][3])
            #print(df[0][1])
        except:
            import traceback
            traceback.print_exc()
    return maintexts

def main():
    l=html()
    print(l)


if __name__ == "__main__":
    main()
    print("完了")
