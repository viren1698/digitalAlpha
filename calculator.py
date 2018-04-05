condition=int(input("enter:-> \n 1: to find  factorial of a number "
                    "\n 2: to find lcm \n 3: to find hcf \n 4: factors of a num"))
if(condition==1):
    num=int(input("enter number"))
    r=1
    for i in range(1,num+1):
        r=r*i
    print("factorial of "+str(num)+" is "+str(r))

elif(condition==2):
    num1=int(input("enter first no"))
    num2=int(input("enter second no"))
    if (num1 <= num2):
        numm = num1
        numm2= num2
    else:
        numm = num2
        numm2=num1
    i=1
    while(1):
        if ((numm2*i)%numm==0):
            print("LCM found="+str(numm2*i))
            break
        i=i+1

elif(condition==3):
    num1=int(input("enter first no"))
    num2=int(input("enter second no"))
    if(num1<=num2):
        numm=num1
    else:
        numm=num2

    for i in range(numm,1,-1):
        if(num1%i==0 and num2%i==0):
            print("HCF of "+str(num1)+"and "+str(num2)+" is "+str(i))
            break

elif(condition==4):
    num = int(input("enter number"))
    print("factors of "+str(num)+" are:")
    for i in range(1, num):
        if(num%i==0):
            print(i)





