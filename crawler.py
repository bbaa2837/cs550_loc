import requests
from bs4 import BeautifulSoup

def crawl_list():
    # champ_list = 
    url = 'http://gameinfo.leagueoflegends.co.kr/ko/game-info/champions/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for champs in soup.seect('#champion-list-content > div > ul'):
        print(champs)

# def crawl_champ(max_champ_num):
#     champ_num = 1
#     champ_name = 
#     while champ_name < max_champ_num:
#         url = 'http://gameinfo.leagueoflegends.co.kr/ko/game-info/champions/' + str(champ_name)
