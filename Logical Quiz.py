import random
total = 0
#score calcu
def score( num):
    global  total
    if num == 3:
        total+=num
        print("\t \t your currrent score==",total)
        print("\n" )

    else:
        total-=1
        print("\tyour currrent score==",total)



# reco_of_Q function recognize the question
def reco_of_Q (qUestions, op1,op2,op3,op4,correctans):
    A,B,C,D= op1,op2,op3,op4
    print('\t',qUestions)
    print('\t (A):',A,'\t (B):',B,'\t(C):',C,'\t (D):',D,'\t')
    Ans = eval(input("\t enter  option"))
    if Ans == correctans :
        curret_ans(qUestions,Ans)
        score(3)
    else:
        print("\t !!!!!  your Answer  is wrong  !!!!! ")
        print("\t correct Answer  is  :",correctans)
        score(1)
        print("\n")

# correct answer Function
def curret_ans(qustion,ans):
    print("\tCongratulation your Answer is correct\t")
    print('\t\t',qustion,ans,' ')
# Questions function
def questions( Q_no):
    if Q_no == 0:
        reco_of_Q('''if the following series is written in reverse order and then all the vowels are deleted which will be the 8th letter from the right in the new series? 
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z''','L','H','K','None of these','K')
    elif Q_no == 1:
        reco_of_Q('''in the following series, how many BCN occur in such a way that Ci in the middle and B and N are on any one side?
        B C M X N C X N B X N C B N C B Y B C X N B C N A B O N M Z C B ''',4,2,5,3,3)
    elif Q_no == 2:
        reco_of_Q(''' How many T's are both immediately preceded and followed by 'E' in  the following series?
         E T E T T M E E E T E T E T E T T E E T T T E E E T E T E T E T T E E T E''',7,6,5,8,8)
    elif Q_no == 3:
        reco_of_Q(''' If the letter of word 'DOLPHIN' are arranged as they  appear in the english alphabetical order which of the following letter will be the 5th from left?''','O','D','I','None of these','None of these')
    elif Q_no == 4:
        reco_of_Q('''Number of letters skipped in between the adjacent letters in the series is one?''','KMPQR','HJLMO','PRSUN','EGIKM','EGIKM')
    elif Q_no == 5:
        reco_of_Q('In acertain code SOBER  is  written as  RNADQ  How  LOTUS  can be written in that code?','KNSTR','MPUWT','KMSTR','LMRST','KNSTR')


#Question selection
for coz in range(10):
    q = random.randint(0 ,7)
    questions(q)
