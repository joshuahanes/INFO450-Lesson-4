import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sqlite3

conn = sqlite3.connect('project.db')

df_weather = pd.read_sql_query("SELECT * FROM WEATHER", conn)
df_weather['time'] = pd.to_datetime(df_weather['time'])

print(df_weather.head())
print(df_weather.describe())

ax = df_weather.plot(x='time', y='temperature_c', kind='line')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('temperature_plot.png')