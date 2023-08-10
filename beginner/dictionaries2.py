"""
1. Create a dictionary called phone_book to store names and phone numbers. 
2. Ask the user to input a name and a corresponding phone number. Add this information to the dictionary. 
3. If the phone number is not 8 digits you must print "invalid phone number" and not add the name and phone number to the dictionary.
4. Ask the user for a name to look up and display the associated phone number.
"""


phone_book = {}
while True:
    name = input("Enter a name (or 'done' to stop): ")
    if name == 'done':
        break
    phone_number = input("Enter the phone number: ")
    
    if len(phone_number) != 8:
        print("invalid phone number")
    else:
        phone_book[name] = phone_number
    

lookup_name = input("Enter a name to look up: ")
print(phone_book[lookup_name])

