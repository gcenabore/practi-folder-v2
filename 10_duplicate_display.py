# Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

def get_number():

    numbers = []
    for i in range(10):
        while True:
            try:
                num = int(input("please enter a number: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. please enter a interger only.")
    return numbers

def display_numbers(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    print(f"number with only the first entry of duplicates {result}")

if __name__ == "__main__":
    numbers = get_number()
    display_numbers(numbers) 