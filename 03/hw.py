import pandas as pd
import random
import matplotlib
matplotlib.use('agg')  # Use this backend or try 'Qt5Agg' if TkAgg doesn't work
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker

# Create the fake data
fake = Faker()
data = {"Neighborhood":[], "Price":[], "Occupancy":[], "Review_Score":[]}
for i in range(100):
    data["Neighborhood"].append(random.choice(["A", "B", "C", "D", "E"]))
    data["Price"].append(random.randint(100, 500))
    data["Occupancy"].append(random.randint(10, 100))
    data["Review_Score"].append(round(random.uniform(0, 5), 1))

# Create the dataframe
df = pd.DataFrame(data)

# Make heatmap using pivot_table
heatmap_data = df.pivot_table(index='Neighborhood', values='Occupancy', aggfunc='mean')

# Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm")
plt.title("Airbnb Data Heatmap")
plt.savefig("airbnb_heatmap.png")

# Create scatterplot between price and neighbourhood
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Neighborhood", y="Price", data=df)
plt.title("Airbnb Data Scatterplot")
plt.savefig("airbnb_scatterplot.png")

# Create hisplot between price and occupancy
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Price", y="Occupancy")
plt.title("Airbnb Data Histogram")
plt.savefig("airbnb_histogram.png")

# Create boxplot between price and review score
plt.figure(figsize=(10, 6))
sns.boxplot(x="Review_Score", y="Price", data=df)
plt.title("Airbnb Data Boxplot")
plt.savefig("airbnb_boxplot.png")

