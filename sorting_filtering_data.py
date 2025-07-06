import pandas as pd 
data = {'Name':['Alice','Bob','Charlie','David'],
        'Age':[24,19,23,30],
        'Score':[85,90,89,95]}

df=pd.DataFrame(data)
sorted_df= df.sort_values(by='Age')
print("Sorted by Age :\n",sorted_df)

filtererd_df=df[df['Score']>90]
print("the filtered data is:\n",filtererd_df)