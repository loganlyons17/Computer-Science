# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd
import math

# Load in the data with read_csv()
co2_data = pd.read_csv("CO2/co2_data.csv", header=1)   # identify the header row
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
co2_data.dropna(subset=['Average'], inplace=True)

# Use matplotlib to make a line graph
plt.plot(co2_data['decimal_year'], co2_data['Average'], color='gray')
plt.ylabel('CO2 ppm')
plt.xlabel('Years')
plt.title('Carbon Dioxide')

# TODO #2: Calculate min, max, and avg anomaly and the corresponding min/max years
min_ppm = co2_data['Average'].iloc[0]
max_ppm = co2_data['Average'].iloc[0]

min_year = co2_data['decimal_year'].iloc[0]
max_year = co2_data['decimal_year'].iloc[0]

sum = 0

for i in range(len(co2_data['Average'])):
    if (co2_data['Average'].iloc[i] < min_ppm):
        min_ppm = co2_data['Average'].iloc[i]
        min_year = co2_data['decimal_year'].iloc[i]
    if (co2_data['Average'].iloc[i] > max_ppm):
        max_ppm = co2_data['Average'].iloc[i]
        max_year = co2_data['decimal_year'].iloc[i]
    sum += co2_data['Average'].iloc[i]


print(f"The maximum co2 was {max_ppm} ppm in {max_year}.")

print(f"The minimum co2 was {min_ppm} ppm in {min_year}.")

print(f"The average co2 was {round(sum / len(co2_data['Average']), 4)} ppm over {len(co2_data['Average'])} years.")

plt.show()