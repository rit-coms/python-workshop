def get_input():
    # get input (2 numbers)
    int_a = int(input("Please type first number: "))
    int_b = int(input("Please type second number: "))
    # get operator (+-*/)
    operator = input("Please tpye in an operator (+=*/): ")
    return int_a, int_b, operator

def do_math(operator, int_a, int_b):
    if operator == "+":
        result = int_a + int_b
    elif operator == "-":
        result = int_a - int_b
    elif operator == "*":
        result = int_a * int_b
    elif operator == "/":
        result = int_a / int_b
    else:
        print("That is not an operator")
    return result

    

while True:
    int_a, int_b, operator = get_input()
    # do the math
    result = do_math(operator, int_a, int_b)
    # print the output
    print(result)
    # do it again
    response = input("Do you want to go again? ")
    if response != "yes":
        break