sentence=input("Enter something :")
noOfWords=1
noOfCharacter=0
for i in sentence:
        noOfCharacter+=1
        if(i==" "):
            noOfWords+=1
print(noOfCharacter)
print(noOfWords)
