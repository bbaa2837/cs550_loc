import sys

f = open(sys.argv[1])
matches = [line.strip().split(",") for line in f]
f.close()

output = open("game-actual-score.csv", 'w+')

matchid_idx = 0
result_idx = 2
duration_idx = 1
team1_idx = 3
team2_idx = 13

for match in matches:
  matchid = match[matchid_idx]
  duration = int(match[duration_idx]) / 60.0
  team1 = match[team1_idx:(team1_idx+10)]
  team2 = match[team2_idx:]

  team1_result = match[result_idx]
  team2_result = "Win" if team1_result == "Fail" else "Fail"

  # Score of 2 teams in case team 1 win
  team1_score = (100 - (duration - 10)) / 100.0
  team2_score = (duration - 10) / 100.0

  # If team 1 loses, then the scores are flipped
  if team1_result == "Fail":
    team1_score, team2_score = team2_score, team1_score

  # for each match we can extract 2 samples and scores of 2 teams
  team1_line = [matchid, match[duration_idx], team1_result] + team1 + team2 + [str(team1_score)]
  team2_line = [matchid, match[duration_idx], team2_result] + team2 + team1 + [str(team2_score)]

  output.write(','.join(team1_line) + '\n')
  output.write(','.join(team2_line) + '\n')

output.close()
      