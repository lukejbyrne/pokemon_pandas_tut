import pandas as pd

### Import Data
# df = dataframe
df = pd.read_csv('pokemon_data.csv')

# Create new column in data frame
df['Total1'] = df['HP'] + df['Attack'] + df['Defense']
df['Total2'] = df.iloc[:, 4:10].sum(axis=1) # Integer location, where : = all rows, axis = 1 sums horizontally

# Drop a column
df = df.drop(columns=['Total1'])

# Move col Total2
cols = list(df.columns)
new_cols = cols[0:4] + [cols[-1]] + cols[4:12]
df = df[new_cols]

print(df.head(5))

# Save modified df to CSV
df.to_csv('modified.csv', index=False)