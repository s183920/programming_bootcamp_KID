"""
1. Create an empty dictionary called student_info. 
2. Ask the user to input the student's name and age. Add this information to the dictionary. 
3. Display the dictionary.
"""
student_info = {}
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
student_info[name] = age
print(student_info)