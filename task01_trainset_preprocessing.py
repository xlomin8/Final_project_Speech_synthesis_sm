import json
import pandas as pd


# 1. 파일 1개
# 1-1. 경로 설정
path = './1.학습레이블.json'


# 1-2. json파일 읽기
with open(path, 'r', encoding='UTF8') as f:
    json_data = json.load(f)

print(json_data)
print(len(json_data))


# 1-3. id 추출
ids = []
for i in range(33401):
    id = json_data[i]['id']
    ids.append(id)

print('id list : ', ids)


# 1-4. text 추출
texts = []
for i in range(33401):
  value = json_data[i]
  sentence = value['sentences'][0]
  text=sentence['origin_text']
  # print(text)
  texts.append(text)


# 1-5. dataframe으로 변환
df = pd.DataFrame(zip(ids, texts), columns=['id', 'text'])
df['id'].sort_values(ascending=True)
print(df)


# 1-6. 저장
df.to_csv('./training_label.csv')


# 1-7. txt파일로 만들기
df = pd.read_csv('./happy.csv')
# print(len(df))


f = open('D:/감성발화/train/heartbroken.txt', 'w', encoding='utf-8')
for i in range(0,33401):
  f.write('wavs/'+df['id'][i]+'.wav'+'|'+df['text'][i]+'\n')

f = open('D:/감성발화/train/heartbroken.txt', 'a', encoding='utf-8')
for i in range(60001,66907):
  f.write('wavs/'+df['file'][i]+'wav'+'|'+df['text'][i])+'\n')




# 2. 폴더 속 여러 파일 한번에 읽기
import json
import pandas as pd
import os


# 2-1. 경로 설정
path = '라벨링데이터/7.중립/0046_G2A3E7S0C0_SSH/'
file_list = os.listdir(path)


# 2-2.  json파일만 리스트에 넣기
file_list_py = [file for file in file_list if file.endswith('.json')]


# 2-3. 데이터프레임으로 변환
dict_list = []
for i in file_list_py:
    for line in open((path+i),"r", encoding='utf-8'):
      try:
        dict_list.append(json.loads(line))
      except:
        pass
df = pd.DataFrame(dict_list)


# 2-4. 파일정보, 전사정보만 추출
df1 = df[['파일정보', '전사정보']]
print(df1)


files = []
for i in range(len(df1['파일정보'])):
  file = list(df['파일정보'][i].values())[1]
  files.append(file)


texts = []
for i in range(len(df1['전사정보'])):
  text = list(df['전사정보'][i].values())[0]
  texts.append(text)


df2 = pd.DataFrame({'file':files, 'text':texts})
print(df2)


# 2-5. 저장
df2.to_csv('./crawled_data/{}.csv'.format(path.split('/')[-2]))


# 3. 2번 과정 거친 파일 concat
import glob


# 3-1. 경로 설정
data_path = glob.glob('./crawled_data/*')
# print(data_path)


# 3-2. concat
df = pd.DataFrame()
for path in data_path[0:]:
    df_temp = pd.read_csv(path)
    df = pd.concat([df, df_temp])


# 3-3. csv파일로 저장
df.to_csv('./neutral.csv', index=False)


# 4. txt파일로 만들기
df = pd.read_csv('./panicked.csv')
# print(len(df))
# exit()


# 4-1. 텍스트 파일 쓰기
# f = open('D:/감성발화/train/happy.txt', 'w', encoding='utf-8')
f = open('C:/Users/ASIA-21/Desktop/mimic-recording-studio/audio_files/panicked.txt', 'w', encoding='utf-8')
for i in range(len(df)):
  f.write(df['file'][i]+'|'+df['text'][i]+'\n')
f.close()
#
# # # 4-2. 기존내용에 추가
# # f = open('D:/감성발화/train/heartbroken.txt', 'a', encoding='utf-8')
# # for i in range(15001, 30001):
# #   f.write('wavs/'+df['file'][i]+'|'+df['text'][i]+'\n')
# # f.close()
