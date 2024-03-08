def palindrome(string):
    
    rev = string[::-1]
    
    if rev == string:
        return True
    else:
        return False
    
print(palindrome("anana"))