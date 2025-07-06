import matplotlib.pyplot as plt
import numpy as np


#plt.subplot(1,2,1)#1st row , 2nd col , 1 subplot 
#plt.plot(x,y)


#plt.subplot(1,2,2)#2nd subplot
#plt.bar(x,y)

#plt.show( )

fig,ax=plt.subplots(1,2,figsize=(10,5))

x=[1,2,3,4]
y=[10,15,20,25]

ax[0].plot(x,y)
ax[0].set_title('line chart')

ax[1].bar(x,y)
ax[1].set_title('bar chart')

plt.savefig('/Users/sakshamdidi/Desktop/Python_tutorial/plot.pdf', ...)


plt.tight_layout()
plt.show()