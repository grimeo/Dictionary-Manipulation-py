# Nov 12

# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 12mn
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# Example Output:

# Menu:
#  1 -> Add an item
#  2 -> Search
#  3 -> Exit (y/n)

# What do you want to do? (1-3): 1
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# Saved!
# What do you want to do? (1-2): 2
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890 What do you want to do? (1-2): 3
# Exit? n


# option

# add info
# search
# exit

peopleInfo = {}
numberOfPeople = 0

Name = ""
Age = None
Address = ""
Contact = None

def showOption():
    print("\n============= Menu =============")
    print("\n1 -> Add an item\n2 -> Search\n3 -> Exit (y/n)\n")

def getInfo():
    Name = input("Type your name: ")
    Age = int(input("Type your age: "))
    Address = input("Type your address: ")
    Contact = int(input("Type your name: "))

def addNew():
    numberOfPeople = numberOfPeople+1
    peopleInfo[numberOfPeople]
    print()
    