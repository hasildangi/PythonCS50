#match shortcut 
name = input("what's your name?") 

match name:
    case"Hasil" |"Lokindra" | "Razzi":
        print("Shantinagar")
    case"Kamal":
        print("chinna")
    case"Kushal":
        print("kullalbada")
    case _:
        print ("who are you?")