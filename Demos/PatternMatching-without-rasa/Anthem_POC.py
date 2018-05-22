
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")


import mammoth
with open(r"C:\Users\user\Desktop\Anthem1.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion
f = open(r"C:\Users\user\Desktop\Anthem1.html","w")
f.write(html)

soup = BeautifulSoup(html,'html.parser')
#soup.prettify()

blacklist = ["img" ]
for tag in soup.findAll():
        if tag.name.lower() in blacklist:
            # blacklisted tags are removed in their entirety
            tag.extract()

   



all_h2=soup.find_all('h2')
    
d_ms={}
for item in all_h2:
    first=item
    second=first.find_next('h2')
    temp=""
    
    while first.findNext()!=second:
        if str(first.findNext().text) != "":
            temp+= str(first.findNext().text)+" "
        first=first.findNext()
    #if temp!=" Please see “Therapy Services” later in this section. " and temp!=' See “Therapy Services” later in this section. ' and temp!="":
    temp=temp.replace('.'," . ")
    d_ms[str(item.text)]=temp

#for item,value in d_ms.items():
 #   print(item,"\n",value,'-----------------','\n')    
    


d_kwds={}
for key,val in d_ms.items():
    if val is not None:
        sents = sent_tokenize(val)
        word_sent = word_tokenize(val.lower())
        _stopwords = set(stopwords.words('english') + list(punctuation)+['·',
  '’',
  '“',
  '”'])
        section_words=[word for word in word_sent if word not in _stopwords]
        d_kwds[key]=list(word for word in set(section_words) if (word.isalpha() and len(word)>2 and len(set(word))!=1))
        
    
d_stem={}
for key,val in d_kwds.items():
    singles = [stemmer.stem(i) for i in val]
    temp=set(singles)
    d_stem[key]=list(temp)
    


bag_of_words2=[]
for i,j in d_stem.items():
    bag_of_words2.append(j)
new_bag=[]
for list_word in bag_of_words2:
    for i in list_word:
        if i.isalpha():
            new_bag.append(i) 
new_bag=list(set(new_bag))


    