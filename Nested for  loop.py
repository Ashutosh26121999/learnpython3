# 1 pattern
s = int(input("enter the number of row "))
for  i  in range(1,s+1): # i represent row number
    for j in  range(i): # j represent  the number of *
        print('*',end=" ")
    print()

# 2 pattern
sq= int(input("enter row"))
for p in range(0,sq):
    for q in range(sq):
            print(" *", end=" ")
    print()

w =  int(input("enter rows00"))
for t in range( 1, w+1):
    print(" *"*t)

po = int(input("enter rows01"))
for u in range( 0,po):
    for v in range(0,po):
        print(v, end=" ")
    print()


