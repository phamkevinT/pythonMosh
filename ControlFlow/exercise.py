number = 10
count = 0
for num in range(1, number+1):
    if(num % 2 == 0):
        print(num)
        count = count + 1
print(f"We have {count} even numbers")
