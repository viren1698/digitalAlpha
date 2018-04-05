sentence = input("Enter the sentence")
letters = 0
digits = 0
uppercase = 0
lowercase = 0
special = 0
for i in sentence:
    print(type(i))
    if(i.isalpha()):
        letters += 1
        if(i.isupper()):
            uppercase += 1
        elif(i.islower()):
            lowercase += 1
    elif(i in '''~!@#$%^&*()_+=-~[];',./{}:"<>?\|'''):
        special += 1
    elif(i.isdigit):
        digits += 1
print('Letters = {:d}, Digits = {:d}, Upper = {:d}, Lower = {:d} and Special = {:d}'.format(letters,digits,uppercase,lowercase,special))
