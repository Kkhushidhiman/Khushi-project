import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Khushi\Downloads\Dataset .csv")

print(df.head())

print(df.columns)

#city analysis
city_count = df['City'].value_counts()
restaurant_no = city_count.head(1)
print("\n City with highest no of restaurants :",city_count.idxmax())
print(restaurant_no)


#Calucate the average rating for restaurants.
rating_of_cities = df.groupby('City')['Aggregate rating'].mean()
print("\n average rating :",rating_of_cities )


#Highest average rating.
average_rating = df.groupby('City')['Aggregate rating'].mean()
print(average_rating.head(1))
