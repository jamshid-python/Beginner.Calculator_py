til = input("Tilni tanlang uz/eng:  ")    
if til == "uz":
    print("Assalomu Alaykum.")
    print("MHT company ga xush kelibsiz.")
    print("Ushbu dastur Jamshid Ahmadov tomonidan yaratilgan.")
    name = input("Ismingiz kim?:  ")
    family = input("Familyangiz kim? ")
    print("Sizning ism-familyangiz", name, family)
    
    amal = input("Amalardan birini tanlang; + - * /  =>> ")
    if amal == "+":
            birinchi_son = int(input("Birinchi sonni kiriting: "))
            ikkinchi_son = int(input("Ikkinchi sonni kiriting: "))
            javob = int(birinchi_son) + int(ikkinchi_son)
            print("Natija",javob)
        
    elif amal == "-":
            birinchi_son1 = int(input("Birinchi sonni kiriting: "))
            ikkinchi_son1 = int(input("Ikkinchi sonni kiriting: "))
            javob1 = int(birinchi_son1) - int(ikkinchi_son1)
            print("Natija: ", javob1)
        
    elif amal == "*":
            birinchi_son2 = int(input("Birinchi sonni kiriting: "))
            ikkinchi_son2 = int(input("Ikkinchi sonni kiriting: "))
            javob2 = int(birinchi_son2) * int(ikkinchi_son2)
            print("Natija", javob)
            
    elif amal == "/" or ":":
            birinchi_son3 = int(input("Birinchi sonni kiriting: "))
            ikkinchi_son3 = int(input("Ikkinchi sonni kiriting: "))
            javob3 = int(birinchi_son3) / int(ikkinchi_son3)
            print("Natija:", javob3)
                     
elif til == "eng":
    print("Hello")
    print("Welcome to MHT company")
    print("This program was created by Jamshid Ahmadov")
    name1 = input("What is your name? : ")
    family1 = input("What is your surname? : ")
    print("Your full name is ", name1, family1)
    
    hk1 = input("Select one of the actions: + - * / =>> ")
    if hk1 == "+":
            a4 = int(input("Enter the first number: "))
            b4 = int(input("Enter the second number: "))
            c4 = int(a4) + int(b4)
            print("the Result", c4)
            
    elif hk1 == "-":
            a5 = int(input("Enter the first number: "))
            b5 = int(input("Enter the second number: "))
            c5 = int(a5) - int(b5)
            print("the Result", c5)
    elif hk1 == "*":
            a6 = int(input("Enter the first number: "))
            b6 = int(input("Enter the second number: "))
            c6 = int(a6) * int(b6)
            print("the Result", c6)
            
    elif hk1 == "/":
            a7 = int(input("Enter the first number: "))
            b7 = int(input("Enter the second number: "))
            c7 = int(a7) / int(b7)
            print("The Result", c7)
# Coder - Jamshid-pyton
# https://github.com/jamshid-python/