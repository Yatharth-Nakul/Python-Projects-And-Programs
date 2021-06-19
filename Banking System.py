import random
class bank:

    def __init__(self,record):
        self.record = record


    def display(self):
        p = int(input("Enter Your Pin : "))
        if p in self.record.keys() :
            print("Account Holder Name :",self.record[p][0])
            print("Account Balance : Rs.",self.record[p][1])
            print("Account Type : ", self.record[p][2])
        else:
            print("Invalid Pin")


    def create(self):
        while True:
            n = input("Enter Your Name : ")
            if n.isalpha():

                a = int(input("Enter Your Age : "))
                if(a>17):
                    x="Major"
                else:
                    x="Minor"

                while True:
                    p = int(input("Create Your Pin : "))
                    if p not in self.record.keys():
                        self.record[p] = [n, 0, x]
                        break
                    elif p in self.record.keys() :
                        print("Select a Different Pin")
                print("Account Created Successfully")
                break

            else:
                print("Name must not contain integer or special characters..")


    def deposite(self):
        p = int(input("Enter Your Pin : "))
        if p in self.record:
            m = int(input("Enter The Amount : "))
            self.record[p][1] += m
            print("Balance Updated :",self.record[p][1])


    def withdraw(self):
        p = int(input("Enter Your Pin : "))
        if p in self.record:
            m = int(input("Enter The Amount : "))
            if (m <= self.record[p][1]):
                self.record[p][1] -= m
                print("Balance Updated :", self.record[p][1])
            else:
                print("Not Enough Balance.. ")


    def calc_si(self):
        p = int(input("Enter Your Pin : "))
        if p in self.record:
            m = int(input("Enter The Amount : "))
            if (m <= self.record[p][1]):
                r = random.randint(1,10)
                t = int(input("Enter Time Period : "))
                si = (m*r*t)/100
                a = m+si
                print("You'll get Rs.{} at {}% rate in {} years. ".format(a,r,t))

            else:
                print("Not Enough Balance.. ")

    def calc_ci(self):
        p = int(input("Enter Your Pin : "))
        if p in self.record:
            m = int(input("Enter The Amount : "))
            if (m <= self.record[p][1]):
                r = random.randint(1,10)
                t = int(input("Enter Time Period : "))
                ci = round(m*((1+(r/100))**t),2)
                print("You'll get Rs.{} at {}% rate in {} years. ".format(ci,r,t))

            else:
                print("Not Enough Balance.. ")


def execute():

    record={}
    obj = bank(record)

    print("******************************")
    print("=====WELCOME TO THE BANK!=====")
    print("Your Money Is Safe With Us")
    print("******************************")

    print("WHAT YOU WANNA DO ? (from 1 - 6)")

    while True:
        print("\n1. Display Account Details \n2. Create Account\n3. Deposite Money\n4. Withdraw Money\n5. Simple Interest Calculator\n6. Compound Interest Calculator\n7. Exit")
        try:
            choice = int(input("Enter your choice :"))
            if choice == 7:
                print("Have a nice day!")
                break
            elif choice == 1:
                obj.display()
            elif choice == 2:
                obj.create()
            elif choice == 3:
                obj.deposite()
            elif choice == 4:
                obj.withdraw()
            elif choice == 5:
                obj.calc_si()
            elif choice == 6:
                obj.calc_ci()

            else:
                print("CHOICE OUT OF RANGE! CHOOSE FROM 1-7")

        except ValueError as e:
            print("PLEASE ENTER A VALID INTEGER !!")

execute()