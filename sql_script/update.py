import csv

champions = list()
with open("../champion-id-map.csv", 'r') as csv_file:
	reader = csv.reader(csv_file, delimiter = ',')
	next(reader)
	for lines in reader:
		champions.append(lines[0])

column_type = ["champion", "mastery", "item"]

for column in column_type:
	for champ in champions:
		print("update champion set {}_img='./public/images/{}_images/{}.png' where name = '{}';".format(column, column, champ.lower(), champ))
