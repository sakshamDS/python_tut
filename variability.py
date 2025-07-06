import pandas as pd
data = {'scores':[60,70,80,90,100]}

df=pd.DataFrame(data)

#range hogi max mei se min minus krke 

range_value=df['scores'].max() - df['scores'].min()
variance_value=df['scores'].var()
std_dev = df['scores'].std()


print(f"Range:{range_value}")
print(f'Variance:{variance_value}')
print(f'standard deviation:{std_dev}')
