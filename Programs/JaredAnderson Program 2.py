#By Jared Anderson

#Test cases:
#"hello" = 21
#"pooh bear" = 18
#"We the People of the United States in Order to form a more perfect Union" = 27
#"101 Dalmatians" = invalid input

h = input("Please Enter in a string to hash: ")

n = 0
i = 0

for element in h: 
    
    i = 0
    
    if element == 'a' or element == 'A':
        n += 1
        i = 1
    if element == 'b' or element == 'B':
        n += 2
        i = 1
    if element == 'c' or element == 'C':
        n += 3
        i = 1
    if element == 'd' or element == 'D':
        n += 4
        i = 1
    if element == 'e' or element == 'E':
        n += 5
        i = 1
    if element == 'f' or element == 'F':
        n += 6
        i = 1
    if element == 'G' or element == 'G':
        n += 7
        i = 1
    if element == 'h' or element == 'H':
        n += 8
        i = 1
    if element == 'i' or element == 'I':
        n += 9
        i = 1
    if element == 'j' or element == 'J':
        n += 10
        i = 1
    if element == 'k' or element == 'K':
        n += 11
        i = 1
    if element == 'l' or element == 'L':
        n += 12
        i = 1
    if element == 'm' or element == 'M':
        n += 13
        i = 1
    if element == 'n' or element == 'N':
        n += 14
        i = 1
    if element == 'o' or element == 'O':
        n += 15
        i = 1
    if element == 'p' or element == 'P':
        n += 16
        i = 1
    if element == 'q' or element == 'Q':
        n += 17
        i = 1
    if element == 'r' or element == 'R':
        n += 18
        i = 1
    if element == 's' or element == 'S':
        n += 19
        i = 1
    if element == 't' or element == 'T':
        n += 20
        i = 1
    if element == 'u' or element == 'U':
        n += 21
        i = 1
    if element == 'v' or element == 'V':
        n += 22
        i = 1
    if element == 'w' or element == 'W':
        n += 23
        i = 1
    if element == 'x' or element == 'X':
        n += 24
        i = 1
    if element == 'y' or element == 'Y':
        n += 25
        i = 1
    if element == 'z' or element == 'Z':
        n += 26
        i = 1
    if element == ' ':
        n += 31
        i = 1
        
    if i == 0:
        break;

n = n % 31  
        
        
if i == 1:
    print(n)
else:
    print("invalid input")










