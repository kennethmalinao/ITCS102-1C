import time
name = input("Hi, What is your name? ").title()
print(f"WELCOME {name}, TO MY CODE COMPILER PROGRAM!")
print("\n===========================================")

while True:
    print("\n\t\t>>MENU LIST<<")
    print("\n===========================================")
    print("\n----------------------")
    print("|A - PRINT STATEMENTS")
    print("|B - VARIABLES")
    print("|C - OPERATORS")
    print("|D - CONDITIONAL STATEMENTS")
    print("|E - LOOP")
    print("|F - LIST")
    print("|G - FUNCTIONS")
    print("|H - DICTIONARY")
    print("|X - EXIT")
    print("----------------------")

    choice = input("\nInput your choice:  ").upper()

    if choice == "A":
        while True:
            print("\nYou chose PRINTING STATEMENTS ")
            print("___________________")
            print("|                  |")
            print("|Option 1 Submenu: |")
            print("|__________________|")
            print("\na - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("\nEnter your choice:  ")
            if sub_choice == 'a':
                print("\n\t===========================================")
                print(" \n\t A print statement is a command used in\n\t programming to output or display information\n\t such as text, numbers, or variables to the\n\t screen, console, or terminal. Using the\n\t print(""\"\"), with the double qoutation marks inside.")
                print("\n\t===========================================")
                continue
            elif sub_choice == 'b':
                print("\n\t===========================================")
                print("\n\tExample: ")
                print("\tprint(""\"Welcome to the Python programming\")")
                user_input = input("\n\tEnter any that you want to print: \n\t")
                print("\n\t===========================================")
                print("\n\tOUTPUT: ")
                print(f"\n\t{user_input}")
                print("\n\t===========================================")
                continue
            elif sub_choice == 'c':
                print("\n\t=======================")
                print("\n\t  Wait for a while...")
                print("\n\t=======================")
                time.sleep(1.5)


                break
            else:
                print("\nInvalid choice. Please enter a, b, or c.")

                continue

    elif choice == "B":
        print("\nPlease Wait....")
        
        while True:
            print("\nYou chose VARIABLES ")
            print("___________________")
            print("|                  |")
            print("|Option 2 Submenu: |")
            print("|__________________|")
            print("\na - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("\nEnter your choice:  ")
            if sub_choice == 'a':
                print("\n\t================================================")
                print("\n\tVariable can change or update its value anytime.\n\tProgrammers use variables to keep track of important data.")
                print("\n\t================================================")

                continue
            elif sub_choice == 'b':
                print("\n\t===========================================")
                print("\n\tExample:")
                print("\tINPUT:")
                print("\n\tname = input('What is your name? ')")
                print("\tage = input(\"How old are you? \")")
                print("\tloc = input(\"Where do you live? \")")
                print("\n\tHello, name!")
                print("\tYou are age years old.")
                print("\tYou live in")
                print("\n\t===========================================")

                print("\n\tOUTPUT:")
                name = input("\tWhat is your name? ").title()
                age = input("\tHow old are you? ")
                loc = input("\tWhere do you live? ")
                print("\n\t================================")
                print("\n\tHello,", name + "!")
                print("\tYou are", age, "years old.")
                print("\tYou live in", loc)
                print("\n\t================================")


                continue
            elif sub_choice == 'c':
                print("\n\t=======================")
                print("\n\t  Wait for a while...")
                print("\n\t=======================")
                time.sleep(1.5)
                break
            else:
                print("Invalid choice... Please enter a, b, or c.")

                continue
    elif choice == "C":
        print("\nPlease Wait....")

        while True:
            print("\nYou chose OPERATORS ")
            print("\n___________________")
            print("|                  |")
            print("|Option 3 Submenu: |")
            print("|__________________|")
            print("\na - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("\nEnter your choice: ")
            if sub_choice == 'a':
                print("\n\t====================================================")
                print("\n\tOperators do math or compare things, like + or ==.\n\tThey help a program solve problems, check conditions,\n\tor combine values.")
                print("\n\t====================================================")

                continue
            elif sub_choice == 'b':
                print("\n\t=============================================")
                print("\n\tExample: ")
                print("\tINPUT: ")
                num1 = int(input("\n\tEnter the first number: "))
                num2 = int(input("\tEnter the second number: "))

                print("\n\t=============================================")
                print("\n\tAddition:", num1, "+", num2, "=", num1 + num2)
                print("\tSubtraction:", num1, "-", num2, "=", num1 - num2)
                print("\tIs the first number greater than the second?", num1 > num2)
                print("\tAre the numbers equal?", num1 == num2)
                print("\n\t=============================================")   

                continue
            elif sub_choice == 'c':
                print("\n\t=======================")
                print("\n\t  Wait for a while...")
                print("\n\t=======================")
                time.sleep(1.5)
                 
                break
            else:
                print("Invalid choice. Please enter a,b, or c.")
            
                continue

        
    elif choice == "D":
        while True:
            print("\nYou chose CONDITIONAL STATEMENTS ")
            print("\n___________________")
            print("|                  |")
            print("|Option 4 Submenu: |")
            print("|__________________|")
            print("\na - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice=input("\nInput Your Choice: ")
            if sub_choice == 'a':
                print("\n\t======================================================")
                print("\n\tIf statements check conditions and run code if true.\n\tThey tell the program to do something only when\n\ta certain condition is true. If the condition\n\tis not true, the program can do something else\n\tusing else.")
                print("\n\t======================================================")

                continue

            elif sub_choice =='b':
                print("\n\t==================================")
                print("\n\tExample: ")
                print("\tINPUT:")
                print('\n\tage = int(input("Enter your age: "))')
                print('\n\t\tif age >= 18: ')
                print("\n\tYou are an adult! ")
                print('\n\telse: ')
                print("\n\t\tYou are a minor. ")
                print("\nOUTPUT: ")
                print("\n\t==================================")
                age = int(input("\n\tEnter your age: "))
                
                if age >= 18:
                    print("\n\tYou are an adult!")
                else:
                    print("\n\tYou are a minor.")
                print("\n\t===================================")

                continue
            
            elif sub_choice =='c':
                print("\n\t=======================")
                print("\n\t  Wait for a while...")
                print("\n\t=======================")
                time.sleep(1.5)
                 
                break
            else:
                print("Invalid choice. Please enter a,b, or c.")
            
                continue 

        continue
    elif choice == "E":
       while True:
            print("\nYou chose LOOP ")
            print("\n___________________")
            print("|                  |")
            print("|Option 5 Submenu: |")
            print("|__________________|")
            print("\na - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("\n\t=========================================")
                print("\n\tA loop in programming is a command that\n\tmakes your code repeat a set of instructions until\n\ta condition is met.")
                print("\n\t=========================================")
                continue
            elif sub_choice == 'b':
                print("\n\t=============================================")
                print("\n\tINPUT: ")
                print("\n\tEXAMPLE: ")
                print("for i in range(1, 11):")
                print("    for x in range(1, number + 1):")
                print("        if any_number == \"1\":")
                print("            print(x, \"+\", i, \"=\", x+i, end=\"\\t\")")
                print("        elif any_number == \"2\":")
                print("            print(x, \"-\", i, \"=\", x-i, end=\"\\t\")")
                print("        elif any_number == \"3\":")
                print("            print(x, \"*\", i, \"=\", x*i, end=\"\\t\")")
                print("        elif any_number == \"4\":")
                print("            print(x, \"/\", i, \"=\", round(x/i, 2), end=\"\\t\")")
                print("        else:")
                print("            print(\"Invalid\", end=\"\\t\")")
                print("    print()")
                print("\n\t==============================================")

                print("\t1. Addition")
                print("\t2. Subtraction")
                print("\t3. Multiplication")
                print("\t4. Division")

                any_number = input("\n\tChoose operation (1-4): ")
                number = int(input("\n\tEnter the numbers of tables (1-10): "))
                print("\n=================================================================================\n")
                print("OUTPUT: \n")
            
                if number == 11:
                    print("\n\tOnly 10 tables allowed!!! ")
                    print("\n\t=================================================================================\n")
                    continue

                for i in range(1, 11):          
                    for x in range(1, number + 1): 
                        if any_number == "1":
                            print(x, "+", i, "=", x+i, end="\t")
                        elif any_number == "2":
                            print(x, "-", i, "=", x-i, end="\t")
                        elif any_number == "3":
                            print(x, "*", i, "=", x*i, end="\t")
                        elif any_number == "4":
                            print(x, "/", i, "=", round(x/i, 2), end="\t")
                        else:
                            print("Invalid", end="\t")
                    print()   
                print("\n=================================================================================")
                continue
            elif sub_choice == 'c':
                print("\n\t=======================")
                print("\n\t  Wait for a while...")
                print("\n\t=======================")
                time.sleep(1.5)
                break
            else:
                print("\nInvalid choice. Please enter a, b, or c.")
                continue

    elif choice == "F":
        while True:
            print("\nYou chose LIST ")
            print("\n___________________")
            print("|                  |")
            print("|Option 6 Submenu: |")
            print("|__________________|")
            print("\na - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("\n\t============================================")
                print("\n\tLists hold many items in order, and you can\n\tadd, remove, or change elements easily.")
                print("\n\t============================================")
                continue

            elif sub_choice == 'b':
                print("\nExample: ")
                print("\n\t================================================")
                print("\n\tWELCOME TO THE FREE ITEMS ADD LIST")
                item_list = []

                while True:
                    item = input("\n\tEnter the items you want to list(or type 'done' to finish): ")
                    if item == "done":
                        break
                    item_list.append("\t" +"-" + item )
                    print("\t" + item, "has been added to your items list.")

                print("\n\tYou have exited the listing item program.")
                print("\n\t============================================")
                print("\n\tYour items list includes: \n")
                for i in item_list:
                    print(i)
                print("\n\t============================================")
                    
                    
                continue
            elif sub_choice == 'c':
                print("\n\t=======================")
                print("\n\t  Wait for a while...")
                print("\n\t=======================")
                time.sleep(1.5)
                break

            else:
                print("\nInvalid choice. Please enter a, b, or c.")
                continue

    elif choice == "G":
        while True:
            print("\nYou chose FUNCTION ")
            print("\n___________________")
            print("|                  |")
            print("|Option 7 Submenu: |")
            print("|__________________|")
            print("\na - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("\n\t==============================================")
                print("\n\tFunctions are used to structure your code in a\n\tbetter way, so that your code becomes easier to\n\tread and to use.")
                print("\n\t==============================================")
                continue
            
            elif sub_choice == 'b':
                print("\n\t=========================================")
                print("\n\tINPUT")
                print("\tEXAMPLE : ")
                print("\n\tdef GreetPerson(name, age, habit, location):")
                print("\t    print(\"Hello,\", name)")
                print("\t    print(\"Your age is:\", age)")
                print("\t    print(\"Your habit is:\", habit)")
                print("\t    print(\"You are from:\", location)")
                print("\t    print(\"Keep studying and improving yourself every day!\")")
                print()
                print("\tname = input(\"Enter your name: \")")
                print("\tage = int(input(\"Enter your age: \"))")
                print("\thabit = input(\"Enter one of your habits: \")")
                print("\tlocation = input(\"Enter your location: \")")
                print("\tgreet_user(name, age, habit, location)")
                print("\n\t=========================================")

                def GreetPerson(name, age, habit, location):
                    print("\n\tHello,", name)
                    print("\tYour age is:", age)
                    print("\tYour habit is:", habit)
                    print("\tYou are from:", location)
                    print("\tKeep studying and improving yourself every day!")
                    print("\n\t=========================================")
                    
                print("\n\t=========================================")
                name = input("\n\tEnter your name: ").title()
                age = int(input("\tEnter your age: "))
                habit = input("\tEnter one of your habits: ")
                location = input("\tEnter your location: ").title()
                print("\n\t=========================================")
                print("\n\tOUTPUT: ")
                GreetPerson(name, age, habit, location)

                continue
 
            elif sub_choice == 'c':
                print("\n\t=======================")
                print("\n\t  Wait for a while...")
                print("\n\t=======================")
                time.sleep(1.5)
                break

            else:
                print("\nInvalid choice. Please enter a, b, or c.")
                continue
        
    elif choice == "H":
        while True:
            print("\nYou chose DICTIONARY ")
            print("\n___________________")
            print("|                  |")
            print("|Option 8 Submenu: |")
            print("|__________________|")
            print("\na - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("\n\t==============================================")
                print("\n\tA dictionary is a data structure that holds a\n\tcollection of data as a set of key-value pairs.\n\tEach key, which must be unique, has an associated\n\tvalue. Typically, the keys in a dictionary must be\n\tsimple data types (such as integers or strings)\n\twhile the values can be of any type.")
                print("\n\t==============================================")

            elif sub_choice == 'b':
                print("\n\t==================================================================")
                print("\n\tINPUT")
                print("\tEXAMPLE: ")
                print("\n\tyour_profile = {}")
                print("\tyour_profile['name'] = input(\"Enter your name: \")")
                print("\tyour_profile['color'] = input(\"Enter your favorite color: \")")
                print("\tyour_profile['food'] = input(\"Enter your favorite food: \")")
                print("\tyour_profile['subject'] = input(\"Enter your favorite subject: \")")
                print("\tyour_profile['sport'] = input(\"Enter your favorite sport: \")")
                print("\tyour_profile['animal'] = input(\"Enter your favorite animal: \")")
                print()
                print("\tfor key, value in your_profile.items():")
                print("\t    print(key.title() + ':', value)")
                print("\n\t==================================================================")

                your_profile = {}

                your_profile['your name'] = input("\n\tEnter your name: ").title()
                your_profile['favorite color'] = input("\tEnter your favorite color: ")
                your_profile['favorite food'] = input("\tEnter your favorite food: ")
                your_profile['favorite subject'] = input("\tEnter your favorite subject: ")
                your_profile['favorite sport'] = input("\tEnter your favorite sport: ")
                your_profile['favorite animal'] = input("\tEnter your favorite animal: ")

                print("\n\t==================================")
                print("\n\tOUTPUT: ")
                print("\t\t>>YOUR PROFILE<<\n")
                for key, value in your_profile.items():
                    print("\t", key.title() + ':', value)
                print("\n\t==================================")

            elif sub_choice == 'c':
                print("\n\t=======================")
                print("\n\t  Wait for a while...")
                print("\n\t=======================")
                time.sleep(1.5)
                break

    elif choice == "X":
        print("\n\t======================================================")
        print("\n\tSystem Out. Thank you for using the compiler program!")
        print("\n\t======================================================")
        time.sleep(1.0)
        break 
    
    else:
        print(" Invalid choice. Please select from the menu options (A-H, X).")
        continue 