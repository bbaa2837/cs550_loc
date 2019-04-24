import requests
from bs4 import BeautifulSoup
import urllib
import os

def crawl_list():
    # champ_list = 
#     url = 'http://gameinfo.leagueoflegends.co.kr/ko/game-info/champions'
#     url = 'https://www.leagueofgraphs.com/ko/'
    url = 'https://www.op.gg/champion/statistics'
    req = requests.get(url)
#     print(source_code.content)
    plain_text = req.text
    soup = BeautifulSoup(plain_text, 'html.parser')
#     a = soup.select('body > div.l-wrap.l-wrap--champion > div.l-container > div.l-champion-index > div.l-champion-index-content > div.l-champion-index-content--main > div.champion-index__champion-list > div:nth-child(1) > a')
#     a = str(a[0])
#     indx_name = a.find('statistics')
#     indx_link = a.find('>')
#     champ_name = a[19:indx_name - 1]
#     champ_link = 'https://op.gg'+a[9:indx_link - 1]
    temp = [0] * 143
    champ_name = [0] * 143
#     champ_link = [0] * 143
    for i in range(len(champ_name)):
        temp[i] = soup.select(
            'body > div.l-wrap.l-wrap--champion > div.l-container > div.l-champion-index > div.l-champion-index-content > div.l-champion-index-content--main > div.champion-index__champion-list > div:nth-child('+ str(i + 1) +') > a'
        )
        temp[i] = str(temp[i][0])
        index_name = temp[i].find('statistics')
        # index_link = temp[i].find('>')
        champ_name[i] = temp[i][19:index_name - 1]
        # champ_link[i] = 'https://op.gg'+temp[i][9:index_link - 1]
        crawl_img(champ_name[i])

#selector : #championListBox > div:nth-child(1) > a

def crawl_img(champ_name):
        url = "http://ddragon.leagueoflegends.com/cdn/9.8.1/img/champion/" + champ_name[0].upper() + champ_name[1:] + ".png"
        source_code = requests.get(url)
        img_content = source_code.content
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = dir_path + '/public/images/champion_images/' + champ_name + '.png'
        with open(filename, "wb") as f:
                f.write(img_content)
        
crawl_list()
