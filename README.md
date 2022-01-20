# KONAN_PREMIER_PROJECT

2021年度ハッカソン用リポジトリ

チャットアプリケーション生成プログラム

## 漫才台本自動生成用プログラム  

## template
xml_run.py  
- 漫才台本を作成するプログラム  

convXML.py 
- xmlファイルを作成するためのプログラム

## template_cook
xml_run_cook_new.py  
- 料理漫才の台本を作成するプログラム  

cookpad_date.py  
- クックパッドのサイトからスクレイピングするプログラム 

convXML.py 
- xmlファイルを作成するためのプログラム

## template_news

- ニュース漫才の台本を作成するプログラム（今回は使わない）

## 実行方法

```
python xml_run.py
```

```
python xml_run_cook_new.py
```

- 漫才台本(xml)が生成される

## URL
- http://www.nadasemi.jp/robot_manzai/chatapplication_hackathon_3/

## ボケ
- RoBERTaのMASKによるボケの生成
- word2vecによるボケの生成

## 参考記事

word2vec  
https://qiita.com/kenta1984/items/93b64768494f971edf86

事前学習済みモデル  
http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/
