import pandas as pd

# Load the data from the CSV file into a Pandas DataFrame
df = pd.read_csv('output_data.csv')

# List the column names
column_names = df.columns

print("Column names in the DataFrame:", column_names)

