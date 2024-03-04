import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

number = 25100
milliseconds = 2123
result = square_root_after_milliseconds(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")