# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib
import sys

# The input is the summonname-champname.csv
# EXPECTED FORMAT OF FILE:
# summoner name, champion name
# EXPECTED OUTPUT OF FILE:
# summoner name, champion name, win rate of champion of summoner('Never played in Rank' when not found)

file = open(sys.argv[1], encoding='utf-8')
lines = [line.strip().split(',') for line in file]
file.close()

def crawl_winrate(username, champname):
    url = 'https://www.op.gg/summoner/champions/userName=' + username
    req = requests.get(url)
    plain_text = req.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    champ_order = soup.select('td.ChampionName.Cell')
    rate_order = soup.select('td.RatioGraph.Cell')
    rate = ""
    exist = 0
    for i in range(len(champ_order)):
        champ_order[i] = str(champ_order[i])
        rate_order[i] = str(rate_order[i])
        if(champname in champ_order[i]):
            roidx = rate_order[i].index('data-value')
            if(rate_order[i][roidx + 12] == '0'):
                rate = '0'
            else:
                rate = rate_order[i][roidx + 12:roidx + 14]
            exist = 1
    if(exist == 0):
        rate = "Never played in Rank"
    return rate

output = open('sum-champ-winrate.csv', 'w', encoding='utf-8')

for line in lines:
    line.append(crawl_winrate(line[0], line[1]))
    output.write(','.join(line) + '\n')

output.close()


crawl_winrate('레피토스', 'Lucian')