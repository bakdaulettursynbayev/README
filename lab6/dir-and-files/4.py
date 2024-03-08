import os
def lines(file):
    with open(file,'r') as file:
        count = 0
        for _ in file:
            count+=1
        return count
file = r'/Users/bakdaulettursunbaev/Desktop/README/test.txt'
a = lines(file)
print(a)