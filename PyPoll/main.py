#!/usr/bin/env python
# coding: utf-8

# Import Dependencies

import os
import csv

# Define CSV Path and Open CSV File

election_data_csv = os.path.join('Resources/election_data.csv')

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_file)

# create empty set to collect candidate names 
# create empty dictionary to assign vote counts (vc) to candidates
# create empty dictionary to assign vote percentage (pct) to candidates

    candidate_set = set([])
    candidate_vc_dict = {}
    candidate_pct_dict = {}
    
# Go through each row, see if new candidate, then add vote to dictionary
    
    for row in csv_reader:
        cand = row[2]
        if cand in candidate_set:
            candidate_vc_dict[cand] = candidate_vc_dict[cand] + 1
        else:
            candidate_set.add(cand)
            candidate_vc_dict[cand] = 1
            
# Calculate total votes
            
    total_votes = sum(candidate_vc_dict.values())

# Calculate Candidate Vote Percentage of the Total Votes
# clean cand_pct and add to candidate_pct_dict   

    candidate_pct_dict = {}
    for k,v in candidate_vc_dict.items():
        cand_key = k
        cand_pct = (v/total_votes)*100

        cand_pct = str(round(cand_pct,2))+'%'
        candidate_pct_dict[cand_key] = cand_pct

# determine vote order

    vote_counts = []
    for i in candidate_vc_dict.values():
        vote_counts.append(i)
    vote_counts.sort(reverse = True)
    
# Assign Candidate Order

    first = vote_counts[0]
    second = vote_counts[1]
    third = vote_counts[2]
    fourth = vote_counts[3]

    for k,v in candidate_vc_dict.items():
        if v == first:
            winner = k
        elif v == second:
            second_place = k
        elif v == third:
            third_place = k
        else:
            fourth_place = k

# Print to match HW format
            
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')       
            
    print(f'{winner}:',candidate_pct_dict[winner],f'({candidate_vc_dict[winner]})')
    print(f'{second_place}:',candidate_pct_dict[second_place],f'({candidate_vc_dict[second_place]})')
    print(f'{third_place}:',candidate_pct_dict[third_place],f'({candidate_vc_dict[third_place]})')
    print(f'{fourth_place}:',candidate_pct_dict[fourth_place],f'({candidate_vc_dict[fourth_place]})')

    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

# Write to txt file
    output_path = os.path.join('analysis/PyPoll_output.txt')
    with open(output_path, "w") as f:
        
        f.write('Election Results\n')
        f.write('-------------------------\n')
        f.write(f'Total Votes: {total_votes}\n')
        f.write('-------------------------\n')  
        
        f.write(f'{winner}: {candidate_pct_dict[winner]} {candidate_vc_dict[winner]}\n')
        f.write(f'{second_place}: {candidate_pct_dict[second_place]} {candidate_vc_dict[second_place]}\n')
        f.write(f'{third_place}: {candidate_pct_dict[third_place]} {candidate_vc_dict[third_place]}\n')
        f.write(f'{fourth_place}: {candidate_pct_dict[fourth_place]} {candidate_vc_dict[fourth_place]}\n')
        
        
        f.write('-------------------------\n')
        f.write(f'Winner: {winner}\n')
        f.write('-------------------------\n')


# In[ ]:





# In[ ]:




