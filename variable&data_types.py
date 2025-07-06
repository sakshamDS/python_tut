starter=float(input("enter  starter price"))
main_course=float(input("enter main course price"))
dessert=float(input("enter dessert price"))

total=float(starter+main_course+dessert)
tax=total*0.18

print("your total without tax is ",total,"$\n","and with tax is ",tax,"$")
