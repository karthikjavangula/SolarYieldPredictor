import pandas as pd
import numpy as np

# Code to split a csv file into multiple smaller csv files based on a categorical value

# Read the csv file
df = pd.read_csv('data/combined_data2.csv')

# Get the unique values of the column to split on
unique_values = df['SOURCE_KEY'].unique()

# # Split the dataframe based on the unique values
# for value in unique_values:
#     df_split = df[df['SOURCE_KEY'] == value]
#     df_split.to_csv(f'data/split_by_source/{value}.csv', index=False)

# Count the number of rows in each split and save it to a txt file
with open('data/split_by_source/row_counts.txt', 'w') as f:
    for value in unique_values:
        count = df[df['SOURCE_KEY'] == value].shape[0]
        f.write(f'{value}: {count}\n')

