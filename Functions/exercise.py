def fizz_buzz(input):
    for number in range(1, input):
        if(number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz")
        elif(number % 3 == 0):
            print("Fizz")
        elif(number % 5 == 0):
            print("Buzz")
        else:
            print(number)


print(fizz_buzz(30))
