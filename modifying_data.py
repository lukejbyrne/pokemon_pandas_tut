import pandas as pd

### Import Data
# df = dataframe
df = pd.read_csv('pokemon_data.csv')

# Create new column in data frame
df['Total'] = df['HP'] + df['Attack'] + df['Defense']

print(df)