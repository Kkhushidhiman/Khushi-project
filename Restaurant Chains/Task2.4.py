#Task 4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Khushi\Downloads\Dataset .csv")

print(df.head())

res_chain = df.groupby("Restaurant Name").size().reset_index(name = "Chain Count")
res_chain = res_chain[res_chain["Chain Count"]>1]
res_chain = res_chain.sort_values(by='Chain Count',ascending=False)
print(res_chain[["Restaurant Name","Chain Count"]].head(10))


plt.bar(res_chain["Restaurant Name"][:10],res_chain["Chain Count"][:10])
plt.xlabel("restaurant chain")
plt.ylabel("No of outlet")
plt.title("top 10 restaurant chains by number of outlet")
plt.show()


# ANALYZE THE RATINGS AND POPULARITY OF DIFFERENT RESTAURANTS CHAINS.


