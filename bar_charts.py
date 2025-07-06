import matplotlib.pyplot as plt

product = ['A', 'B', 'C', 'D']
sales = [10, 20, 30, 40]

plt.pie(
    sales, 
    labels=product, 
    autopct='%1.1f%%', 
    colors=['red', 'green', 'pink', 'yellow']
)
plt.title('Product Sales')
plt.show()
