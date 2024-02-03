"""
A program that reads and outputs shipping logs saved as text files.
User can type in name of file they would like to view.
Program reads data and outputs using string manipulation.
Prints log info in console in a readable way
"""
import os

print("-"*50)
print("Welcome to log management program!")
print("-"*50)



# Options to view or exit?????? too much??
while True:
    print("Choose from the options: \n1. View Log \n2. Exit Program")
    user_option = input("Type option number here:\t")
    if user_option.isnumeric():
        user_option = int(user_option)
    
    if user_option == 1:
        # Print file names to show user selection in folder
        # Can I print numbered then choose from that list???????
        # ORRRRR ALLL DATA ON ONE TXT FILE, AS LIST??? LIKE DUMMY_TEXT.TXT WK 7 PORTFOLIO SUNDAY
        print(os.listdir())

    # Loop to ask for correct file name
        while True:
            try:
                user_file = input("Type file name:\t")
                with open(user_file, "r") as file:
                    content = file.read()
                    break

            except FileNotFoundError:
                print("File not found")

        # Split and store in variables
        split_string = content.split("|")

        date_time = split_string[0]
        log_type = split_string[1]
        tracking_number = split_string[2]
        location = split_string[3]
        goods_type = split_string[4]

        # Format to make readable for user
        log_output = f"Date: \t\t{date_time} \nLog Type: \t{log_type} \
            \nTracking No.: \t{tracking_number} \nLocation: \t{location} \
            \nGoods Type: \t{goods_type}"

        print("-"*50)
        print(log_output)
        print("-"*50)

    if user_option == 2:
        print("-"*50)
        print("Thanks for using log management tool!")
        print("-"*50)
        break

    else:
        print("Please type '1' or '2' only")  # WHY DOES THIS PRINT AFTER LOG???? HMMM ORDER OF CODE
        print("-"*50)