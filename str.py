 #asking the name of the user
name = input("What is your name?")

#remove the whitespace from the string and capitalize the user's name
name = name.strip().title()

#split user's name intothe first name and last name into
first, last = name.split(" ")


#say helllo to user
print(f"hello , bro {last}")

