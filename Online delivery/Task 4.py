import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Khushi\Downloads\Dataset .csv")

print(df.head())

print("T A S K 4 ")
#ONLINE DELIVERY


#DETERMINE THE PERCENTAGE OF RESTAURANTS THAT OFFER ONLINE DELIVERY.

online_delivery = df['Has Online delivery'].value_counts().get('Yes',0)
print(" Number of restaurants with online delivery \n : ",online_delivery)

rows = len(df)
percentage_of_online_delivery = round((online_delivery/rows)*100)
print("Total percentage of online delivery \n\n :",percentage_of_online_delivery)

#COMPARE THE AVERAGE RATINGS OF RESTAURANTS WITH AND WITHOUT ONLINE DELIVERY.
compare_avg_rating = df.groupby('Has Online delivery')['Aggregate rating'].mean()
print(compare_avg_rating)