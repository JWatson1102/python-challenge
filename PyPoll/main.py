import os
import csv
import pathlib

voter_path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources','election_data.csv' )

with open(voter_path) as file_copy:
    reader = csv.reader(file_copy, delimiter = ",")
    header = next(file_copy)
    
    candidate_list = []

    for row in reader:
        candidate_list.append(row[2])

total_votes = len(candidate_list)

#creates a list of each unique candidate
unique_candidate_list = []

for name in candidate_list:
    if name not in unique_candidate_list:
        unique_candidate_list.append(name)

#generates a dictionary with
#name_of_candidate : 0
candidate_votes = {}

for name in unique_candidate_list:
    candidate_votes[name] = 0

#adds 1 to each candidates dictionary intiger value
for name in candidate_list:
    candidate_votes[name] += 1

#print(candidate_votes)

winner = ""
winner_percent = 0

candidate_percentage = {}

master_dictionary = {}



for name in unique_candidate_list:

    candidate_percentage[name] = round(((candidate_votes[name] / total_votes) * 100),0)

    if candidate_percentage[name] > winner_percent:
       winner = name
       winner_percent = candidate_percentage[name] 
    
    master_dictionary[name] = {
        'Percentage' : candidate_percentage[name],
        'Total' : candidate_votes[name]
        }


output_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "analysis", "analysis.txt" )

final_output = [
    'Election Results',
    '---------------------',
    'Total Votes: ' + str(total_votes),
    '---------------------',
]

for name in unique_candidate_list:
    final_output.append(
            name + ': ' + str(master_dictionary[name]['Percentage']) + '% (' + str(master_dictionary[name]['Total']) + ')'
        )

last_part_list = [
    '---------------------',
    'Winner: ' + winner,
    '---------------------'
]

final_output.extend(last_part_list)

with open(output_path, 'w') as output_interactor:

    for line in final_output:
        output_interactor.write(line)
        output_interactor.write("\n")

for line in final_output:
    print(line)





