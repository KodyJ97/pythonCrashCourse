import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, highs, and lows temperatures from file.
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)

# Plot Data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, low, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)

# Below draws date labels diagonally to prevent overlap.
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

first_date = datetime.strptime('2018-7-1', '%Y-%m-%d')
print(first_date)
plt.show()
