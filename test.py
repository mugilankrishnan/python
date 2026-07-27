n=input()
words=input().split()
max_len=0
result=""
for word in words:
    if len(word)%2==1 and len(word)>max_len:
        max_len=len(word)
        result=word
if result:
    print(result)
else:
    print("better luck next time")


    