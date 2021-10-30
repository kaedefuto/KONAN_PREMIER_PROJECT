import wikipedia
import MeCab

wikipedia.set_lang("ja") # 言語設定を日本語にする 

page_summary = wikipedia.page("漫才").summary # 要約文を取得
# print(page_summary)

mecab = MeCab.Tagger() # MeCabの設定
mecab_parse = mecab.parse(page_summary) # 要約文を形態素解析 
# print(mecab_parse) #中身を確認

mecab_parse_node = mecab.parseToNode(page_summary)

words = [] #形態素解析結果 
while mecab_parse_node:
    #形態素解析結果をリストに入れる
    words += [[mecab_parse_node.surface] + mecab_parse_node.feature.split(",")]
    mecab_parse_node = mecab_parse_node.next # 次のノード(単語)へ # print(words)
    for idx in words:
        if idx[1]=="名詞": #リストの2番目が名詞
            print(idx)
