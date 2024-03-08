def letters(string):
    uppers = 0
    lowers = 0
    
    for c in string:
        if c.isupper() == True:
            uppers += 1
        elif c.islower() == True:
            lowers += 1
    return uppers, lowers

print(letters("Hello World"))