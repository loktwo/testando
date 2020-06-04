#!/bin/python3
#pqp irmao

class calc():

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b
        
    def div(a,b):
        return self.a / self.b

a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
obj = calc(a,b)

choice = 1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", obj.div())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()
