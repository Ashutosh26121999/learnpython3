# 1 PROGRAM
s= "python"
print(s[0])
print(s[-1])
print(s[2])
print(s[-3])
print(s[-5])
# 2 PROGRAM
ss=input("Enter some string:")
i=0


for x in ss:
    print("positive index of character:{} and at nagative index:{} is {}".format(i,i-len(ss),x))
    i=i+1
    print("\2n")
    print(ss[-3:-7:-1])
    print(ss[1:6:1])
