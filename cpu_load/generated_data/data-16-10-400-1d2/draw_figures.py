import pandas as pd

df = pd.read_csv('data-16-10-400-1d2.csv')
# df['arrival_time'] = pd.to_datetime(df['arrival_time'], unit='s')
print(df.head())
line = df.drop(['twentyfour'], axis=1).plot(x='jobs_per_sec', y=['eight', 'sixteen', 'thirtytwo', 'sixtyfour'])
fig = line.get_figure()
fig.savefig('jobtime-workers.png')


