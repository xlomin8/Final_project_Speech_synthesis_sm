import json
import pandas as pd



# 경로 설정
path = './1.학습레이블.json'


# json파일 읽기
with open(path, 'r', encoding='UTF8') as f:
    json_data = json.load(f)

print(json_data)
print(len(json_data))
exit()


# id 추출
ids = []
for i in range(33401):
    id = json_data[i]['id']
    ids.append(id)

print('id list : ', ids)


# text 추출
texts = []
for i in range(33401):
  value = json_data[i]
  sentence = value['sentences'][0]
  text=sentence['origin_text']
  print(text)
  texts.append(text)


# dataframe으로 변환
df = pd.DataFrame(zip(ids, texts), columns=['id', 'text'])

df


# 저장
df.to_csv('./training_label.csv')


# txt파일로 만들기
df = pd.read_csv('./training_label.csv')

# for i in range(0,33401):
#   print('wavs/'+df['id'][i]+'.wav'+'|'+df['text'][i])

for i in range(0,15458):
  print('wavs/'+df['id'][i]+'.wav'+'|'+df['text'][i])