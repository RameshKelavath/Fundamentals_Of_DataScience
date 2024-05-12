#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing  libraries.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Setting a visual style for the Graph.

plt.style.use('ggplot')

# Loading 2020 exam Data Set.

data_path_2020 = '2020input9.csv'
data_2020 = pd.read_csv(data_path_2020, header=None, sep='\s+')
data_2020.columns = ['MinScore', 'MaxScore', 'Students']

# Calculating the mid scores and total scores.

data_2020['MidScore'] = (data_2020['MinScore'] + data_2020['MaxScore']) / 2
data_2020['TotalScore'] = data_2020['MidScore'] * data_2020['Students']

# Calculating the average and standard deviation for the 2020 exam data set.

total_students = data_2020['Students'].sum()
total_points = data_2020['TotalScore'].sum()
avg_score_2020 = total_points / total_students
std_dev_2020 = np.sqrt(((data_2020['MidScore'] - avg_score_2020) ** 2 * data_2020['Students']).sum() / total_students)

# Calculating the median score for 2020 exam data set.

data_2020['Cumulative'] = data_2020['Students'].cumsum()
median_pos = total_students / 2
median_bin = data_2020[data_2020['Cumulative'] >= median_pos].iloc[0]
prev_cumulative = data_2020[data_2020['Cumulative'] < median_pos]['Cumulative'].max() if not data_2020[data_2020['Cumulative'] < median_pos].empty else 0
median_score = median_bin['MinScore'] + ((median_pos - prev_cumulative) / median_bin['Students']) * (median_bin['MaxScore'] - median_bin['MinScore'])

# Loading 2024 exam Data Set.
data_path_2024 = '2024input9.csv'
scores_2024 = pd.read_csv(data_path_2024).iloc[:, 0]

# Calculating the median score for 2020 exam data set.
avg_2024 = scores_2024.mean()
std_dev_2024 = scores_2024.std()

# Creating simulated data for both years for demonstration.
np.random.seed(42)
simulated_2020 = pd.Series(np.random.normal(avg_score_2020, std_dev_2020, 300))
simulated_2024 = pd.Series(np.random.normal(avg_2024, std_dev_2024, 300))

# Determining bins for the histogram.
bins = np.histogram_bin_edges(np.concatenate([simulated_2020, simulated_2024]), bins='auto')

# Plotting the histograms for comparison.
plt.figure(figsize=(14, 9))
plt.hist([simulated_2020, simulated_2024], bins=bins, alpha=0.75, label=['2020 Scores', '2024 Scores'],
         color=['#4E79A7', '#F28E2B'], stacked=True, edgecolor='black')

# Adding  stattistics_summary box to the plot.

statistics_summary = (
    "Student ID:             23029839\n"
    "Mean 2020:            {:6.2f}\n"
    "STD 2020:             {:6.2f}\n"
    "Mean 2024:            {:6.2f}\n"
    "STD 2024:             {:6.2f}\n"
    "Median Grade (V)- {:6.2f}"
).format(avg_score_2020, std_dev_2020, avg_2024, std_dev_2024, median_score)

# Adding statistics_summary  to the plot with improved alignment
plt.text(0.01, 0.98, statistics_summary, transform=plt.gca().transAxes, fontsize=13, 
         verticalalignment='top', horizontalalignment='left', 
         bbox=dict(boxstyle='round4', facecolor='white', alpha=0.5))


# Plotting Styles.
plt.title('Comparison of 2020 and 2024 Exam Scores', fontsize=16,fontweight='bold')
plt.xlabel('Scores', fontsize=16,fontweight='bold')
plt.ylabel('Number of Students', fontsize=16,fontweight='bold')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.grid(True, linestyle='--', alpha=0.8)

# Saving and showing the plot.
plt.savefig('23029839.png', bbox_inches='tight', dpi=300)
plt.show()


# In[ ]:




