def func(x, y):
    if (x>1) and (y>1):
        return 1
    elif (x<0) and (y<0):
        return 3
    elif (x<0) and (y>0):
        return 2
    elif (x>0) and (y<0):
        return 4
    else:
        print("Invalid options")

print("Input coordinates (x, y)")
print(func(int(input()), int(input())))