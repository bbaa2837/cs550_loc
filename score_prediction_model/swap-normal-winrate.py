import sys

championid_file = open(sys.argv[1])
championid_map = {}
for line in championid_file:
  temp = line.strip().split(',')
  # print(temp)
  # exit(1)
  championid_map[temp[3]] = temp[4]
championid_file.close()

match_file = open(sys.argv[2])
newname = sys.argv[2][:-4] + '-processed.csv'
output = open(newname, 'w+')

lines = [line.strip().split(',') for line in match_file]
output.write(','.join(lines[0]) + '\n')

for line in lines[1:]:
  for i in range(10):
    line[i+10] = championid_map[line[i]]

  output.write(','.join(line) + '\n')

output.close()
match_file.close()
