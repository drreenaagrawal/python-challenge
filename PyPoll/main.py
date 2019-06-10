import os, csv

csv_path = os.path.join('..', 'Resources', 'election_data.csv')

candidate = []
candidate_list = []
frequency = []
percent = []
#arrays to hold the third column of the csv file, the unique candidate list, frequency of votes, and % of votes

f = open("outputpoll.txt", "a") 
#open text file outputbank.txt to store output

print("'''text", file = f)
print("Election Results", file = f)
print("Election Results")

with open(csv_path, newline="", encoding="UTF8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
#open and read csv file
    next(csv_reader)
#moves over the header row

    for row in csv_reader:
        candidate.append(row[2])
        #appends the third column of the csv file to candidate

for x in candidate:
    if x not in candidate_list:
        candidate_list.append(x)
#candidate_list provides the list of candidates


for y in candidate_list:
    frequency.append(candidate.count(y))
    #frequency gives the number of votes received by each candidate

total = sum(frequency)
print("-" * 30, file = f)
print("-" * 30)
print(f"Total number of votes: {total}", file = f)
print(f"Total number of votes: {total}")
print("-" * 30, file = f)
print("-" * 30)

for z in frequency:
    percent.append(round((z*100)/total,3))
    #percent gives the % of votes received by each candidate, rounded to the third decimal

max_frequency = max(frequency)
#max_frequency gives the highest vote count for a candidate

roster = zip(candidate_list, percent, frequency)
for row in roster:
    print(f"{row[0]}: {row[1]}% ({row[2]}) ", file = f)
    print(f"{row[0]}: {row[1]}% ({row[2]}) ") 

    if row[2] == max_frequency:
        winner = row[0]

print("-" * 30, file = f)
print("-" * 30)
print(f"Winner: {winner}", file = f)
print(f"Winner: {winner}")
print("-" * 30, file = f)
print("-" * 30)
print("'''", file = f)

f.close()
#close text file