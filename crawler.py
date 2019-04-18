import requests
from bs4 import BeautifulSoup
import urllib
import os

def crawl_list():
    # champ_list = 
#     url = 'http://gameinfo.leagueoflegends.co.kr/ko/game-info/champions'
    url = 'https://www.leagueofgraphs.com/ko/'
    source_code = requests.get(url)
    print(source_code.content)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

#selector : #championListBox > div:nth-child(1) > a

def crawl_img(champ_name):
        url = "http://ddragon.leagueoflegends.com/cdn/9.8.1/img/champion/" + champ_name + ".png"
        source_code = requests.get(url)
        img_content = source_code.content
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = dir_path + '/public/images/champion_images/garen.png'
        with open(filename, "wb") as f:
                f.write(img_content)
        
crawl_list()
# crawl_img('Garen')