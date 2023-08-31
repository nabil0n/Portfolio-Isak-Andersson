pw = "hejhej"

def addi(x, y):
    return print("Added these numbers are: "+str(x + y))
def subt(x, y):
    return print("Subtracted these numbers are: "+str(x - y))
def mult(x, y):
    return print("Multiplied these numbers are: "+str(x * y))
def div(x, y):
    return print("Divided these numbers are: "+str(x / y))

print("Welcome to the calculator! Please enter password: ")

while input() != pw:
    print("Wrong password, try again: ")
else:
    print("""What would you like to calculate? Press:
          1. Add
          2. Subtract
          3. Multiply
          4. Divide""")
    choice = int(input())
    while choice < 1 or choice > 4:
        print("Not a valid option.")
        choice = int(input())
    else:
        print("Enter two numbers: ")
        i = int(input())
        j = int(input())
        if choice == 1:
            addi(i, j)
        elif choice == 2:
            subt(i, j)
        elif choice == 3:
            mult(i, j)
        elif choice == 4:
            div(i, j)
