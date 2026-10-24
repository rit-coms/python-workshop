def factorial(num): # 5
    i = num # i = 5
    result = 1
    while i != 0:
       result = result * num # 5
       print("Result: " + str(result))
       i -= 1 # i = 4
       num -= 1
    return result

def fact(n):
    total = 1
    if n == 0 or n == 1:
        return total
    else:
        for number in range(1, n+1):
            total *= number
        return total

print(factorial(3))