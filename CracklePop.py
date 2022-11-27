def CracklePop():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 != 0: 
            print("Crackle")
        elif num % 3 != 0 and num % 5 == 0:
            print("Pop")
        elif num % 3 == 0 and num % 5 == 0:
            print("CracklePop")
        else:
            print(num)

CracklePop()