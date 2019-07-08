from math import pow
a=23
print(id(a))
print(type(a))
print("a value",a)
# base conversion

x=300
y=0b1010101010101
z=0x554b
o=0O5656556
print("# base conversion\n")
print(x,y,z,o,"PRINTED\n")
print("Type of x,y,z,o \t",type(x),type(y),type(z),type(o))
print("\n")

#type base conversion
print("#type base conversion\n")
print("BINARY")
print(bin(o),"=o")
print(bin(z),"=z")
print(bin(y),"=y")
print(bin(x),"=x")
print("\n")
print("OCTAL")
print(oct(o),"=o")
print(oct(z),"=z")
print(oct(y),"=y")
print(oct(x),"=x")
print("\n")
print("HEXADECIMAl")
print(hex(o),"o")
print(hex(z),"z")
print(hex(y),"y")
print(hex(x),"x")
print("POWER function\n")
print(pow(x,2),"power of ")
print("\n\t")

#fe=0b10110.001
#print(fe)