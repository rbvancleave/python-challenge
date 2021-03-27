#!/usr/bin/env python
# coding: utf-8

# In[11]:


# import pandas
import pandas as pd


# In[12]:


df = pd.read_csv('Resources/budget_data.csv')


# In[13]:


month_count = df.count()[0]
total_pl = df['Profit/Losses'].sum()


print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {month_count}')
print(f'Total: ${total_pl}')

month_ind = []
change = []
for num in range(0,month_count):
    if num == 0:
        pass
    else:
        change.append(int(df['Profit/Losses'][num])-int(df['Profit/Losses'][num-1]))
        month_ind.append(df['Date'][num])

change_avg = round(sum(change)/len(change),2)
print(f'Average Change: ${change_avg}')


change_max = max(change)
i = change.index(change_max)
max_month = month_ind[i]
print('Greatest Increase in Profits:',max_month, f'(${change_max})')

change_min = min(change)
i = change.index(change_min)
min_month = month_ind[i]
print('Greatest Decrease in Profits:',min_month, f'(${change_min})')


# In[ ]:




