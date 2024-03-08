import os
def cope(file3,file4):
    with open(file3,"r") as file:
        with open(file4,"w") as filee:
            filee.write(file.read())
a = r'/Users/bakdaulettursunbaev/Desktop/README/abs.py'
b = r'/Users/bakdaulettursunbaev/Desktop/README/abc.py'
cope(a,b)