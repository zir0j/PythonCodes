# Operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#What will be printed
print("Hello! Do you wanna do some math?")
initial_response = input("yes/no: ")
if initial_response == "yes":
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # Choices for the user
        choice = input("Enter choice(1/2/3/4): ")

        # Conditions and Outputs
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "/", num2, "=", divide(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", multiply(num1, num2))
      
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                print("Okay! See you next time!")
                break
        
        else:
            print("Invalid Input")

