name=input("What's your name :")#.strip().titlt()
#print("Hello",name)
#print("Hello ",end="")
#print(name)

# Remove whitespaces from string
name=name.strip()

# CApitalize users name
name=name.capitalize()

# Capitalize each first char in a string
name=name.title()

first, last=name.split(" ")

print(f"Hello,{last}")



#print('Hello"friend"')
#print("Hello\"friend\"")  # Escaping characters
