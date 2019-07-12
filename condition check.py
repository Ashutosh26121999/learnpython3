import random

a = 3.2
if a == 3.2:
    print("QUIZ START")
else:
    print('bye bye')
print("Q1=WHO IS PESIDENT OF AMERICA\n")
a = "DONAL TRUMP"
b = "HELERAY Quntion"
c = "BARAK OBAMA"
d = "COLUMBUS"
print("a= DONAL TRUMP\t b= HELERAY Quntion\tc= BARAK OBAMA\td= COLUMBUS")
ans = eval(input("enter your answer"))
if ans == a:
    print("Your Ans is correct")
    print(" PESIDENT OF AMERICA is:\t", a)
else:
    print("incorect answer")
print("Q2=IN WITCH YEAR VASKODEGAMA FOUND INDIA\n")
print("A:1389\tB:1495\tC:1567\tD:1497\n")
print("Write your answer")
ans2 = eval(input())
if ans2 == 1497:
    print("Your Ans is correct")
    print("VASKODEGAMA FOUND INDIA in :\t", ans2)
else:
    print("incorect answer")

print("BETER LUCK NEXT TIME")

lt = ['asd', 'sdewe', 'rewerwe', 'wrwrwfd']
for tr in range(len(lt)):

    rt = random.choice(lt)
    print('rt=', rt)
