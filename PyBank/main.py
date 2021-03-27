#!/usr/bin/env python
# coding: utf-8

# Import Dependencies

import os
import csv

# Define CSV Path and Open CSV File

budget_data_csv = os.path.join('Resources/budget_data.csv')

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_file)
    
# create empty lists for time period (month) and Profit/Loss (p_l)
    month = []
    p_l = []
    
# Go through each row to append values to month and p_l list

    for row in csv_reader:
        month.append(row[0])
        p_l.append(int(row[1]))
        
# Calculate number of time periods (months) and total Profit/Loss (p_l)
        
    num_month = len(month)
    total_pl = sum(p_l)

# Create list to add the values of each variance from month to month

    change = []
    
    x = 0
    
    for i in range(0,num_month):
        if i == 0:
            pass
        else:
            change.append(int(p_l[i])-int(p_l[i-1]))
    
# Save Variable for avg, max, min

    avg_change = round(sum(change)/len(change),2)
    max_change = max(change)
    min_change = min(change)
    max_month = month[change.index(max_change)]
    min_month = month[change.index(min_change)]

# Print to match HW format

    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {num_month}')
    print(f'Total: ${total_pl}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {max_month} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_month} (${min_change})')
    
# Write to txt file

    output_path = os.path.join('analysis/PyBank_output.txt')
    with open(output_path, "w") as f:
        f.write('Financial Analysis\n')
        f.write('----------------------------\n')
        f.write(f'Total Months: {num_month}\n')
        f.write(f'Total: ${total_pl}\n')
        f.write(f'Average Change: ${avg_change}\n')
        f.write(f'Greatest Increase in Profits: {max_month} (${max_change})\n')
        f.write(f'Greatest Decrease in Profits: {min_month} (${min_change})\n')

