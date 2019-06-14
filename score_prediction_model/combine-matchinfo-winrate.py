import sys

# read match info
match_file = open(sys.argv[1])
matches = [line.strip() for line in match_file]
match_file.close()

# read winrate file
winrate_file = open(sys.argv[2], encoding='utf-8')
winrates = [line.strip().split(',')[2] for line in winrate_file]
winrate_file.close()

output = open("match-data.csv", 'w')

i = 0
for match in matches:
  temp = [match]
  for j in range(10):
    temp += [winrates[i]]
    i += 1

  output.write(','.join(temp) + '\n')

output.close()
