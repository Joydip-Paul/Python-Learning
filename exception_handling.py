
# EXCEPTIONS HANDLING
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("OI MIA ZERO DIA VAG KORTE PARBA NA")
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("Error:", e)


#REAL WORLD EXCEPTION HANDLING
print("===========================")
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Bro, you can’t divide by zero!")
    return a / b

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error happened:", e)