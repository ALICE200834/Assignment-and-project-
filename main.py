print("welcome to utility Toolbox")
print("Menu:")
print("Calcuator")
print("Age checker")
print("String manipulation")
print("quiz app")
choice=input("Choose an option")

#Calculator
if choice == "1":
    print("Welcome to calc app")
    num1=float(jnput("Enter first number:"))
    num2=float(input("Enter second number"))
    operator = input ("Which sign would you like to use addition ,subtraction ,multiplication ,division")
    if operator =="+":
        print(num1 + num2)
    elif operator =="-"
        print(num1 - num2)
    elif operator =="/"
        print(num1 / num2)
    elif operator =="*"
        print(num1 * num 2)
elif choice == "2":
    print("Welcome to age checker")
    age = input("How old are you ? ")

    if age >= 12 :
        print("You are a child")
    elif age >= 18 :
        print("You are a teenager")
    elif age >= 22:
        print ("You are an adult")
    else age>= 90
        print ("You are a senior citizen")
     
