import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv('test_data_has_null.csv', encoding='cp949')

# Step 2: Remove rows with null values
df = df.dropna()
print(df)
# Step 3: Calculate the average of the columns you're interested in
# For example, if you want to calculate the average of the 'column_name' column:
average = df['column_name'].mean()

# Step 4: Calculate the absolute difference between each row's value and the average
df['difference'] = abs(df['column_name'] - average)

# Step 5: Sort the DataFrame by the 'difference' column in ascending order
df = df.sort_values(by='difference')

# Step 6: Take the top 10 rows from the sorted DataFrame
nearest_10_rows = df.head(10)

# Display the resulting DataFrame
# print(nearest_10_rows)
