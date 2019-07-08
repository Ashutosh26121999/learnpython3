# bytes DAta type
print("<----------------# bytes DAta type  #---------------->")
byta=[10,20,30,55,12]
byt=bytes(byta)

print("id of byt =>",id(byt),"type of byt: ",type(byt))
print("byt [0]::::",byt[0])
print("byt [-5]::::",byt[-5])
print("byt [3]::::",byt[3])
print("byt [0:-5]::::",byt[0:-5])#print garbage value
print("byt [0:4]::::",byt[0:4])#print garbage value
#"this line give error"-----------byt[3]="g2g"
print("new byt ")
for t in byt: print(t)

# bytearray DAta type
print("\n\n\n<----------------# bytearray DAta type  #---------------->\n\n\n")
bytaa=[10,20,30,55,12]
bytr=bytearray(bytaa)

print("old bytr :;" )
for u in bytr:print(u)
print("id of bytr =>",id(bytr),"type of bytr: ",type(bytr))
print("bytr [0]::::",bytr[0])
print("bytr [-5]::::",bytr[-5])
print("bytr [3]::::",bytr[3])
print("bytr [0:-5]::::",bytr[0:-5])#print garbage value
print("bytr [0:4]::::",bytr[0:4])#print garbage value
bytr[3]=218
print("new bytr :;")
for u in bytr:print(u)

print("\n\n\n\n<-----!!!!!!!!!!!!!-----[ bytes & bytearray NOT USE STRING CONCEPT ]-----!!!!!!!!!!!!!----->\n\n\n")

print("\n\n\n\n<-----!!!!!!!!!!!!!-----[ List data type ]-----!!!!!!!!!!!!!----->\n\n\n")

l1=[]
print("type of l1",type(l1))
l1.append(10)
l1.append(22)
l1.append("loop")
l1.append(10)
l1.append(None)
print("\n List l1:",l1*2,"\t\n\n")
l2=[100,'thougent',10.20,600]
pp=l1.__add__(l2)
print(pp,"663")

l1[2]='55pop'
l1.append(bytr)# in list bytes and bytarray are added
print("list l1 after modefy:",l1)

print("\n\n\n\n<-----!!!!!!!!!!!!!-----[ tuppel data type ]-----!!!!!!!!!!!!!----->\n\n\n")
t1=(77,'kw3',90.0933,7+44j)
t2=(77,'kw3',90.0933,7+44j,l1)
print("t1 type:",type(t1),"tuppel t1++",t1)
#give error :>>     t1[0]=7.3
print("t1=",t1)
print("added:::::::",t1.__add__(t2))

print("\n\n\n\n<-----!!!!!!!!!!!!!-----[ Renge data type ]-----!!!!!!!!!!!!!----->\n\n\n")
r1=range(11)
print(property(range),"type::",type(r1))
print("range of r1:;",r1)
for r in r1:print("NEW\n",r)
# ERROR!!!!!!!::r1[3]=44

r2=range(0,46)
for rr in r2: print('\n\nr2',rr)
r3=range(1,65,5)# its therd perameteter not suppor float value
for rrr in r3:print("\n\n\nr3",rrr)

print("\n\n\n\n<-----!!!!!!!!!!!!!-----[ set data type ]-----!!!!!!!!!!!!!----->\n\n\n")
s1={2,4,5,'set',7,2}
st=set(s1)
print("typeof st",type(st),"value:///:",st)
st.add(900)
st.add("SET")
st.remove("set")
print(st,"after update")
print("\n\n\n\n<-----!!!!!!!!!!!!!-----[ frozenset data type ]-----!!!!!!!!!!!!!----->\n\n\n")
s2={4,16,25,'Set',49,24}
fst= frozenset(s2)
print("typeof fst",type(fst),"\t\fvalue of fst:///:",fst)
#fst.add(900)
#fst.add("SET")
#fst.remove("set")
print(fst,"fst after update")
print("\n\n\n\n<-----!!!!!!!!!!!!!-----[ frozenset data type ]-----!!!!!!!!!!!!!----->\n\n\n")
d1={}
print("typevof d1:-:",type(d1))
d1['r32']="dictonry"
d1[4]="dictonry"
d1[4]=77
d1[5]=7.77
d1[43]=5477
d1[33]=l1
print("in d1:",d1)
d1[33]=t1
print("after update in d1:",d1)
