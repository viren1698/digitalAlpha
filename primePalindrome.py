prime = []
for a in range(900,1001):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        prime.append(str(a))
print(prime)
prime_palindrome = []
for i in range(len(prime)):
    if(prime[i] == prime[i][::-1]):
        prime_palindrome.append(prime[i])
print(prime_palindrome)
