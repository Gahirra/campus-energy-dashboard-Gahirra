import pandas as pd
import os

def load_data():
    files = os.listdir("data")
    all_data = []

    for file in files:
        if file.endswith(".csv"):
            try:
                df = pd.read_csv("data/" + file)
                df['building'] = file.replace(".csv", "")  
                all_data.append(df)
            except:
                print("File not found", file)

    combined = pd.concat(all_data, ignore_index=True)
    return combined

df = load_data()
print(df.head())

df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp')

def calculate_daily_totals(df):
    return df['kwh'].resample('D').sum()

def calculate_weekly_totals(df):
    return df['kwh'].resample('W').sum()

def building_summary(df):
    return df.groupby("building")['kwh'].agg(['mean', 'min', 'max', 'sum'])

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, mr):
        self.readings.append(mr)

    def total_consumption(self):
        return sum(r.kwh for r in self.readings)
    


import matplotlib.pyplot as plt

daily = calculate_daily_totals(df)
weekly = calculate_weekly_totals(df)
building_sum = building_summary(df)

fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# line chart
axs[0].plot(daily)
axs[0].set_title("Daily Consumption")

# bar chart
axs[1].bar(building_sum.index, building_sum['mean'])
axs[1].set_title("Average Weekly Usage Per Building")

# scatter plot
axs[2].scatter(df.index, df['kwh'])
axs[2].set_title("Peak Hour Scatter")

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()

df.to_csv("cleaned_energy_data.csv")
building_sum.to_csv("building_summary.csv")

total = df['kwh'].sum()
highest = building_sum['sum'].idxmax()

with open("summary.txt", "w") as f:
    f.write(f"Total Campus Consumption: {total}\n")
    f.write(f"Highest Consuming Building: {highest}\n")

