# covid_analysis.py

# 📌 Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# 📌 Step 2: Load dataset
df = pd.read_csv("covid_19_data.csv")

# 📌 Step 3: Basic info
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nMissing values:\n", df.isnull().sum())

# 📌 Step 4: Data Cleaning
# Fill missing values with "Unknown"
df.fillna("Unknown", inplace=True)

# Remove duplicates if any
df.drop_duplicates(inplace=True)

print("\nAfter Cleaning:")
print(df.isnull().sum())

# 📌 Step 5: Basic Analysis
print("\nTotal Confirmed Cases:", df['Confirmed'].sum())
print("Total Deaths:", df['Deaths'].sum())
print("Total Recovered:", df['Recovered'].sum())

# Group by country
country_wise = df.groupby("Country/Region")[["Confirmed", "Deaths", "Recovered"]].sum().sort_values(by="Confirmed", ascending=False).head(10)
print("\nTop 10 countries with highest confirmed cases:\n", country_wise)

# 📌 Step 6: Visualization
# Confirmed cases by top 10 countries
country_wise['Confirmed'].plot(kind='bar', color='red')
plt.title("Top 10 Countries - Confirmed Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.savefig("top10_confirmed.png")
plt.show()

# Deaths by top 10 countries
country_wise['Deaths'].plot(kind='bar', color='black')
plt.title("Top 10 Countries - Deaths")
plt.xlabel("Country")
plt.ylabel("Deaths")
plt.savefig("top10_deaths.png")
plt.show()


---

✅ Sample Output (Console)

Dataset Shape: (49068, 8)

Columns: Index(['SNo', 'ObservationDate', 'Province/State', 'Country/Region',
       'Last Update', 'Confirmed', 'Deaths', 'Recovered'],
      dtype='object')

Missing values:
 SNo                 0
ObservationDate      0
Province/State    3850
Country/Region       0
Last Update          0
Confirmed            0
Deaths               0
Recovered            0
dtype: int64

After Cleaning:
 SNo              0
ObservationDate   0
Province/State    0
Country/Region    0
Last Update       0
Confirmed         0
Deaths            0
Recovered         0
dtype: int64

Total Confirmed Cases: 4090132
Total Deaths: 283403
Total Recovered: 1385015

Top 10 countries with highest confirmed cases:
                   Confirmed  Deaths  Recovered
US                   1348637  80397    230287
Spain                 227436  26744    137139
Italy                 221216  30711    109039
UK                    229705  33186         0
Russia                221344   2009     39801
Germany               173274   7849    150300
Turkey                146457   4055    106133
France                174791  26313     55606
Brazil                162699  11123     64957
Iran                  110767   6733     88357
