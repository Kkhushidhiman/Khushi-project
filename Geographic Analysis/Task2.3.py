#GEOGRAPHIC ANALYSIS.
import folium.map
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

df = pd.read_csv(r"C:\Users\Khushi\Downloads\Dataset .csv")

print(df.head())

print(df.columns)

#PLOT THE LOCATIONS OF RESTAURANTS ON A MAP USING LONGITUDE AND LATITUDE.

avg_lat = df['Latitude'].mean()
avg_lon = df['Longitude'].mean()
restaurant_map = folium.Map(location=[avg_lat, avg_lon], zoom_start=12)

# Add restaurant locations to the map
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Restaurant Name']}",
        icon=folium.Icon(icon='info-sign')
    ).add_to(restaurant_map)

# Save the map to an HTML file
restaurant_map.save('restaurants_map.html')

print("Map has been saved as 'restaurants_map.html'.")

#IDENTIFY ANY PATTERNS OR CLUSTERS OF RESTAURANTS IN SPECIFIC AREAS.
map = folium.Map(location = [df['Latitude'].mean(),df['Longitude'].mean()],zoom_start= 1,height = '100%', width ='100%')

heat = [[row['Latitude'],row['Longitude']] for i,row in df.iterrows()]
HeatMap(heat,radius = 10).add_to(map)

map

