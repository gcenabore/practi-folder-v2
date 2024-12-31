
number = []
while True:
    for i in range(10):
        while True:
            try:
                num = int(input("Please enter 10 different numbers: "))
                number.append(num)
                break
            except ValueError:
                print("ERROR: please enter a integer value only..")
            
    duplicates = list(set([num for num in number if number.count(num) > 1]))
    print(f"the numbers with duplicates are {duplicates}.")
    
    retry = input("Do you want to try again? y/n: ").strip().lower()
    if retry != "y":
        print("THANK YOU!!")
        break



