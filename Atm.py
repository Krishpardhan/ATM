pin=1234
balance=1000
_pin=int(input("Please enter your pin number:"))
if(_pin==pin):
    while(True):
        print('''Welcome in our ATM App
1.Balance Enquiry
2.Cash Withdrawl
3.Cash Deposit
4.Money Transfer
5.Exit''')
        choice=int(input("Please Enter your Choice:"))
        if(choice==1):
            print("Your Balance is:",balance)
        elif(choice==2):
            amount=int(input("Enter the Amount:"))
            if(amount>balance):
                print("Balance Insufficient")
            else:
                balance=balance-amount
                print("Withdrawl successfully \n your remaining balance is:",balance)
        elif(choice==3):
            amount=int(input("Enter the amount:"))
            balance=amount+balance
            print("Your balance is:",balance)
        elif(choice==4):
            break
        else:
            print("Invalid Choice")
else:
    print("Invalid Pin")
