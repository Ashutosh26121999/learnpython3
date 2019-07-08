from random import randint
# one digits random number generaton
print("Random number of one digits")
# THIS LINE GENERATS RANDOM NUMBER FROM 0 TO 9
print(randint(0,9))
print("ONE DIGITS RANDOM NUMBER GENERATED")

# OTP generator of six digits
print ("OTP Generator")
# THIS LINE GENERATS OTP
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print("OTP generated")

# OTP generator of six digits WITHOUT SPACE
print ("OTP Generator without space between number")
# THIS LINE GENERATS OTP WITOUT SPACE BY USING sep=''
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")
print("OTP generated without space")

# GENERAT OTP n NUMBER OF TIME WHICH YOU GIVE IN FOR LOOOP

print("generat OTP 7 time")
for i in range(7):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")

print("OTP generated at time")
