#By Jared Anderson

#Test Cases:
#Input:
#Select the first matrix (A,B,C,D): 5
#Not a valid input, Please enter in (A,B,C,D): a
#Select the Second matrix (A,B,C,D): a
#Do you want to add or multiply them (A, M): b
#Not a valid input, Please enter in (A,M): a

#Otput:
#Out = 2   4   
#      6   8  


#Input:
#Select the first matrix (A,B,C,D): '
#Not a valid input, Please enter in (A,B,C,D): b
#Select the Second matrix (A,B,C,D): h
#Not a valid input, Please enter in (A,B,C,D): c
#Do you want to add or multiply them (A, M): 6
#Not a valid input, Please enter in (A,M): m

#Otput:
#Out = 22  28  
#      49  64  


#Input:
#Select the first matrix (A,B,C,D): d
#Select the Second matrix (A,B,C,D): d
#Do you want to add or multiply them (A, M): m

#Output:
#Out = 30  36  42  
#      66  81  96  
#      102 126 150 

#Input:
#Select the first matrix (A,B,C,D): d
#Select the Second matrix (A,B,C,D): c
#Do you want to add or multiply them (A, M): m

#Output:
#Out = 22  28  
#      49  64  
#      76  100 

#Input:
#Select the first matrix (A,B,C,D): b
#Select the Second matrix (A,B,C,D): c
#Do you want to add or multiply them (A, M): a

#Output:
#Invalid. The Dimentions of the Matrixes do not match.

#Input:
#Select the first matrix (A,B,C,D): a
#Select the Second matrix (A,B,C,D): c
#Do you want to add or multiply them (A, M): m

#Output:
#Invalid. The Dimentions of the Matrixes are not compatible.
A = [[1,2],[3,4]]
B = [[1,2,3],[4,5,6]]
C = [[1,2],[3,4],[5,6]]
D = [[1,2,3],[4,5,6],[7,8,9]]
first = []
second = []
out = []

valid1 = ["a","b","c","d","A","B","C","D"]
valid2 = ["a","m","A","M"]

errmsg1 = 'Not a valid input, Please enter in (A,B,C,D): '
errmsg2 = 'Not a valid input, Please enter in (A,M): '
       
msg1 = 'Select the first matrix (A,B,C,D): '
msg2 = 'Select the Second matrix (A,B,C,D): '
msg3 = 'Do you want to add or multiply them (A, M): '


def CheckInput(validList, msg, errmsg):
    x = ""
    check = 0
    while x not in validList:
        try:
            if check == 1:
                x = str(input(errmsg))
            else:
                x = str(input(msg))
        except ValueError:
            check = 1
        if x not in validList:
            check = 1
    return x
    
def PrintMatrix(matrix, name):
    
    temp = name + " = "
    
    for i in range(len(matrix)):
        if i != 0:
            temp += "      "
            
        for j in range(len(matrix[0])):

            if len(str(matrix[i][j])) < 2:
                temp += (str(matrix[i][j]) + "   ")
                
            elif len(str(matrix[i][j])) < 3:
                temp += (str(matrix[i][j]) + "  ")
                
            else:
                temp += (str(matrix[i][j]) + " ")

        print(temp)
        temp = ""
        
        
def AddMatrix(mat1, mat2):
    
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        
        for i in range(len(mat1)):
            temp = []
            
            for j in range(len(mat1[0])):
                temp.append(mat1[i][j] + mat2[i][j])
                
            out.append(temp)
            
        PrintMatrix(out, "Out")
        
    else:
        print("Invalid. The Dimentions of the Matrixes do not match.")
        
        
def MultiplyMatrix(mat1, mat2):
    
    if len(mat1[0]) == len(mat2):
        
        for i in range(len(mat1)):
            temp = []
            
            for j in range(len(mat2[0])):
                
                l = 0
                for k in range(len(mat2)):
                    l += mat1[i][k] * mat2[k][j]
                    
                temp.append(l)
            out.append(temp)
                    
        PrintMatrix(out, "Out")    
    else:
        print("Invalid. The Dimentions of the Matrixes are not compatible.")
        
        
x = CheckInput(valid1, msg1, errmsg1) 
y = CheckInput(valid1, msg2, errmsg1)  
z = CheckInput(valid2, msg3, errmsg2) 


if x is "a" or x is "A":
    first = A
elif x is "b" or x is "B":
    first = B
elif x is "c" or x is "C":
    first = C
elif x is "d" or x is "D":
    first = D
else:
    print("Error in input 1")
    
if y is "a" or y is "A":
    second = A
elif y is "b" or y is "B":
    second = B
elif y is "c" or y is "C":
    second = C
elif y is "d" or y is "D":
    second = D
else:
    print("Error in input 2")
    
    
if z is "a" or z is "A":
    AddMatrix(first, second)
else:
    MultiplyMatrix(first, second)
    

    
    
    
    
    
    
    
    
    
    
    
    

