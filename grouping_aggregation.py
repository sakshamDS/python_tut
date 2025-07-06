import pandas as pd 
data = {'scores':[65,70,75,80,85]}#dictionary banai hai yaha pe 
df=pd.DataFrame(data)

mean_score = df['scores'].mean()#iss line pe hamara jo df hai scores wala uska mean calculate hoga aur ek variable mei sore ho jayega


print(f"Mean score:{mean_score}")