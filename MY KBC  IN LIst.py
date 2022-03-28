print("\n\t\tWELCOME IN KBC.....kaun banega coder\n")
print("\t\t`````````````````````````````````````")
print("\tnamskar! me Amitabh bachchan bol rha hu........\n\t\tkaun banega coder se\n let's play\n")
print("So first question on your screen\n")
question = [
"How many continents are there?",
"What is the capital of India?", 
"NG mei kaun se course padhaya jaata hai?" ,
"who is the founder of 'python'?","when python is published?",
"python is a ______ programming language?"
]

options = [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"],
["bill gates","guido van rossum","jeff bezoz","ratan tata"],["1989","1990","1991","1992"],
["high level","interpreted","general purpose","all of the above"]
]

solution = [4, 4, 1,2,3,4]
li=[["3 seven","4 Eight"],["2 bhopal","4 Delhi"],["1 software engineering","2 counseling"],
["1 bill gates","2 guido van rossum"],["1 1989","3 1991"],["1 high level","4 all of the above"]]

pall=[["1 four- 20%","2 nine-40%","3 seven- 80%","4 Eight- 99.9%"],
["1 chnadigarh-60%","2 bhopal- 85%","3 chennai-35%","4 Delhi- 99.9%"],
["1 software engineering- 99.9%","2 counseling- 90%","3 Tourism-65%","4 Agriculture- 20%"],
[" 1 bill gates- 90%","2 guido van rossum- 99.9%"," 3 jeff bezoz- 45%","4 ratan tata- 60%"],
["1 1989- 70%","2 1990- 40%","3 1991- 90%","4 1992- 50%"],
["1 high level- 90%","2 interpreted- 60%","3 general purpose- 70%","4 all of the above- 99.1%"]
]
experts=["1 teena dabi","2 vikash divyakirti","3 meenamma","4 miss arpita lataye"]
i=0
count=0
s=0
c=0
b=0
while i<len(question):
    print(i+1,question[i])
    print("````````````````````````````````")
    j=i
    k=0
    while k<len(options[j]):
        n=options[j][k]
        print(k+1,n)
        k+=1
    l1=input("do you want lifeline:")
    if l1=="y":
        print("you have three lifeline:-\n" )
        print("1 50-50 lifeline\n2 audience pall\n3 experts pall")
        l=int(input("Enter your number of lifeline:"))
        if l==1 and count==0:
            k=0
            while k<len(li[i]):
                print(li[i][k])
                k+=1
            print("chose any one answer which is given above\n")
            a=int(input("Enter your answer:"))
            if a==solution[i]:
                print("correct")
                s=s+1000
            else:
                print("you lost the game\n")
                break
            count+=1
        elif l==2 and c==0:
            k=0
            while k<len(pall[i]):
                print(pall[i][k])
                k+=1
            print("you want to go with audience\n")
            a=int(input("Enter your answer:"))
            if a==solution[i]:
                print("correct")
                s+=1000
            else:
                print("you lost the game\n")
                break
            c+=1
        elif l==3 and b==0:
            k=0
            while k<len(experts):
                print(experts[k])
                k+=1
            print("you want to go with expert\n")
            e=int(input("Enter expert number:"))
            if e<=4:
                print(solution[i])
            a=int(input("Enter your answer:"))
            if a==solution[i]:
                print("correct")
                s+=1000
            else:
                print("you lost the game\n")
                break
            b+=1
        else:
            print("you can use lifeline only once\n")
            a=int(input("Enter your answer:"))
            if a==solution[i]:
                print("correct")
                s=s+1000
            else:
                print("you lost the game\n")
                break
    else:
        print("okay")
        a=int(input("Enter your answer"))
        if a==solution[i]:
            print("correct")
            s=s+1000
        else:
            print("you lost the game\n")
            break
    i=i+1
print("thankyou for playing with us")
print("you won the cheque of",s,"Rs.")
       
       