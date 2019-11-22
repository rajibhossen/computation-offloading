import pandas as pd

# df = pd.read_csv('average_job_time.csv')
# # df['arrival_time'] = pd.to_datetime(df['arrival_time'], unit='s')
# print(df.head())
# line = df.drop(['twentyfour'], axis=1).plot(x='jobs_per_sec', y=['eight', 'sixteen', 'thirtytwo', 'sixtyfour'])
# fig = line.get_figure()
# fig.savefig('jobtime-workers.png')

df = pd.read_csv('average_queue_time.csv')
# df['arrival_time'] = pd.to_datetime(df['arrival_time'], unit='s')
print(df.head())
line = df.drop(['twentyfour'], axis=1).plot(x='jobs_per_sec', y=['eight', 'sixteen', 'thirtytwo', 'sixtyfour'])
fig = line.get_figure()
fig.savefig('queuetime-workers.png')