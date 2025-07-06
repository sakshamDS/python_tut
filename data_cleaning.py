import pandas as pd
import numpy as np

data = {
    'Name': ['sara', 'adam', 'sid', 'ram'],
    'Age': [23, np.nan, 56, np.nan],
    'City': ['delhi', np.nan, 'chennai', np.nan]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

missing_data = df.isnull()  #isnull() is used to check if the given data is missing or not 
print("\nmissig data:\n",missing_data)

df_dropped = df.dropna()
print("\nData after dropping the row with missing values :\n",df_dropped) #dropna() is used to drop the row with the missing values 

