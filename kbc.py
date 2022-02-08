def kbc(q,o,s,l):
    print("-----------WELCOME TO KBC-------------------")
    i=0
    count=0
    sum=0
    while(i<len(q)):
        j=0
        print("Your question is here")
        print(q[i])
        while(j<len(o[i])):
            print(j+1,o[i][j])
            j+=1
        a=int(input("Enter your Answer Or Else You Can Use 5050"))
        if(a == s[i]):
            sum=sum+10000
            print("Congratulations Your Answer Is Right And You Have Won",sum)
        elif(a == 5050):
            if(count==1):
                print("Sorry You Have Already Used The 50/50 Lifeline")
                a1=int(input("Enter Your Answer:"))
            if(count<1):
                count+=1
                print(l[i][0])
                print(l[i][1])
                a1=int(input("You Have Two Options Now Choose Corrcet Answer"))
            if(a1 == s[i]):
                sum=sum+10000
                print("Congratulations Your Answer Is Right And You Have Won",sum)
            else:
                print("Your Answer Is Wrong You Lost",sum)
                print("----Game Over-----")
                break
        else:
            print("Your Answer Is Wrong You Lost",sum)
            print("----Game Over-----")
            break
        i+=1
kbc([
    "1)How many continents are there?",        
    "2)What is the capital of India?",          
    "3)NG mei kaun se course padhaya jaata hai?" 
],[
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
],
[3, 4, 1],
[["1 eight\n","3 seven"],["2 Bhopal\n","4 Delhi"],["1 Software Engineering\n","3 Tourism"]])