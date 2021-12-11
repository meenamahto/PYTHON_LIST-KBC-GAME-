print("\n\t\tWELCOME IN KBC.....kaun banega coder\n")
print("\t\t`````````````````````````````````````")
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

i=0
s=0
count=0
while i<len(question):
    print(i+1,question[i])
    print("```````````````````````````````")
    j=i
    k=0
    while k<len(options[j]):
        n=options[j][k]
        print(k+1,n)
        k+=1
    l=input("do you want life line if y / n :")
    if l=="y":
        if count==0:
            print("you have 50-50 lifeline\n")
            k=0
            while k<len(li[i]):
                print(li[i][k])
                k+=1
            print("chose any one answer which is given above\n")
            a=int(input("Enter your answer:"))
            if a==solution[i]:
                print("your answer is correct")
                s+=1000
                print("you won a cheque of",s,"/-\n")
            else:
                print("you lost the game\n")
                break
            count+=1
        else:
            print("you can use lifeline only once....\n")
            fa=int(input("Enter your answer:"))
            if fa==solution[i]:
                print("your answer is correct")
                s+=1000
                print("you won a cheque of",s,"/-\n")
            else:
                print("sorry! you lost the game\n")
                break

    else:
        fa=int(input("Enter your answer:"))
        if fa==solution[i]:
            print("your answer is correct")
            s+=1000
            print("you won a cheque of",s,"/-\n")
        else:
            print("sorry! you lost the game\n")
            break
    i=i+1
print("thankyou! for playing with us......")
print("you won the cheque of",s,"Rs")

