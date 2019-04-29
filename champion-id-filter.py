import json
from pprint import pprint
import os

championFile = []

for root, dirs, files in os.walk("../champion_data/ko_KR/champion"):
  championFile = [root + '/' + file  for file in files]

output = open("champion-id-map.txt", 'w')

for file in championFile:
  f = open(file, encoding='utf-8')

  data = json.load(f)

  championName = file.split('/')[-1][:-5]
  # print(championName)

  # print(data["data"][championName]["id"], data["data"][championName]["key"])
  output.write(data["data"][championName]["id"] + ',' + \
               data["data"][championName]["key"] + '\n')

  f.close()

output.close()
