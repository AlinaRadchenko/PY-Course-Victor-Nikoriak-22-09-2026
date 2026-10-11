# AI log: none
def operation_mapper(oper):
    def operation(a, b):
        if oper == "+":
            return a + b
        elif oper == "-":
            return a - b
        elif oper == "/":
            return a / b
        elif oper == "*":
            return a * b
        elif oper == "**":
            return a ** b
    return operation


print(operation_mapper("+")(1, 2))
# 3.5
print(operation_mapper("/")(7, 2))
# 1024
print(operation_mapper("**")(2,10))
# operation_mapper не є декоратором, бо не приймає іншу функцію
