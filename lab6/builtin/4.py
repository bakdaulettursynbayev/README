import time, math

def func(num, ms):
    
    time.sleep(ms / 1000)
    
    return math.sqrt(num)

num = int(input("Num: "))
ms = int(input("Time: "))

print(f"Square root of {num} after {ms} miliseconds is {func(num, ms)}")