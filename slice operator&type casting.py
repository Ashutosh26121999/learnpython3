print("Let's start slice operator\n\n")
look="How was your day today"

print(look,"\n")
print("\n\nlength=",len(look))
#now using slice operator
print(look[0:5],"==look[0:5]")
print(look[:8],"==look[:8]")
print(look[:],"==look[:]")
print(look[-22:21],"==look[-22:21]")
print(look[-1:22],"==look[-1:22]")
print(look[-22:],"==look[-22:]")
print(look[:25],"==look[:25]")
print(look[4:12+4]*8 ,"==look[4:12+4]")


print("Let's start Type coersion\t\n\n")
print("INT\n\t\t")
print(int(4.5),"A")
print(int("10"),"B")
#print(int(7+5j),"C")
#print(int("loop"),"loop")

print("\f \n float\n\t\t")
print(float(4),"A")
print(float("10"),"B")
#print(float(7+5j),"C")
#print(float("loop"),"loop")

print("\f \n complex\n\t\t")
print(complex(4),"A")
print(complex("10"),"B")
print(complex(7.6),"C")
#print(complex("loop"),"loop")
print(complex(0.9,8),"D")
#print(complex(0b0101),"error")
print(complex(4,8),"E")

print("\f \n str\n\t\t")
print(str(4),"A")
print(str(10.5),"B")
print(str(7+5j),"C")
print(str("loop"),"loop")



