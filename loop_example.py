
# topping = input("What is your favorite topping")

# while topping != "pineapple":
#     print(f"{topping.capitalize()} ain't pineapple")
#     topping = input("What is your favorite topping")

#     if topping == "sausage":
#         break


# break exits the loop complete (gives you another out)

# continue skips to the next loop iteration

numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
