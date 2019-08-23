count = 1

# 1
print("This is patter no == ",count)
count+=1
n = int(input(" enter number of row "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end= " ")
    print()

# 2
print("This is patter no == ",count)
count+=1
n1 = int(input(" enter number of row "))
for i in range(1,n1+1):
    for j in range(1,n1+1):
        print(chr(64+j),end= " ")
    print()


# 3
print("This is patter no == ",count)
count+=1
n1 = int(input(" enter number of row "))
for i in range(1,n1+1):
    for j in range(1,i+1):
        print(j,end= " ")
    print()

#4
print("This is patter no == ",count)
count+=1
n = int(input(" enter number of row "))
for i in range(1,n1+1):
    for j in range(1,i+1):
        print(chr(64+j),end= " ")
    print()
#5
print("This is patter no == ",count)
count+=1
n1 = int(input(" enter number of row "))
for i in range(1,n1+1):
    for j in range(1,n1+2-i):
         print("*",end= " ")
    print()

#6
print("This is patter no == ",count)
count+=1
n1 = int(input(" enter number of row "))
for i in range(1,n1+1):
    for j in range(1,n1+2-i):
         print(chr(65+n-i),end= " ")
    print()

#7
print("This is patter no == ",count)
count+=1
n1 = int(input(" enter number of row "))
for i in range(1,n1+1):
    for j in range(1,n1+2-i):
         print(n+1-j,end= " ")
    print()

#8
print("This is patter no == ",count)
count+=1
n2 = int(input("inter row number"))
for i in range(1,n2+1):
    print(" "*(i-1),(str(n2+1-i)+" ")*(n2+1-i))

#9
print("This is patter no == ",count)
count+=1
n2 = int(input("inter row number"))
for i in range(1,n2+1):
    print(" "*(i-1),end=" ")
    for j in  range(1,n2+2-i):
        print(j,end=" ")
    print()
#10
print("This is patter no == ",count)
count+=1
n2 = int(input("inter row number"))
for i in range(1,n2+1):
    print(" "*(i-1),"*"*(2*i-1))

#11
print("This is patter no == ",count)
count+=1
n2 = int(input("inter row number"))
for i in range(1,n2+1):
    print(" "*(n2-i+1),(str(i)+" ")*(2*i-1))

#12
print("This is patter no == ",count)
count+=1
n = int(input("inter row number"))
for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(1,i):
        print(chr(i-j+65),end=" ")
    for k in range(0,i):
        print(chr(k+65),end=" ")
    print()

#13
print("This is patter no == ",count)
count+=1
nm = int(input("inter row number"))
for i in range(1,nm+1):
    print(" "*(nm-i),end=" ")
    for j in range(1,i+1):
        print(nm-j,end=" ")
    print()
for k in range(1,nm):
    print(" "*k,end="")
    for l in range(1,nm+1-k):
        print(nm-l ,end=" ")
    print()
#14
print("This is patter no == ",count)
count+=1
num = int (input('row'))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(num-j,end=" ")
    print()

for a in range(1,num+1):
    for k in range( 1, num+1-a):
        print(num-k,end=" ")
    print()

#!5
print("This is patter no == ",count)
count+=1
num = int (input('row'))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for a in range(1,num+1):
    for k in range( 1, num+1-a):
        print("*",end=" ")
    print()
#16
print("This is patter no == ",count)
count+=1
n = int (input('row'))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(i,i+1):
        print(chr(64+i),end=" ")
        if i>=2:
            print(" "*(2*i-4),end="")
            for k in range(i,i+1):
                print(chr(64+i),end=" ")
    print()

#17 x tree
print("This is patter no == ",count)
count+=1
n = int (input('row'))
for a in range(1,n+1,2):
     for i in range(1,n+1):
        print(" "*(2*n-i-a),end=" ")
        for j in range(1,i+a):
                print("*",end=" ")
        print()
for b in range(1,n+1):
    print(" "*(n-2),end=" ")

    print("*"*3)

#18
print("This is patter no == ",count)
count+=1
n = int(input(" enter number of row "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i),end= " ")
    print()
