# CS550 Team Project LoC
## Look on Combination

### Environments Specification
1. Web browser: Chrome, Safari
2. Python v3.6
3. Nodejs v10.15.3

### Downloading
```
git clone https://github.com/bbaa2837/cs550_loc
cd cs550_loc
```

### Before Start
```
./start_setup.sh

pip install tensorflow
pip install pandas
pip install numpy
```

### Running
```
npm run dev:server
npm run dev:client
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

### DB
check the database connection from localhost:3000/info
