import pandas as pd

# cpu_data = pd.read_csv('data-8-10-300-1d3.csv', names=['client_id', 'job_id', 'arrival_time', 'end_time', 'job_time', 'queue_time', 'total_time'])
df = pd.read_csv('data-8-10-300-1d3.csv')
df['arrival_time'] = pd.to_datetime(df['arrival_time'], unit='s')
print(df.head())
line = df.drop(['client_id', 'job_id', 'end_time'], axis=1).plot(x='arrival_time', y=['job_time', 'queue_time', 'total_time'])
fig = line.get_figure()
fig.savefig('cpu_load_figure.pdf')
