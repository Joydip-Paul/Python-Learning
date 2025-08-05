# 📝 Task: Build a Simple Calculator Function
# Requirements:
# Write four functions:
# add(a, b) — returns the sum of a and b.
# subtract(a, b) — returns a minus b.
# multiply(a, b) — returns the product of a and b.
# divide(a, b) — returns a divided by b. (Hint: handle division by zero!)
# Then, call each function with some example numbers and print the results.


# CALCULATOR FUNCTIONS
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

print("Add:", add(10, 20))
print("Subtract:", subtract(50, 30))
print("Multiply:", multiply(5, 6))
print("Divide:", divide(50, 5))

