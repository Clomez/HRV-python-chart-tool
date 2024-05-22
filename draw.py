import json
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Read the stats from the file
with open('stats.json', 'r') as f:
    stats = json.load(f)

# Extract startTimes, averages, and medians
start_times = [datetime.fromisoformat(stat['startTime']) for stat in stats]
averages = [stat['avg'] for stat in stats]
medians = [stat['median'] for stat in stats]

# Plot the average data
plt.plot(start_times, averages, marker='o', label='Average Values', color='blue')

# Calculate the trend line for averages (using numpy polyfit for a linear fit)
trend_avg = np.polyfit([t.timestamp() for t in start_times], averages, 1)
trend_line_avg = np.poly1d(trend_avg)

# Plot the trend line for averages
trend_avg_values = trend_line_avg([t.timestamp() for t in start_times])
plt.plot(start_times, trend_avg_values, 'r-', label='Trend Line (Avg)')

# Annotate the start and end points of the trend line
plt.annotate(f'{trend_avg_values[0]:.2f}', xy=(start_times[0], trend_avg_values[0]), xytext=(start_times[0], trend_avg_values[0] + 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, color='red')
plt.annotate(f'{trend_avg_values[-1]:.2f}', xy=(start_times[-1], trend_avg_values[-1]), xytext=(start_times[-1], trend_avg_values[-1] + 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, color='red')

# Plot the median data
plt.plot(start_times, medians, marker='x', label='Median Values', color='green')

# Calculate the trend line for medians (using numpy polyfit for a linear fit)
trend_median = np.polyfit([t.timestamp() for t in start_times], medians, 1)
trend_line_median = np.poly1d(trend_median)

# Plot the trend line for medians
plt.plot(start_times, trend_line_median([t.timestamp() for t in start_times]), 'orange', label='Trend Line (Median)')

# Add titles and labels
plt.title('HRV Samples Over Time with Trend Lines')
plt.xlabel('Time')
plt.ylabel('HRV Sample Value')

# Add a legend
plt.legend()

# Add gray horizontal lines every 5 units
plt.yticks(np.arange(0, max(max(averages), max(medians)) + 5, 5))
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, color='gray')

# Format the x-axis to show date and time
plt.gcf().autofmt_xdate()

# Show the plot
plt.show()
