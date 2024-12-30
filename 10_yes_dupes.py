
number = []

for i in range(10):
    try:
        num = int(input("Please enter 10 different numbers: "))
        number.append(num)
        break
    except ValueError:
        print("ERROR: please enter a integer value only..")
        