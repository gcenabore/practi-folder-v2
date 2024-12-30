# Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

numbers = []

for i in range(10):
    while True:
        try:
            num = int(input("please enter a number: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. please enter a interger only.")

no_dupes = [num for num in numbers if numbers.count(num) == 1]
print(f"the numbers without duplicates is {no_dupes}")

