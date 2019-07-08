print("TEST ON THE FLOAT DATA TYPE")
f=2093.032
print("id of 'f'\t",id(f),"class of 'f'\t",type(f))
print("\n")
print("this line generates error\n")
#g=0o452.74
#h=0b101010.001
#j=0x73ACC.ABC

print("error printed\n")
print("expontaial")
e=3.2e2
print("exponent of e varibel=",e,"id of e=",id(e),"type of e=",type(e))

#complex
print("\n\n\tTEST ON THE COMPLEX DATA TYPE")
c=2+3j
print("id of 'c'\t",id(c),"class of 'c'\t",type(c), "value of 'c'",c)
print("\n")
print("this line generates error\n")
#test= 23+5i

op=0o265+23j
print("op=",op)

iop=0o265+5.0j
print("iop=",iop)


#poi=80+0xAbc6j
print("poi= error")

print("checkin real and imagenary part of complex data type\n")
print('real of c=',c.real)
print('imagenary of c=',c.imag)

print("\n\n\tTEST ON THE BOOL DATA TYPE")
tr=True
fa=False
print("id of 'tr'\t",id(tr),"class of 'tr'\t",type(tr), "value of 'tr'",tr)
print("id of 'fa'\t",id(fa),"class of 'fa'\t",type(fa), "value of 'fa'",fa)
print("this line generates error\n")
#tri=true
#print(tri)


print("magice\n")
print("sum of tr+tr",tr+tr)
print("sum of fa+fa",fa+fa)
print("sum of tr+fa",tr+fa)


print("\n\n\tTEST ON THE STR DATA TYPE")
s='peterson '
print("id of 's'\t",id(s),"class of 's'\t",type(s), "value of 's'",s,"length of s ",len(s))
print("\nthis line not execute BECAUSE in is multline\n")
#pp="operation is on many members of our team
#is die and many are inhell in battelfield"

print("oops!!!!!!!! generat SOL error \n")
print("this line execute\n")
ppp=""" operation is on, many members of our team 
is die and many are inhell in battelfield, also our 'commender' id die"""
print("multline =",ppp)
