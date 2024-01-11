import pandas as pd

### Import Data
# df = dataframe
df = pd.read_csv('pokemon_data.csv')

print(df.head(3))
print(df.tail(3))

### Read Headers
cols = df.columns

## Read Each Column
print(cols)
print(df[[cols[1],cols[2]]])

## Read Each Row
# iloc = integer location
print(df.iloc[0:2])
print(df.loc[df['Type 1'] == "Fire"]) # finding specific data

# get the data as single objects as opposed to a list
for index, row in df.iterrows():
    print(index, row)

## Read a specific location
# from item at index 2 get column 1 val
print(df.iloc[2,1])