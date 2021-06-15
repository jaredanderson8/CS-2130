#By Jared Anderson
#Test Cases:

#Input: n:10 r:5
#Output:
#Permutation:
#P(10,5) w/repeats: 100000
#P(10,5) w/o repeats: 30240
#Combination:
#C(10,5) w/repeats: 2002
#C(10,5) w/o repeats: 252

#Input: n:4 r:2
#Output:
#Permutation:
#P(4,2) w/repeats: 16
#P(4,2) w/o repeats: 12
#Combination:
#C(4,2) w/repeats: 10
#C(4,2) w/o repeats: 6

#Input: n:48 r:3
#Output:
#Permutation:
#P(48,3) w/repeats: 110592
#P(48,3) w/o repeats: 103776
#Combination:
#C(48,3) w/repeats: 19599
#C(48,3) w/o repeats: 17296

import math 

n = 0
check = 0
while not int(n) > 0:
    try:
        if check == 1:
            n = int(input('Not a valid input, Please enter in a number:'))
        else:
            n = int(input('Enter a value for n:'))
    except ValueError:
        check = 1

r = n + 1
check = 0
check2 = 0
while not int(r) <= n:
    try:
        if check == 1:
            r = int(input('Not a valid input, Please enter in a number:'))
        else:
            if(check2 == 0):
                r = int(input('Enter a value for r:'))
            else:
                r = int(input('r must be equal to or less than n, Please enter in a number:'))
            if(r > n):
                check2 = 1
            else:
                check2 = 0
           
    except ValueError:
        check = 1
        
print("Permutation:")
p1 = n**r
print("P(" + str(n) + "," + str(r) + ") w/repeats: " + str(p1))

p2 = math.factorial(n) / math.factorial(n - r)
print("P(" + str(n) + "," + str(r) + ") w/o repeats: " + str(p2))

print("Combination:")
c1 = math.factorial(n+r-1)  /  (math.factorial(r) * math.factorial((n+r-1) - r))
print("C(" + str(n) + "," + str(r) + ") w/repeats: " + str(c1))

c2 = math.factorial(n)  /  (math.factorial(r) * math.factorial((n - r)))
print("C(" + str(n) + "," + str(r) + ") w/o repeats: " + str(c2))
