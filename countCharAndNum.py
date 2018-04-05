st=input("enter something")
alpha=0
charr=0
for i in range(st.__len__()):
    if(st[i].isalpha()):
        alpha=alpha+1
    elif(st[i].isnumeric()):
        charr=charr+1

print("no of alphabets="+str(alpha))
print("no of digits="+str(charr))
