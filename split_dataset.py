
import os,math

import json
import decimal
import datetime

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

if __name__ == "__main__":

    currDir = os.path.dirname(os.path.abspath(__file__))

    fname_train_origin = os.path.join(currDir, 'datasets', 'train_origin.json')

    fname_train = os.path.join(currDir, 'datasets', 'train.json')
    fname_valid = os.path.join(currDir, 'datasets', 'valid.json')

    with open(fname_train_origin, 'r', encoding='utf-8') as fp:
        train_origin = fp.read()
        train_origin = train_origin.strip()
        train_origins = train_origin.split('\n')
        
        total = len(train_origins)
        m = math.ceil( total * 0.98 )

        trainsets = train_origins[ : m]
        trainsets = trainsets[:1000] # 转换数据实在是太久了，弄小点
        validsets = train_origins[m :]
        validsets = validsets[:50]

        trainsets = "\n".join(trainsets)
        validsets = "\n".join(validsets)

        with open(fname_train, 'w', encoding='utf-8') as fp:
            fp.write(trainsets)

        with open(fname_valid, 'w', encoding='utf-8') as fp:
            fp.write(validsets)


