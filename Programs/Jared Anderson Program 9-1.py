#Expected Output:
#A = 1 1 1 1 
#    1 1 1 1 
#    1 1 1 1 
#    1 1 1 1 
#A - reflexive, symmetric
 
#B = 1 1 1 1 
#    0 1 1 1 
#    0 0 1 1 
#    0 0 0 1 
#B - reflexive
 
#C = 0 1 1 1 
#    0 0 1 1 
#    0 0 0 1 
#    0 0 0 0 
#C - anti-reflexive, anti-symmetric, asymmetric
 
#D = 1 0 1 0 
#    1 0 1 0 
#    1 0 1 0 
#    1 0 1 0 
#D - none
 

A = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
B = [[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]]
C = [[0,1,1,1],[0,0,1,1],[0,0,0,1],[0,0,0,0]]
D = [[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0]]

def Reflexive(matrix):
    count = 0
    for i in range(4):
        if (matrix[i][i] == 1):
            count += 1
    return count  
    
def Symmetric(matrix):
    count = 0
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] != matrix[j][i]):
                return False
    return True


def AntiSymmetric(matrix):
    count = 0
    for i in range(4):
        for j in range(4):
            if not (matrix[i][j] == 0 and matrix[j][i] == 0):
                if (matrix[i][j] == matrix[j][i]):
                    return False
    return True
    
    
def PrintMatrix(matrix, name):
    
    temp = name + " = "
    
    for i in range(4):
        if i != 0:
            temp += "    "
        for j in range(4):
            temp += (str(matrix[i][j]) + " ")
        print(temp)
        temp = ""
     
    
def Relations(matrix, name):
    
    out = name + " - "
    
    if(Reflexive(matrix) == 0):
        out += "anti-reflexive"
    elif(Reflexive(matrix) == 4):
        out += "reflexive"
        
        
    if(Symmetric(matrix)):
        if(out != name + " - "):
            out += ", "
        out += "symmetric"
        
    elif(AntiSymmetric(matrix)):
        if(out != name + " - "):
            out += ", "
        out += "anti-symmetric"  
        
        
    if("anti-reflexive" in out and "anti-symmetric" in out):
        out += ", asymmetric"
        
        
    if(out == name + " - "):
        out += "none"
        
        
    return out
  
        
PrintMatrix(A, "A")
print(Relations(A, "A"))
print(" ")

PrintMatrix(B, "B")
print(Relations(B, "B"))
print(" ")

PrintMatrix(C, "C")
print(Relations(C, "C"))
print(" ")

PrintMatrix(D, "D")
print(Relations(D, "D"))
print(" ")












