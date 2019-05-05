import sys

# USAGE: python champion-id-to-name-converter.py <summonername-champid file>

# The input is the summonername-champid file
# EXPECTED FORMAT OF FILE:
# summoner name, champion id
# EXPECTED OUTPUT OF FILE:
# summoner name, champion name
file = open(sys.argv[1], encoding='utf-8')
lines = [line.strip().split(',') for line in file]
file.close()

idToNameFile = open('champion-id-map.txt')
idToNameDict = {}

for line in idToNameFile:
  line = line.strip().split(',')
  idToNameDict[line[1]] = line[0]

idToNameFile.close()

output = open('summonname-champname2.csv', 'w', encoding='utf-8')

for line in lines:
  if not line[1] in idToNameDict:
    print(line[1] + ' is not ID of a champion')
    exit(1)

  line[1] = idToNameDict[line[1]]
  output.write(','.join(line) + '\n')

output.close()
