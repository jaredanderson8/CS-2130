#By Jared Anderson
#test cases:

#input: 50
#expected output:
#50 in base 2: 110010
#50 in base 8: 62
#50 in base 16: 32

#input: 69
#expected output:
#69 in base 2: 1000101
#69 in base 8: 105
#69 in base 16: 45

#input: 7
#expected output:
#7 in base 2: 111
#7 in base 8: 7
#7 in base 16: 7

#input: negative value or a string:
#expected output:
# Not a valid input, Please enter in a positive base 10 number:


x = 0
check = 0
while not int(x) > 0:
    try:
        if check == 1:
            x = int(input('Not a valid input, Please enter in a positive base 10 number:'))
        else:
            x = int(input('Please enter in a positive base 10 number:'))
    except ValueError:
        check = 1

#bianary
y = bin(x)
y = y[2:]
print x , "in base 2:" , y

#octal
y = oct(x)
y = y[1:]
print x , "in base 8:" , y

#hexadecimal
y = hex(x)
y = y[2:]
print x , "in base 16:" , y
