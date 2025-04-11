#CUISINE COMBINATION
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Khushi\Downloads\Dataset .csv")

print(df.head())

print(df.columns)

#IDENTIFY THE MOST COMMON CUISINE COMBINATION.

common_combination = df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
top10 = common_combination.head(10)
print("Top 10 most common :",top10)


#DETERMINE IF CERTAIN CUISINE COMBINATIONS TEND TO HAVE HIGHER RATINGS.
high_ratings = common_combination.iloc[0]
print("MAX RATING is :",high_ratings)