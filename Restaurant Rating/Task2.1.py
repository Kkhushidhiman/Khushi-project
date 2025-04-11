#T A S K  2
print("\n \n \n TASK 2")
#RESTAURANTS RATINGS 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Khushi\Downloads\Dataset .csv")

print(df.head())

print(df.columns)


#ANALYZE THE DISTRIBUTION OF AGGREGATE RATINGS AND DETERMINE THE MOST COMMON RANGE.

aggregate_ratings = df['Aggregate rating'].value_counts()
print(aggregate_ratings)

print(aggregate_ratings.idxmax())

# CALCULATE THE AVERAGE NUMBER OF VOTES BY EVERY RESTAURANTS 

avg_vote = round(df['Votes'].mean(),3)
print("\n The average number of votes :",avg_vote)





