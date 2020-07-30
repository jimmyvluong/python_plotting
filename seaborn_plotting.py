#8A-D College Success as SUBPLOTS

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

from matplotlib.pyplot import figure

plt.style.use('seaborn')
# Read in primary csv file as a DataFrame
success_df = pd.read_csv("8AD_success_table.csv")

# Read in csv file with sector averages as a DataFrame
avg_df = pd.read_csv("8AD_success_table_sector_avg.csv")

# Get a list of unique college names from the primary DataFrame
college_names_list = success_df['college_name'].unique()

# Loop through the college_names_list by each college_name
for college_name in college_names_list:
    
    # Filter the DataFrame based on column values
    #FTFE
    college_df1 = success_df[(success_df['college_name'] == college_name) 
                            & (success_df['level_of_study'] == 'FE')
                            & (success_df['mode_of_study'] == 'FT')]
    #FTHE
    college_df2 = success_df[(success_df['college_name'] == college_name) 
                            & (success_df['level_of_study'] == 'HE')
                            & (success_df['mode_of_study'] == 'FT')]
    #PTFE
    college_df3 = success_df[(success_df['college_name'] == college_name) 
                            & (success_df['level_of_study'] == 'FE')
                            & (success_df['mode_of_study'] == 'PT')]
    #PTHE
    college_df4 = success_df[(success_df['college_name'] == college_name) 
                            & (success_df['level_of_study'] == 'HE')
                            & (success_df['mode_of_study'] == 'PT')]
    
    # Plot the year and success_percentage for each college_name
    
    figure(num=None, figsize=(11, 8), dpi=300, facecolor='w', edgecolor='k')
    
    plt.subplot(2,2,1)
    plt.plot(college_df1.year, college_df1.success_percentage, label = college_name)
    
    # Plot the overall sector
    plt.plot(avg_df.year, avg_df.ftfe, color='gray', linestyle='dashed', label = "Overall Sector")
    # Add titles and format the graph
    plt.suptitle("Students Achieving a Recognized Qualification")
    plt.title('8A Full-Time Further Education')
    plt.xticks((np.arange(2014, 2019, step = 1)))
    plt.yticks((np.arange(0, 110, step = 10)))
    plt.ylabel('% Successful', fontsize = 12)
    plt.legend(loc = 'lower right', fontsize = 12)
    
    # Add labels to graph
    for index, row in college_df1.iterrows():
        plt.annotate(str(row['success_percentage']), (row['year'], row['success_percentage']))
    
    plt.subplot(2,2,2)
    plt.plot(college_df2.year, college_df2.success_percentage, label = college_name)
    # Plot the overall sector
    plt.plot(avg_df.year, avg_df.fthe, color='gray', linestyle='dashed', label = "Overall Sector")

    plt.title('8B Full-Time Higher Education')
    plt.xticks((np.arange(2014, 2019, step = 1)))
    plt.yticks((np.arange(0, 110, step = 10)))
    plt.ylabel('% Successful', fontsize = 12)
    plt.legend(loc = 'lower right', fontsize = 12)
    
    plt.subplot(2,2,3)
    plt.plot(college_df3.year, college_df3.success_percentage, label = college_name)
    # Plot the overall sector
    plt.plot(avg_df.year, avg_df.ptfe, color='gray', linestyle='dashed', label = "Overall Sector")
    # Add titles and format the graph
    plt.title('8C Part-Time Further Education')
    plt.xticks((np.arange(2014, 2019, step = 1)))
    plt.yticks((np.arange(0, 110, step = 10)))
    plt.xlabel('Academic Year', fontsize = 12)
    plt.ylabel('% Successful', fontsize = 12)
    plt.legend(loc = 'lower right', fontsize = 12)
    
    plt.subplot(2,2,4)
    plt.plot(college_df4.year, college_df4.success_percentage, label = college_name)
    # Plot the overall sector
    plt.plot(avg_df.year, avg_df.pthe, color='gray', linestyle='dashed', label = "Overall Sector")
    # Add titles and format the graph
    plt.title('8D Part-Time Higher Education')
    plt.xticks((np.arange(2014, 2019, step = 1)))
    plt.yticks((np.arange(0, 110, step = 10)))
    plt.xlabel('Academic Year', fontsize = 12)
    plt.ylabel('% Successful', fontsize = 12)
    plt.legend(loc = 'lower right', fontsize = 12)
    
    plt.savefig('Images/' + college_name + "_8ABCD_success.pdf")
    
    # Make the graph appear at the end of each loop
    plt.show()
