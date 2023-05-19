# This program allows the user to perform arithmetic operations on two numbers, and can also read in equations from a file.

# Provide information and introduce the program
print("Welcome to The Calculator")
print("The Calculator can help you perform basic arithmetic calculations, such as addition, subtraction, multiplication, and division.")
print("To perform a calculation, enter two numbers and an operation symbol (+,-,*,/) and the program will calculate the result." )
print("To read equations from a file, select option 2 from the menu and enter the file name.")

# The program presents the user with a simple menu, and prompts the user for their choice. 
# Depending on the user's choice, the program will either ask for two numbers and an operation, or read in equations from a file. 
while True:    
    print("\nPlease choose What do you want to do:")
    print("\tEnter 1: for Calculating two numbers")
    print("\tEnter 2: to read all of the equations from a txt file")
    print("\tEnter 3: to exit")
    try:
        # Validate user input for program choice
        program_choice = int(input("\tEnter Your choice (1,2,3): "))
        VALID_CHOICES = [1, 2, 3]
        if program_choice not in VALID_CHOICES : 
            raise ValueError
        elif program_choice == 3 :
            print("Thank you for using The Calculator ")
            break
    
        # Run the calculation program
        else:
            if program_choice == 1:
                print("\nYou have chosen to calculate two numbers.")                  
                operation_symbols=["+","-","*","/"]
                while True:
                    try:
                        # Loop the program till the user enter N 
                        repeat = input("\nTo proceed enter\"y\". To go back to menue enter \"N\"? : ").lower()           
                        if repeat == "y":
                            while True:
                                try:
                                    # Validate user input for first number
                                    user_number1 = float(input("\tEnter the first number you'd like to calculate: "))
                                    
                                    # Validate user input for operation symbol
                                    while True :
                                        try:
                                            user_operation = input("\tEnter the operation symbol \"+,-,*,/\" : ")
                                            if user_operation in operation_symbols:
                                                break
                                            else:
                                                raise Exception   
                                        
                                        except Exception:
                                            print("Invalid operation symbol. Please enter a valid operation symbol using only +, -, *, or /.") 
                                            continue     
                                
                                # Validate user input for second number
                                    while True: 
                                        try:                            
                                            user_number2 = float(input("\tEnter the second number, please: "))
                                            break # break the loop if the input is valid
                                        
                                        except ValueError:  # Handle non-numeric input by the user
                                            print("Invalid input. Please enter a valid number, using only digits and a decimal point.")
                                            continue
                                                        
                                    # Calculate numbers
                                    if user_operation == "+" :
                                        calculation_result = user_number1 + user_number2
                                       
                                    if user_operation == "-" :
                                        calculation_result = user_number1 - user_number2
                                       
                                    if user_operation == "*" :
                                        calculation_result = user_number1 * user_number2
                                        
                                    if user_operation == "/" :
                                        calculation_result = user_number1 / user_number2
                                       
                                    print("\n\tThe calculation result is: ", calculation_result)
                                    
                                    # Write equation to a file
                                    equation = str(user_number1) +" "+ user_operation +" "+ str(user_number2) +" "+ "=" +" "+ str(calculation_result)
                                    with open('calculation.txt', 'a') as file:
                                        file.write(equation + "\n")
                                
                                except ValueError:  # Handle non-numeric input by the user (for the first number)
                                    print("Invalid input. Please enter a valid number, using only digits and a decimal point.")
                                    continue
                                break

                        elif repeat != "n":
                            raise Exception 
                        else:
                            break
                                
                        
                    except Exception:
                        print("please choose either \"Y\" or \"N\"") 
                        continue
            
            
            # This section opens a file specified by the user and reads the contents of the file.
            # It is used to retrieve input data for the program.           
            else:
                print("\nYou have chosen to read equations from a file.")
                while True: 
                    try:
                        file_name = input("please enter the file name: ")
                        if '.' not in file_name:
                            file_name += '.txt' # add .txt extension by default
                        
                        with open(file_name, 'r') as file:
                            file_contents = file.read()
                            print(file_contents)
                        break # break the loop if the input is valid
                    
                    except FileNotFoundError as error:
                            print("The file that you are trying to open does not exist")
                            print(error)
                            continue
                break
                                                
    except ValueError:  # Handle non-numeric input by the user
        print("\nPlease enter (1 or 2). Only numerical input is allowed.")
        continue
                    
    
            
            
        
    
    
            
            


                
        








        

