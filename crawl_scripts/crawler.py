import requests
from bs4 import BeautifulSoup
import urllib
import os

def crawl_list():
    url = 'https://www.op.gg/champion/statistics'
    req = requests.get(url)
    plain_text = req.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    temp = [0] * 144
    champ_name = [0] * 144
#     champ_link = [0] * 143
    for i in range(len(champ_name)):
        temp[i] = soup.select(
            'body > div.l-wrap.l-wrap--champion > div.l-container > div.l-champion-index > div.l-champion-index-content > div.l-champion-index-content--main > div.champion-index__champion-list > div:nth-child('+ str(i + 1) +') > a'
        )
        if(temp[i] != []):
            temp[i] = str(temp[i][0])
            index_name = temp[i].find('statistics')
            # index_link = temp[i].find('>')
            champ_name[i] = temp[i][19:index_name - 1]
            # champ_link[i] = 'https://op.gg'+temp[i][9:index_link - 1]
            crawl_img(champ_name[i])

def crawl_img(champ_name):
    # url = "http://ddragon.leagueoflegends.com/cdn/9.8.1/img/champion/" + champ_name[0].upper() + champ_name[1:] + ".png"
    url = "http://opgg-static.akamaized.net/images/lol/champion/" + champ_name[0].upper() + champ_name[1:] + ".png?image=w_140&v=1"
    source_code = requests.get(url)
    img_content = source_code.content
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = dir_path + '/public/images/champion_images/' + champ_name + '.png'
    print(champ_name)
    with open(filename, "wb") as f:
        f.write(img_content)

def crawl_champnum():
    url = 'https://www.mobafire.com/league-of-legends/champions'
    req = requests.get(url)
    plain_text = req.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for i in range(143):
        good = soup.select('#content > div > div.self-clear.mf-redesign > div.col-left > div > a:nth-child(' + str(i + 1) + ')')
        good = str(good[0])
        babo = good.index('champion')
        babo2 = good.index('special')
        champnum = good[babo + 9:babo2 - 2]
        crawl_mastery(champnum)

def crawl_mastery(champnum):
    url = 'https://www.mobafire.com/league-of-legends/champion/' + champnum + '/stats'
    req = requests.get(url)
    plain_text = req.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    good = soup.select('#content > div > div.mf-redesign > div.col-left > div.champ-pages > div > div.champ-build > div:nth-child(2) > div.champ-build__section__content > div.champ-build__section__content__tab.current > div > div')
    print(champnum)
    if(good != []):
        good = str(good[0])
        babo = good.index('new-runes__item__circle')
        good = good[babo + 1:]
        babo = good.index('new-runes__item__circle')
        good = good[babo + 1:]
        babo = good.index('src')
        babo2 = good.index('.png')
        good = good[babo + 5:babo2 + 4]
        url = "http://www.mobafire.com" + good
        source_code = requests.get(url)
        img_content = source_code.content
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = dir_path + '/public/images/mastery_images/' + champnum.split('-')[0] + '.png'
        with open(filename, "wb") as f:
                f.write(img_content)    

def crawl_winrate():
#     url = "http://fow.kr/statistics"
    f = open("champion-normal-winrate.txt", 'w')
    url = "https://www.op.gg/champion/statistics"
    req = requests.get(url)
    plain_text = req.text
    soup = str(BeautifulSoup(plain_text, 'html.parser'))
#     soup = soup.select('#r_out > tr:nth-child(1) > td:nth-child(7)')
    chmp_list = [0] * 715
    wr_list = [0] * 715
    for i in range(200):
        print(i)
        try:
                chmp_list[i] = soup.index('champion-index-table__name')
                wr_list[i] = soup.index('champion-index-table__cell champion-index-table__cell--value')
                soup2 = soup[chmp_list[i] + 28:]
                endindx = soup2.index('</div>')
                # print(soup[chmp_list[i] + 28:chmp_list[i] + 28 + endindx])
                # print(soup[wr_list[i] + 62:wr_list[i] + 68])
                f.write(soup[chmp_list[i] + 28:chmp_list[i] + 28 + endindx] + ',' + soup[wr_list[i] + 62:wr_list[i] + 68] + '\n')
                soup = soup[wr_list[i] + 300:]
        except ValueError as e:
                print(e)
#     print(wr_list)
    f.close()

crawl_list()
# crawl_champnum()
# crawl_winrate()