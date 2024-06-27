def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("Division not possible as y=0.")
    else:
        return a/b
    
def menu():
    print("Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main():
    while True:
        menu()
        choice=int(input("Enter the operation: "))
            
        if (choice == 1 or choice == 2 or choice == 3 or choice == 4):
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
        else:
            exit()

            
        if(choice == 1):
            sum_ = add(a,b)
            print(a, ' + ', b, ' = ', add(a,b))
                
        elif(choice == 2):
            diff = subtract(a,b)
            print(a, ' - ', b, ' = ', subtract(a,b))
                
        elif(choice == 3):
            prod = multiply(a,b)
            print(a, ' * ', b, ' = ', multiply(a,b))
                
        elif (choice == 4):
            quo = divide(a,b)
            print(a, ' / ', b, ' = ', divide(a,b))
                
        elif(choice == 5):

            x=input("Y/N")
            if (x in 'Yy'):
                print("Exiting the calculator")
                break
            else:
                continue
        else:
            print("Entered choice is invalid. Please enter a valid option.")
            
main()
    
    
    
