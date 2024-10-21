def calculator():

    def calculator_inputs():
        while True:
            try:
                x = float(input("Enter first number: "))  # Get first number
                y = float(input("Enter second number: "))  # Get second number
                calculator_menu(x, y)  # Pass inputs to menu
                break  # Exit the loop after one round of inputs and operations
            except ValueError:
                print("Invalid input. Try again.")
    
    def calculator_menu(x, y):
        while True:
            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("0. Exit")
            
            try:
                user_input = int(input("\nEnter your choice: "))  # Get operation choice
                
                if user_input == 1:
                    print(f"The sum of {x} and {y} is {addition(x, y)}")
                elif user_input == 2:
                    print(f"The difference between {x} and {y} is {subtraction(x, y)}")
                elif user_input == 3:
                    print(f"The product of {x} and {y} is {multiplication(x, y)}")
                elif user_input == 4:
                    quotient, remainder = division(x, y)
                    print(f"The quotient of {x} and {y} is {quotient} and the remainder is {remainder}")
                elif user_input == 5:
                    print(f"{x} raised to {y} is {exponentiation(x, y)}")
                elif user_input == 0:
                    return  # Exit the menu, terminating the program
                else:
                    print("Invalid choice. Try again.")
                
            except ValueError:
                print("Invalid input. Please enter a valid choice.")
    
    def addition(x, y):
        return x + y

    def subtraction(x, y):
        return x - y

    def multiplication(x, y):
        if x == 0 or y == 0:
            return 0
        product = 0
        for _ in range(int(y)):  # Loop b times
            product = addition(product, a)
        return product

    def division(x, y):
        if y == 0:
            return "undefined", 0  # Handle division by zero
        quotient = 0
        while x >= y:
            x = subtraction(x, y)
            quotient += 1
        remainder = x  # The leftover a is the remainder
        return quotient, remainder

    def exponentiation(x, y):
        if y == 0:
            return 1  # Any number raised to power 0 is 1
        result = x
        for _ in range(int(y) - 1):  # Loop b-1 times
            result = multiplication(result, x)
        return result

    calculator_inputs()  # Start the calculator


calculator()
