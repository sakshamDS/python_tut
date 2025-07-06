import pandas as pd 
data = {'scores':[65,70,75,80,85]}#dictionary banai hai yaha pe

data_with_mode = {'scores':[65,65,75,80,85]}

df=pd.DataFrame(data)

mean_score = df['scores'].mean()#iss line pe hamara jo df hai scores wala uska mean calculate hoga aur ek variable mei sore ho jayega

median_score=df['scores'].median()

#MODE IS USEFULL FOR CATEGORICAL DATA

print(f"Mean score:{mean_score}")
print(f"Median score:{median_score}")