
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



total=(name1+name2).lower()
l=total.count("l")
o=total.count("o")
v=total.count("v")
e=total.count("e")
t=total.count("t")
r=total.count("r")
u=total.count("u")
e=total.count("e")
love=l+o+v+e
true=t+r+u+e
love_scor=str(true)+str(love)
love_score=(int(love_scor))

if(love_score>10 or love_score<90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score<=50 or love_score>=40):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")