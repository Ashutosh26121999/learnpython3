#immutabel type
print("\n\n\n\t\t\tImmutabel in python\n\n\n\t\t\t")
v="Toor"
m="city"
mp="state"
ds="ghazipur"
DS="GHAZIPUR"
nn="city"
nm="State"
opn="STATE"


print("\nv=>",v,"id of v=>",id(v),"\n\t")
print("\nm=>",m,"id of m=>",id(m),"\n\t")
print("\nmp=>",mp,"id of mp=>",id(mp),"\n\t")
print("\nds=>",ds,"id of ds=>",id(ds),"\n\t")
print("\nnn=>",nn,"id of nn=>",id(nn),"\n\t")
print("\nnm=>",nm,"id of nm=>",id(nm),"\n\t")
print("\nopn=>",opn,"id of opn=>",id(opn),"\n\t")

if(id(m)==id(nn)):
    print("id of m & nn == True")
else:
    print("false m & nn")

print("\n\n\t",nn is m,"11")
print("\n\n\t",ds is v,"12")
print("\n\n\t",ds is DS,"13")

if(id(mp)==id(nm) & id(nm)== id(opn)):
    print("true")
else:print("false !!!!!!!!!!!!!!")

#checking immutabilty on range
print("\n\n\n\t#######------ #checking immutabilty on range #-------#########\n\n\n")
r1=258
r2=258
print("r1 is r2",r1 is r2)
print("id of r1",id(r1),"id of r2",id(r2))

r3=257
print("r1 is r3",r1 is r3)
print("id of r1",id(r1),"id of r3",id(r3))

f1=9.8
f2=9.08
print("id of f1:",id(f1),"id of f2:",id(f2),"\n f1 is f2",f1 is f2)
print("because float not support reusing concept")

c1=9.8+6j
c2=9.8+6j
print("id of c1:",id(c1),"id of c2:",id(c2),"\n c1 is c2",c1 is c2)
print("because complex not support reusing concept")
