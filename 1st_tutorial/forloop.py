word=input("write word: ")
n=0
for i in word:
    if(i.lower() in "aeiou"):
        word=word[:n]+'g'+word[n+1:]
    n+=1
print(word)
        