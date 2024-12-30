#****DATA PRE-PROCESSING****
# Step 1: Import required libraries 
import pandas as pd

# Step 2: Loading dataset into a pandas DataFrame 
df = pd.read_csv('obesity_factors.csv')  

# Step 3: Filter the data for the years 2018 to 2023
# We are only interested in data between 2018 and 2023
df_filtered = df[df['YearStart'].between(2018, 2023)]
# Step 4: Define the columns we want to retain
columns_to_keep = ['YearStart', 'LocationDesc', 'Class', 'Data_Value', 
                   'Sample_Size', 'StratificationCategory1', 'Stratification1']

# Step 5: Create a new DataFrame with only the relevant columns
processed_data = df_filtered[columns_to_keep]

# Step 6: Remove rows with any empty (NaN) values
df_cleaned = processed_data.dropna()

# Step 7: Perform random sampling
sample_size = 4082  # i am taking 10% of my cleaned data of 40.8k data

# Randomly sample 'sample_size' rows
df_sampled = df_cleaned.sample(n=sample_size, random_state=42)

# Step 8: Check the first few rows of the sampled data
print(df_sampled.head())

# Step 9: Save the sampled data to a new CSV file
df_sampled.to_csv('sampled_data.csv', index=False)
