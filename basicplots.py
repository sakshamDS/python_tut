import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014]
sales = [100, 1110, 200, 250, 300]

plt.plot(years, sales, 
         marker='o',      # 'o' for circles (not '0')
         linestyle='',  # '--' for dashed line (not '_')
         color='red')    # Correct color specification

plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)

plt.show()