import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Khushi\Downloads\Dataset .csv")

print(df.head())

print("\n Task 3")
#Price Range Distribution

print(df.columns)

df.hist(column="Price range")
plt.title('Distribution of range')
plt.xlabel('Price range')
plt.ylabel('Counts')
plt.show()

#Calculate the percentage of restaurants at each price range category.

price_range_counts = df['Price range'].value_counts()
price_range_percentages = (price_range_counts/price_range_counts.sum())*100
print(price_range_percentages)