def roberta(text, masked_idx=5):
    from transformers import T5Tokenizer, RobertaForMaskedLM
    import MeCab
    token_list =[]

    tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-roberta-base")
    tokenizer.do_lower_case = True  # due to some bug of tokenizer config loading

    model = RobertaForMaskedLM.from_pretrained("rinna/japanese-roberta-base")

    # original text
    #text = "4年に1度オリンピックは開かれる。"

    # prepend [CLS]
    text = "[CLS]" + text

    # tokenize
    tokens = tokenizer.tokenize(text)
    #print(len(tokens))
    #print(tokens)  # output: ['[CLS]', '▁4', '年に', '1', '度', 'オリンピック', 'は', '開かれる', '。']
    tokens1=list()
    for i in tokens:
        tokens1.append(i)

    # mask a token
    #masked_idx = 5
    for i in range(masked_idx,len(tokens),5):
        tokens[i] = tokenizer.mask_token
        #tokens[i+1] = tokenizer.mask_token
    #print(tokens)  # output: ['[CLS]', '▁4', '年に', '1', '度', '[MASK]', 'は', '開かれる', '。']

    # convert to ids
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    #print(token_ids)  # output: [4, 1602, 44, 24, 368, 6, 11, 21583, 8]

    # convert to tensor
    import torch
    token_tensor = torch.LongTensor([token_ids])

    # provide position ids explicitly
    position_ids = list(range(0, token_tensor.size(1)))
    #print(position_ids)  # output: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    position_id_tensor = torch.LongTensor([position_ids])

    # get the top 10 predictions of the masked token
    with torch.no_grad():
        outputs = model(input_ids=token_tensor, position_ids=position_id_tensor)
        predictions = outputs[0][0, masked_idx].topk(10)

    for i, index_t in enumerate(predictions.indices):
        index = index_t.item()
        token = tokenizer.convert_ids_to_tokens([index])[0]
        token_list.append(tokenizer.convert_ids_to_tokens([index])[0])
        #print(i, token)

    #変換前文書
    #print(tokens)#[MASK]
    l1=""
    for i in range(1,len(tokens)):
        if tokens[i] =="[MASK]":
            l1+="「"+tokens1[i]+"」"
        else:
            l1+=tokens[i]
    
    #変換後文書
    l2=""
    j=0
    for i in tokens[1:]:
        if i =="[MASK]":
            l2+="「"+token_list[j]+"」"
            j+=1
        else:
            l2+=i


    return l2,l1



def main():
    text = "4年に1度オリンピックは開かれる。"
    l ,i=roberta(text,5)
    print(l)


if __name__ == "__main__":
    main()
    print("完了")