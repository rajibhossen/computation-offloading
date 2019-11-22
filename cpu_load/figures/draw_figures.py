import pandas as pd

# df = pd.read_csv('average_job_time.csv')
# # df['arrival_time'] = pd.to_datetime(df['arrival_time'], unit='s')
# print(df.head())
# line = df.drop(['twentyfour'], axis=1).plot(x='jobs_per_sec', y=['eight', 'sixteen', 'thirtytwo', 'sixtyfour'])
# fig = line.get_figure()
# fig.savefig('jobtime-workers.png')


# df = pd.concat([
#     pd.read_csv('average_job_time.csv'),
#     pd.read_csv('average_queue_time.csv')
# ])
#
# result=df.groupby('jobs_per_sec', as_index=False).sum()
#
# result.to_csv('average_service_time.csv')

df = pd.read_csv('average_service_time.csv')
# df['arrival_time'] = pd.to_datetime(df['arrival_time'], unit='s')
print(df.head())
line = df.drop(['twentyfour'], axis=1).plot(x='jobs_per_sec', y=['eight', 'sixteen', 'thirtytwo', 'sixtyfour'], ylim=(0,20))
fig = line.get_figure()
fig.savefig('servicetime-workers.png')