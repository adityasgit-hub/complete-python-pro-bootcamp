# Calculator

# Add
def add(num1, num2):
  return num1 + num2

# Subtract
def subtract(num1, num2):
  return num1 - num2

# Multiply
def multiply(num1, num2):
  return num1 * num2

# Divide
def divide(num1, num2):
  return num1 / num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("Enter the first number: "))

for operator in operations:
    print(operator)
    
sel_op = input("Enter an operator from the above: ")

num2 = int(input("Enter the second number: "))

op = operations[sel_op]
answer = op(num1, num2)

print(f"{num1} {sel_op} {num2} = {answer}")
