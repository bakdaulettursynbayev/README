def mult(nums):
    ttl = 1
    
    for i in nums:
        ttl = ttl * i
    
    return ttl

print(mult((2, 2, 3, 5, 11)))