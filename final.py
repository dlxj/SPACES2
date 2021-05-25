
import numpy as np
import extract_convert as convert
import extract_vectorize as vectorize
import extract_model as extract
import seq2seq_model as seq2seq
from snippets import *

if len(sys.argv) == 1:
    fold = 0
else:
    fold = int(sys.argv[1])


def predict(text, topk=3):
    # 抽取
    texts = convert.text_split(text)
    vecs = vectorize.predict(texts)
    preds = extract.model.predict(vecs[None])[0, :, 0]
    preds = np.where(preds > extract.threshold)[0]
    summary = ''.join([texts[i] for i in preds])
    # 生成
    summary = seq2seq.autosummary.generate(summary, topk=topk)
    # 返回
    return summary


import numpy as np
epochs = 1024
model.load_weights('weights/seq2seq_model.%s.weights' % (epochs - 1))

def predict(text, topk=3):
    # 抽取
    texts = text_split(text) # convert.
    vecs = vectorize_predict(texts)
    preds = extract_model.predict(vecs[None])[0, :, 0]
    preds = np.where(preds > threshold)[0]
    summary = ''.join([texts[i] for i in preds])
    # 生成
    summary = autosummary.generate(summary, topk=topk)
    # 返回
    return summary


import json
import decimal
import datetime
import pandas as pd

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json 
def JsonParse(s):
    return json.loads(s, strict=False )

# convert dict to string
def JsonString(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)


dic_text = {}

datas = []

with open('./SPACES/datasets/valid.json', 'r', encoding='utf-8') as fp:
  text = fp.read()
  text = text.strip()
  textss = text.split('\n')

  n = 0
  for s in textss:
    data = json.loads(s, strict=False )
    texts = data['text']

    tmp = []
    for d in texts:
      tmp.append( d['sentence'] )

    tmptext = "\n".join(tmp)

    #if text in dic_text:
    #  continue
    #else:
    #  dic_text[text] = True

    #print(text)
    machine_summary = predict(tmptext, topk=3)
    #print(summary)
    #print('#############################################\n\n\n\n\n')

    data['machine_summary'] = machine_summary
    data['booktext'] = tmptext

    datas.append(data)
    # print(text)
    
    n += 1
    
    print( f"{n}/{len(textss)}" )
    
    #if n >= 3:
    #  break


tmp = []
for d in datas:
  tmp.append( [ d['booktext'], d['summary'], d['machine_summary'] ] )
  #tmp.append( [ d['full_name_path'], d['booktext'], d['summary'], d['machine_summary'] ] )

#csv = pd.DataFrame(tmp,columns=['目录','原文', '人工摘要', '机器摘要'])
csv = pd.DataFrame(tmp,columns=['原文', '人工摘要', '机器摘要'])
csv.to_csv('/content/summarys.csv', index=False ,encoding="utf-8")
csv.to_csv('/content/gdrive/MyDrive/summarys.csv', index=False ,encoding="utf-8")


#! -*- coding: utf-8 -*-
# 法研杯2020 司法摘要
# 最终模型：所有步骤串起来
# 使用方式：
# from final import *
# summary = predict(text, topk=3)
# print(summary)
# 科学空间：https://kexue.fm

# import numpy as np
# import extract_convert as convert
# import extract_vectorize as vectorize
# import extract_model as extract
# import seq2seq_model as seq2seq
# from snippets import *

# if len(sys.argv) == 1:
#     fold = 0
# else:
#     fold = int(sys.argv[1])


# def predict(text, topk=3):
#     # 抽取
#     texts = convert.text_split(text)
#     vecs = vectorize.predict(texts)
#     preds = extract.model.predict(vecs[None])[0, :, 0]
#     preds = np.where(preds > extract.threshold)[0]
#     summary = ''.join([texts[i] for i in preds])
#     # 生成
#     summary = seq2seq.autosummary.generate(summary, topk=topk)
#     # 返回
#     return summary


# if __name__ == '__main__':

#     from tqdm import tqdm
#     import pandas as pd
#     tmp = []

#     for i in range(num_folds): # num_folds
#         fold = i

#         data = extract.load_data(extract.data_extract_json)
#         valid_data = data_split(data, fold, num_folds, 'valid')
#         total_metrics = {k: 0.0 for k in metric_keys}
#         for d in tqdm(valid_data):
#             text = '\n'.join(d[0])
#             summary = predict(text)

#             tmp.append([text, summary])

#             metrics = compute_metrics(summary, d[2])
#             for k, v in metrics.items():
#                 total_metrics[k] += v

#     csv = pd.DataFrame(tmp,columns=['文本','摘要'])
#     csv.to_csv('/content/summarys.csv', index=False ,encoding="utf-8")
#     csv.to_csv('/content/gdrive/MyDrive/summarys.csv', index=False ,encoding="utf-8")
    
#     metrics = {k: v / len(valid_data) for k, v in total_metrics.items()}
#     print(metrics)
