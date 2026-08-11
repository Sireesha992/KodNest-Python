def calculate(first_number,second_number,operator):
    if operator == "+":
        return first_number+second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number*second_number
    elif opeartor =="/":
        return first_number/second_number
first_number = 12
second_number = 5
operator = "+"
result = calculate(first_number, second_number, operator)
print(result)
