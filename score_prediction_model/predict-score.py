from keras.models import Sequential,load_model
import pandas as pd
import numpy as np
import sys

model = load_model('model4.h5')
# model.summary()

# testing_data = pd.read_csv('testing-data-unnormalized-processed.csv', delimiter=',')
# testing_label = pd.read_csv('testing-label-classification.csv', delimiter=',')

# testing_score = model.evaluate(testing_data, testing_label, batch_size=32)
# print(testing_score)

# championid_file = open('champion-winrate.csv')

championid_file = [
    "Aatrox,aatrox,266,1,0.5244", "Ahri,ahri,103,2,0.5272", "Akali,akali,84,3,0.4712",
    "Alistar,alistar,12,4,0.4923", "Amumu,amumu,32,5,0.5031", "Anivia,anivia,34,6,0.5146",
    "Annie,annie,1,7,0.5103", "Ashe,ashe,22,8,0.5219", "AurelionSol,aurelionsol,136,9,0.5432",
    "Azir,azir,268,10,0.488", "Bard,bard,432,11,0.5319", "Blitzcrank,blitzcrank,53,12,0.5067",
    "Brand,brand,63,13,0.4963", "Braum,braum,201,14,0.4689", "Caitlyn,caitlyn,51,15,0.4921",
    "Camille,camille,164,16,0.5151", "Cassiopeia,cassiopeia,69,17,0.5124", "Chogath,chogath,31,18,0.5077",
    "Corki,corki,42,19,0.5046", "Darius,darius,122,20,0.5067", "Diana,diana,131,21,0.4788",
    "Draven,draven,119,22,0.5284", "DrMundo,drmundo,36,23,0.4909", "Ekko,ekko,245,24,0.5151",
    "Elise,elise,60,25,0.5191", "Evelynn,evelynn,28,26,0.5097", "Ezreal,ezreal,81,27,0.4925",
    "Fiddlesticks,fiddlesticks,9,28,0.5122", "Fiora,fiora,114,29,0.4883", "Fizz,fizz,105,30,0.5154",
    "Galio,galio,3,31,0.4774", "Gangplank,gangplank,41,32,0.5171", "Garen,garen,86,33,0.5157",
    "Gnar,gnar,150,34,0.4912", "Gragas,gragas,79,35,0.4797", "Graves,graves,104,36,0.4929",
    "Hecarim,hecarim,120,37,0.5094", "Heimerdinger,heimerdinger,74,38,0.501", "Illaoi,illaoi,420,39,0.5212",
    "Irelia,irelia,39,40,0.4865", "Ivern,ivern,427,41,0.5159", "Janna,janna,40,42,0.5217",
    "JarvanIV,jarvaniv,59,43,0.49", "Jax,jax,24,44,0.5023", "Jayce,jayce,126,45,0.4984",
    "Jhin,jhin,202,46,0.4904", "Jinx,jinx,222,47,0.532", "Kaisa,kaisa,145,48,0.4978",
    "Kalista,kalista,429,49,0.4618", "Karma,karma,43,50,0.49", "Karthus,karthus,30,51,0.5184",
    "Kassadin,kassadin,38,52,0.5095", "Katarina,katarina,55,53,0.5053", "Kayle,kayle,10,54,0.5108",
    "Kayn,kayn,141,55,0.5038", "Kennen,kennen,85,56,0.5054", "Khazix,khazix,121,57,0.4926",
    "Kindred,kindred,203,58,0.4951", "Kled,kled,240,59,0.5229", "KogMaw,kogmaw,96,60,0.4985",
    "Leblanc,leblanc,7,61,0.4747", "LeeSin,leesin,64,62,0.4819", "Leona,leona,89,63,0.5153",
    "Lissandra,lissandra,127,64,0.4854", "Lucian,lucian,236,65,0.4849", "Lulu,lulu,117,66,0.5028",
    "Lux,lux,99,67,0.5174", "Malphite,malphite,54,68,0.4918", "Malzahar,malzahar,90,69,0.5241",
    "Maokai,maokai,57,70,0.517", "MasterYi,masteryi,11,71,0.4921", "MissFortune,missfortune,21,72,0.5182",
    "MonkeyKing,monkeyking,62,73,0.5082", "Mordekaiser,mordekaiser,82,74,0.5385", "Morgana,morgana,25,75,0.5198",
    "Nami,nami,267,76,0.5101", "Nasus,nasus,75,77,0.4837", "Nautilus,nautilus,111,78,0.529",
    "Neeko,neeko,518,79,0.5115", "Nidalee,nidalee,76,80,0.5071", "Nocturne,nocturne,56,81,0.4644",
    "Nunu,nunu,20,82,0.5164", "Olaf,olaf,2,83,0.5086", "Orianna,orianna,61,84,0.492",
    "Ornn,ornn,516,85,0.4911", "Pantheon,pantheon,80,86,0.5251", "Poppy,poppy,78,87,0.5084",
    "Pyke,pyke,555,88,0.5081", "Quinn,quinn,133,89,0.5065", "Rakan,rakan,497,90,0.5136",
    "Rammus,rammus,33,91,0.5263", "RekSai,reksai,421,92,0.5035", "Renekton,renekton,58,93,0.5049",
    "Rengar,rengar,107,94,0.5204", "Riven,riven,92,95,0.5073", "Rumble,rumble,68,96,0.5172",
    "Ryze,ryze,13,97,0.4492", "Sejuani,sejuani,113,98,0.52", "Shaco,shaco,35,99,0.5213",
    "Shen,shen,98,100,0.5148", "Shyvana,shyvana,102,101,0.4999", "Singed,singed,27,102,0.4711",
    "Sion,sion,14,103,0.5078", "Sivir,sivir,15,104,0.5416", "Skarner,skarner,72,105,0.4952",
    "Sona,sona,37,106,0.5328", "Soraka,soraka,16,107,0.5071", "Swain,swain,50,108,0.5054",
    "Sylas,sylas,517,109,0.4933", "Syndra,syndra,134,110,0.4793", "TahmKench,tahmkench,223,111,0.5018",
    "Taliyah,taliyah,163,112,0.523", "Talon,talon,91,113,0.5273", "Taric,taric,44,114,0.5081",
    "Teemo,teemo,17,115,0.5036", "Thresh,thresh,412,116,0.5125", "Tristana,tristana,18,117,0.4933",
    "Trundle,trundle,48,118,0.4425", "Tryndamere,tryndamere,23,119,0.5059", "TwistedFate,twistedfate,4,120,0.5033",
    "Twitch,twitch,29,121,0.4517", "Udyr,udyr,77,122,0.4952", "Urgot,urgot,6,123,0.5014",
    "Varus,varus,110,124,0.4894", "Vayne,vayne,67,125,0.489", "Veigar,veigar,45,126,0.5042",
    "Velkoz,velkoz,161,127,0.5099", "Vi,vi,254,128,0.5271", "Viktor,viktor,112,129,0.4857",
    "Vladimir,vladimir,8,130,0.4939", "Volibear,volibear,106,131,0.5255", "Warwick,warwick,19,132,0.5017",
    "Xayah,xayah,498,133,0.5095", "Xerath,xerath,101,134,0.5012", "XinZhao,xinzhao,5,135,0.5164",
    "Yasuo,yasuo,157,136,0.4817", "Yorick,yorick,83,137,0.5287", "Zac,zac,154,138,0.4908",
    "Zed,zed,238,139,0.5113", "Ziggs,ziggs,115,140,0.5068", "Zilean,zilean,26,141,0.5292",
    "Zoe,zoe,142,142,0.5036", "Zyra,zyra,143,143,0.5103"    
]

championid_map = {}
for line in championid_file:
  temp = line.strip().split(',')
  # print(temp)
  # exit(1)
  championid_map[temp[1]] = [int(temp[3])/143, temp[4]]
# championid_file.close()

champion_list1 = sys.argv[1:]
input_data = [""] * 20
for i in range(10):
  input_data[i] = championid_map[champion_list1[i]][0]
  input_data[i+10] = championid_map[champion_list1[i]][1]

input_data = np.array([input_data])
# print(input_data)
team1_score = model.predict(input_data)[0][0]

champion_list2 = champion_list1[5:] + champion_list1[:5]
input_data = [""] * 20
for i in range(10):
  input_data[i] = championid_map[champion_list2[i]][0]
  input_data[i+10] = championid_map[champion_list2[i]][1]

input_data = np.array([input_data])
# print(input_data)
team2_score = model.predict(input_data)[0][0]
print(team1_score, team2_score)
