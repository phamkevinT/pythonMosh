from email import message


def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


greet("Kevin", "Pham")


###########################################


def get_greeting(name):
    return (f"Greetings, {name}")


message = get_greeting("Kevin")
file = open("content.txt", "w")
file.write(message)


######################## Keyword Arguments ########################


def increment(number, by):
    return number + by


print(increment(2, by=1))


######################## Default Arguments ########################


def increment(number, by=1):
    return number + by


print(increment(2))  # Outputs 3, as the default value for 'by' is 1
print(increment(2, 5))  # Outputs 7


######################## xargs ########################

def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(2, 3, 4, 5))


######################## xxargs ########################


def save_user(**user):
    print(user)


save_user(id=1, name="Kevin", age="24")

# Can pass multiple keyword arguments into a a function and python will package them into a user object dictionary


######################## Scope ########################
