import pandas as pd 

data={
    'name':["sara","shubhman","yuzi"],
    'colour':["red","green","yellow"],
    'class':[1,2,3]
}

df=pd.DataFrame(data)
print("pandas DataFrame:\n",df)