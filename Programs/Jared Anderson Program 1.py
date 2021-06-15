#Program 1 - Set Operations
#by Jared Anderson

#Expected Output:
# A = {1, 3, 5, 6, 8}
# B = {2, 3, 4, 7, 9}
# AuB = {1, 3, 5, 6, 8, 2, 4, 7, 9}
# AnB = {3}
# A-B = {1, 5, 6, 8}

A = [1,3,5,6,8]
B = [2,3,4,7,9]

i = 0

#initial print out
print('A = {' + ', '.join(str(x) for x in A) + '}')
print('B = {' + ', '.join(str(x) for x in B) + '}')

#union

u = A

while i < len(B):
    t = B[i]
    if t not in u:
        u.append(t)
    i += 1

print('AuB = {' + ', '.join(str(x) for x in u) + '}')    


#intersection
A = [1,3,5,6,8]
B = [2,3,4,7,9]

i = 0
u = []

while i < len(B):
    t = B[i]
    if t in A:
        u.append(t)
    i += 1
    
print('AnB = {' + ', '.join(str(x) for x in u) + '}') 


#Minus

A = [1,3,5,6,8]
B = [2,3,4,7,9]

i = 0
u = A

while i < len(B):
    t = B[i]
    if t in A:
        u.remove(t)
    i += 1    
    
print('A-B = {' + ', '.join(str(x) for x in u) + '}') 
