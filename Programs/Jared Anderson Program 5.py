#Test Case:
#input: and, n, n:
#output:
#Answer:
#p	q	p A q
#F	F	F
#T	F	F
#F	T	F
#T	T	T

#input: or, n, n,
#output:
#Answer:
#p	q	p V q
#F	F	F
#T	F	T
#F	T	T
#T	T	T

#input: and, y, y:
#output:
#Answer:
#p	q	~p A ~q
#F	F	T
#T	F	F
#F	T	F
#T	T	F

x = ""
check = 0
while x != "and" and x != "or" and x != "AND" and x != "OR":
    try:
        if check == 1:
            x = str(input('Not a valid input, Please enter in and/or'))
        else:
            x = str(input('Do you want to AND or OR the variables (and/or): '))
    except ValueError:
        check = 1
    if x is not "and" or "or" or "AND" or "OR":
        check = 1
        
y = ""
check = 0
while y != "y" and y != "n" and y != "Y" and y != "N":
    try:
        if check == 1:
            y = str(input('Not a valid input, Please enter y/n'))
        else:
            y = str(input('Do you want to NOT p (y/n)? '))
    except ValueError:
        check = 1
    if y is not "y" or "n" or "Y" or "N":
        check = 1        
    
z = ""
check = 0
while z != "y" and z != "n" and z != "Y" and z != "N":
    try:
        if check == 1:
            z = str(input('Not a valid input, Please enter y/n'))
        else:
            z = str(input('Do you want to NOT q (y/n)? '))
    except ValueError:
        check = 1
    if z is not "y" or "n" or "Y" or "N":
        check = 1        
    
i = 0

print("Answer:")

if x == "and" or x == "AND":
    
    if (y == "y" or y == "Y") and (z == "y" or y == "Y"):
        print("p	q	~p A ~q")
    if (y != "y" and y != "Y") and (z == "y" or z == "Y"):
        print("p	q	p A ~q")
    if (y == "y" or y == "Y") and (z != "y" and z != "Y"):
        print("p	q	~p A q")
    if (y != "y" and y != "Y") and (z != "y" and z != "Y"):
        print("p	q	p A q")
            
    while i < 4:
        
        temp = ""
        w = ""
        if i == 0:
            p = "F"
            q = "F"
        if i == 1:
            p = "T"
            q = "F"
        if i == 2:
            p = "F"
            q = "T"
        if i == 3:
            p = "T"
            q = "T"
            
        temp = (p + "	" + q + "	")
        if y == "y" or y == "Y": 
            if p == "F":
                p = "T"
            else:
                p = "F"
                
        if z == "y" or y == "Y": 
            if q == "F":
                q = "T"
            else:
                q = "F"
                
        if p == "T" and q == "T":
            w = "T"
        else:
            w = "F"
            
        temp += w   
        print(temp)
        
        i += 1
        
else:
    
    if (y == "y" or y == "Y") and (z == "y" or y == "Y"):
        print("p	q	~p V ~q")
    if (y != "y" and y != "Y") and (z == "y" or z == "Y"):
        print("p	q	p V ~q")
    if (y == "y" or y == "Y") and (z != "y" and z != "Y"):
        print("p	q	~p V q")
    if (y != "y" and y != "Y") and (z != "y" and z != "Y"):
            print("p	q	p V q")
            
    while i < 4:
        
        temp = ""
        w = ""
        if i == 0:
            p = "F"
            q = "F"
        if i == 1:
            p = "T"
            q = "F"
        if i == 2:
            p = "F"
            q = "T"
        if i == 3:
            p = "T"
            q = "T"
            
        temp = (p + "	" + q + "	")
        if y == "y" or y == "Y": 
            if p == "F":
                p = "T"
            else:
                p = "F"
                
        if z == "y" or y == "Y": 
            if q == "F":
                q = "T"
            else:
                q = "F"
                
        if p == "T" or q == "T":
            w = "T"
        else:
            w = "F"
            
        temp += w   
        print(temp)
        
        i += 1











