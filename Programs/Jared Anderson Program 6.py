#By Jared Anderson
#Expected Output:
#---------------------------------------------
#a| b| c| d| e| (( c + ~d ) * b ) * ~( d + a * e )
#---------------------------------------------
#1| 1| 1| 1| 1| 0
#1| 1| 1| 1| 0| 0
#1| 1| 1| 0| 1| 0
#1| 1| 1| 0| 0| 1
#1| 1| 0| 1| 1| 0
#1| 1| 0| 1| 0| 0
#1| 1| 0| 0| 1| 0
#1| 1| 0| 0| 0| 1
#1| 0| 1| 1| 1| 0
#1| 0| 1| 1| 0| 0
#1| 0| 1| 0| 1| 0
#1| 0| 1| 0| 0| 0
#1| 0| 0| 1| 1| 0
#1| 0| 0| 1| 0| 0
#1| 0| 0| 0| 1| 0
#1| 0| 0| 0| 0| 0
#0| 1| 1| 1| 1| 0
#0| 1| 1| 1| 0| 0
#0| 1| 1| 0| 1| 1
#0| 1| 1| 0| 0| 1
#0| 1| 0| 1| 1| 0
#0| 1| 0| 1| 0| 0
#0| 1| 0| 0| 1| 1
#0| 1| 0| 0| 0| 1
#0| 0| 1| 1| 1| 0
#0| 0| 1| 1| 0| 0
#0| 0| 1| 0| 1| 0
#0| 0| 1| 0| 0| 0
#0| 0| 0| 1| 1| 0
#0| 0| 0| 1| 0| 0
#0| 0| 0| 0| 1| 0
#0| 0| 0| 0| 0| 0

x = 31
z = ""
y = 0
a = 1
b = 1
c = 1
d = 1
e = 1

print("---------------------------------------------")
print("a| b| c| d| e| (( c + ~d ) * b ) * ~( d + a * e )")
print("---------------------------------------------")

while x >= 0:
    z = bin(x)
    z = z[2:]
    
    if len(z) == 4:
        z = "0" + z
    if len(z) == 3:
        z = "00" + z
    if len(z) == 2:
        z = "000" + z
    if len(z) == 1:
        z = "0000" + z
        
    a = z[0]
    b = z[1]
    c = z[2]
    d = z[3]
    e = z[4]
    
    if ((c=="1" or d=="0") and b=="1") and not (d=="1" or (a=="1" and e=="1")):
        y = 1
    else:
        y = 0
    
    print(a + "| " + b + "| " + c + "| " + d + "| " + e + "| " + str(y))
    x -= 1
    
