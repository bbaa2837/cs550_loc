# CS550 Team Project LoC
## Look on Combination

### Environments Specification
1. Web browser: Chrome, Safari
2. Python v3.5 or higher
3. Nodejs v10.15.3

### Downloading
```
git clone https://github.com/bbaa2837/cs550_loc
cd cs550_loc
```

### Before Start
```
npm install
mkdir public\images\champion_images
mkdir public\images\mastery_images
```

### Running
```
npm run dev:server
npm run dev:client
```
### For crawling
Python libraries are needed
```
pip3 install requests
pip3 install bs4
```

To crawl champions, masteries and images, run
```
python3 crawler.py
```

### Preprocessing data
Change iteration of data collection -> change numofiterations in server.js(line 17).


For changing champion id to name
```
python3 champion-id-to-name-converter.py <csv file you want to convert>
```

For gathering win rate for champions of each player
```
python3 crawler-winrate.py summonname-champname.csv
```

### Setting DB
npm install mysql

