import sys
from random import randint

data_file = open(sys.argv[1])
lines = [line for line in data_file]
data_file.close()

idx_set = set()
while len(idx_set) < 3000:
  idx_set.add(randint(0,10304))

temp_set = idx_set.copy()

# 2000 samples are randomly selected as testing data
testing_data_file = open("testing-data.csv", 'w+')
for i in range(2000):
  testing_data_file.write(lines[idx_set.pop()])
testing_data_file.close()

# 1000 samples are used for cross validation set
cv_data_file = open("cv-data.csv", 'w+')
for e in idx_set:
  cv_data_file.write(lines[e])
cv_data_file.close()

# the rest are training data file
training_data_file = open("training-data.csv", 'w+')
for i in range(len(lines)):
  if i in temp_set:
    continue
  else:
    training_data_file.write(lines[i])
training_data_file.close()
