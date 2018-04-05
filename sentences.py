import re
sentence = '''#Python is an interpreted high level programming language for general-purpose programming*.'''
clean_sentence = re.sub("\W+"," ",sentence)
print(clean_sentence)
sentence_to_words = clean_sentence.split()
print(sentence_to_words)
palindrome = []
for i in range(len(sentence_to_words)):
    if(sentence_to_words[i] == sentence_to_words[i][::-1]):
        palindrome.append(sentence_to_words[i])
print()
print("The palindrome words in the sentence are as follows : ")
print(palindrome)

from collections import Counter
frequency = Counter(sentence_to_words)
print(frequency)
