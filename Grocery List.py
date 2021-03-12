import pandas as pd
budget=int(input("Please enter your bduget: "))
item_name=[]
item_Quantity=[]
item_price=[]
left_ammount=budget
def addItem():
    print("Enter product : ")
    item=input()
    item_name.append(item)
    print('Enter quantity :')
    item_Quantity.append(float(input()))
    print('Enter Price :')
    price=int(input())
    global left_ammount
    if left_ammount>price:
        item_price.append(price)

        left_ammount=left_ammount-price
    else:
        print(f"Can't Buy the product ###(because budget left is {left_ammount}) ")
        item_name.pop()
        item_Quantity.pop()

def mainMenu():
    print('1.Add an item')
    print('2.Exit')
    choice=int(input('Enter your choice :'))
    return choice
choice=mainMenu()

while(True):
    if choice==1:
        addItem()
        choice=mainMenu()
    elif  choice==2:
        print('Amount left can buy you wheat')
        df=pd.DataFrame({'item':item_name,'Quantity':item_Quantity,'Price':item_price})
        print(df)
        break
    else:
        print('Invalid Input Try another input :')






