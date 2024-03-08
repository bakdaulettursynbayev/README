import os

print('Exist:', os.access('/Users/bakdaulettursunbaev/Desktop/README', os.F_OK))
print('Readable:', os.access('/Users/bakdaulettursunbaev/Desktop/README', os.R_OK))
print('Writable:', os.access('/Users/bakdaulettursunbaev/Desktop/README', os.W_OK))
print('Executable:', os.access('/Users/bakdaulettursunbaev/Desktop/README', os.X_OK))