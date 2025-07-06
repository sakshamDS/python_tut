import pandas as pd

# Replace 'your_dataset.csv' with your actual file name
df = pd.read_csv('global_energy_consumption copy.csv') 

import pandas as pd

# Replace 'your_dataset.csv' with your actual file name
df = pd.read_csv('global_energy_consumption copy.csv')


# Check if there are any missing values in the entire dataset
total_missing = df.isnull().values.any()
print("\nAre there any missing values in the dataset?")
print(total_missing)  # Will print True if there are missing values, False otherwise

def filter_countries_by_consumption(df, threshold, above=True):
    """
    Filter countries based on total energy consumption.
    
    Parameters:
    - df: DataFrame containing the energy data
    - threshold: The energy consumption threshold in TWh
    - above: If True, returns countries above threshold; if False, returns below
    
    Returns:
    - Filtered DataFrame
    """
    if above:
        filtered = df[df['Total Energy Consumption (TWh)'] >= threshold]
    else:
        filtered = df[df['Total Energy Consumption (TWh)'] < threshold]
    
    # Get unique countries (in case there are multiple entries per country)
    unique_countries = filtered['Country'].unique()
    
    return unique_countries, filtered

# Example usage:
# Filter countries with consumption above 7000 TWh
high_consumption_countries, high_df = filter_countries_by_consumption(df, 7000, above=True)
print("Countries with high energy consumption (>7000 TWh):", high_consumption_countries)

# Filter countries with consumption below 5000 TWh
low_consumption_countries, low_df = filter_countries_by_consumption(df, 5000, above=False)
print("Countries with low energy consumption (<5000 TWh):", low_consumption_countries)


