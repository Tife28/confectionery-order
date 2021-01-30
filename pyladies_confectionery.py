# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:36:58 2020
@author: Tife
"""
import sys

def inventory():
    print("Welcome Admin!, please create your menu.")
    foodMenu = []
    Price = []
    Quantity = []
    while True:
        foodmenu = str(input("\n Enter food type: "))
        price = int(input("\n Enter price of stock: N"))
        quantity = int(input("\n Enter quantity available: "))
                
        foodMenu.append(foodmenu)
        Price.append(price)
        Quantity.append(quantity)

        print(foodMenu)
        print(Price)
        print(Quantity)
        menu_length = len(foodMenu)
        
        print('Do you want to add new items to store?')
        answer = input("Enter 'y' for Yes and 'n' for No: ")
        if answer == "y":
            continue
        else:
            print("Continuing...")
            break
    print("The following are available: ")
    print("=================================================")
    print('FOOD MENU\tPRICE (N)\tQUANTITY')
    print("=================================================")
    for x in range(menu_length):
        print(foodMenu[x] +"\t" + str(Price[x]) + "\t\t" + str(Quantity[x]) + " piece(s)")
        print('----------------------------------------------')
    print('{0:=^50}'.format('End of List'))
      
def customer():  
    foodMenu = ['Cake', 'Pizza', 'Salad', 'Sndwich', 'Pancake']
    Price = [400, 4000, 321, 564, 200]
    Quantity = [774, 323, 432, 232, 5342]
    menu_length = len(foodMenu)
    Purchase = []
    purchase_length = len(Purchase)
        
    name = str(input("\n Please enter your name: "))
    print("Hello " + name + "! WELCOME TO PYLADIES CONFECTIONERY.") 
    while True:
        print("The following are available: ")
        print("=================================================")
        print('FOOD MENU\tPRICE ($)\tQUANTITY IN STOCK')
        print("=================================================")
        for x in range(menu_length): 
            print(foodMenu[x] +"\t\t"+ str(Price[x]) + " \t\t" + str(Quantity[x]) + " piece(s)")
            print('----------------------------------------------')
        print('{0:=^50}'.format('End of List'))
        print("Please make your order(s)")
        foodmenu = str(input("\n What will you like to order: "))
        if foodmenu == foodMenu[0]:
            quantity = int(input("\n Enter quantity of order: "))
            if quantity <= Quantity[0]:
                print("You ordered " + str(quantity) + " " + foodmenu +"(s) at N" + str(Price[0]) + " each")
                Quantity[0] = Quantity[0] - quantity
                purchase = quantity * Price[0]
                Purchase.append(purchase)
                print("Will you like to order something else?")
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    print("Continuing...")
                    break
            else:
                print("Sorry, only " + str(Quantity[0]) + " piece(s) are available.")
                print("Will you like to order something else?")
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    if purchase_length == 0:
                        sys.exit("Thank you for stopping by " + name + ", we hope you love our services. Do well to visit us again.")
                    else:
                        print('Continuing...')
                        break  
        elif foodmenu == foodMenu[1]:
            quantity = int(input("\n Enter quantity of order: "))
            if quantity <= Quantity[1]:
                print("You ordered " + str(quantity) + " " + foodmenu +"(s) at N" + str(Price[1]) + " each")
                Quantity[1] = Quantity[1] - quantity
                purchase = quantity * Price[1]
                Purchase.append(purchase)
                print("Will you like to order something else?")
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    print("Continuing...")
                    break
            else:
                print("Sorry, only " + str(Quantity[1]) + " piece(s) are available.")
                print("Will you like to order something else?")
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    if purchase_length == 0:
                        sys.exit("Thank you for stopping by " + name + ", we hope you love our services. Do well to visit us again.")
                    else:
                        print('Continuing...')
                        break  
        elif foodmenu == foodMenu[2]:
            quantity = int(input("\n Enter quantity of order: "))
            if quantity <= Quantity[2]:
                print("You ordered " + str(quantity) + " " + foodmenu +"(s) at N" + str(Price[2]) + " each")
                Quantity[2] = Quantity[2] - quantity
                purchase = quantity * Price[2]
                Purchase.append(purchase)
                print("Will you like to order something else?")  
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    print("Continuing...")
                    break
            else:
                print("Sorry, only " + str(Quantity[2]) + " piece(s) are available.")
                print("Will you like to order something else?")
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    if purchase_length == 0:
                        sys.exit("Thank you for stopping by " + name + ", we hope you love our services. Do well to visit us again.")
                    else:
                        print('Continuing...')
                        break  
        elif foodmenu == foodMenu[3]:
            quantity = int(input("\n Enter quantity of order: "))
            if quantity <= Quantity[3]:
                print("You ordered " + str(quantity) + " " + foodmenu +"(s) at N" + str(Price[3]) + " each")
                Quantity[3] = Quantity[3] - quantity
                purchase = quantity * Price[3]
                Purchase.append(purchase)
                print("Will you like to order something else?")
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    print("Continuing...")
                    break
            else:
                print("Sorry, only " + str(Quantity[3]) + " piece(s) are available.")
                print("Will you like to order something else?")
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    if purchase_length == 0:
                        sys.exit("Thank you for stopping by " + name + ", we hope you love our services. Do well to visit us again.")
                    else:
                        print('Continuing...')
                        break  
        elif foodmenu == foodMenu[4]:
            quantity = int(input("\n Enter quantity of order: "))
            if quantity <= Quantity[4]:
                Quantity[4] = Quantity[4] - quantity
                purchase = quantity * Price[4]
                Purchase.append(purchase)
                print("You ordered " + str(quantity) + " " + foodmenu +"(s) at N" + str(Price[4]) + " each")
                print("Will you like to order something else?")
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    print("Continuing...")
                    break 
            else:
                print("Sorry, only " + str(Quantity[4]) + " piece(s) are available.")
                print("Will you like to order something else?")
                answer = input("Enter 'y' for Yes and 'n' for No: ")
                if answer == "y":
                    continue
                else: 
                    if purchase_length == 0:
                        sys.exit("Thank you for stopping by " + name + ", we hope you love our services. Do well to visit us again.")
                    else:
                        print('Continuing...')
                        break  
        else:
            print("Sorry, we are out of stock. Please check back later.")
            print("Will you like to order something else?")
            answer = input("Enter 'y' for Yes and 'n' for No: ")
            if answer == "y":
                continue
            else: 
                if purchase_length == 0:
                    sys.exit("Thank you for stopping by " + name + ", we hope you love our services. Do well to visit us again.")
                else:
                    print('Continuing...')
                    break  
    print("============================================================")
    print('\n PYLADIES CONFECTIONERY\t\t\t\tRECEIPT')
    print('------------------------------------------------------------')
    print("Your purchase(s) cost(s)\t\t\t N" + str(sum(Purchase)))
    print('------------------------------------------------------------')
        
    if purchase >= 1000:
        amount = (5 * sum(Purchase)) / 100
        amount1 = (20 * sum(Purchase)) / 100
        amount2 = sum(Purchase) - amount1 + amount
        print("5% VAT on purchase(s)\t\t\t\t N" + str(amount))
        print('------------------------------------------------------------')
        print("20% Discount on purchase(s)\t\t\t N" + str(amount1))
        print('------------------------------------------------------------')
        print("Total amount is \t\t\t\t N" + str(amount2))
        print('------------------------------------------------------------')
        print("Thank you for stopping by " + name + ", we hope you love our services.") 
        print('{0:=^65}'.format('Do well to visit us again.'))
    elif purchase >= 500 :
        amount = (5 * sum(Purchase)) / 100
        amount1 = sum(Purchase) + amount
        print("5% VAT on purchase(s)\t\t\t\t N" + str(amount))
        print('------------------------------------------------------------')
        print("Total amount is\t\t\t\t\t N " + str(amount1))
        print('------------------------------------------------------------')
        print("Thank you for stopping by " + name + ", we hope you love our services.")
        print('{0:=^65}'.format('Do well to visit us again.'))
    else:
        print("Thank you for stopping by " + name + ", we hope you love our services.")
        print('{0:=^65}'.format('Do well to visit us again.'))
       
customer()