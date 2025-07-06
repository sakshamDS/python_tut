import random
imagined_number=random.randint(1,5)
users_number=0
while users_number!=imagined_number:
    users_number=int(input("enter a number between 1 to 5 "))
    if users_number==imagined_number:
        print("u got it right")
        break

    print("INCORECT!!! \n","TRY AGAIN")
    

