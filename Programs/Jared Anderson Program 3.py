#Jared Anderson Program 3
string = ""
x = 4

for i in range(x):
    string += '1' * (x-i)
    string += '0' * (x-i)
    
print(string)
