# # For Loops
# for number in range(1, 10, 2):
#     print("Attemp", number, number * ".")


# # For Else Loops
# successful = True
# for number in range(3):
#     print("Attempt")
#     if(successful):
#         print("Successful")
#         break
# else:
#     print("Attemped loop and didn't break out of loop")


# # Nested Loops
# for x in range(5):
#     for y in range(3):
#         print(f"{x}, {y}")


# # Iterables
# for x in "Python":
#     print(x)

# for x in [1, 2, 3, 4]:
#     print(x)

# shopping_cart = ["apple", "towel", "bread"]
# for item in shopping_cart:
#     print(item)


# # While Loops
# number = 100
# while number > 0:
#     print(number)
#     number = number // 2


command = ""
while command.lower() != "quit":
    command = input(">")
    print(">", command)
