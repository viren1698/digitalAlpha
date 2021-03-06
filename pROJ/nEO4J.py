# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:40:46 2018

@author: user
"""

#-----------------------------------------------    
# =============================================================================
# import tika
# from tika import parser
# parsed = parser.from_file(r'C:\Users\user\Downloads\Anthem.docx', xmlContent=True)
# 
# =============================================================================


from neo4j.v1 import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "Viren@123"))


           
def createNode(title,parent,prop):
    
    with driver.session() as session:
      
        with session.begin_transaction() as tx:
            result=tx.run("CREATE (n:Subnode { name : {title} , parent : {parent} , prop:{prop} })",parent=parent,title=title,prop=prop)
          
def createMultipleRelations():
    
    with driver.session() as session:
      
        with session.begin_transaction() as tx:
            result=tx.run("MATCH (a:Subnode),(b:Subnode)  WHERE a.name = b.parent  CREATE (a)-[r:type]->(b) RETURN a,b")
  
                  
def deleteSelfRelations():
    
    with driver.session() as session:
      
        with session.begin_transaction() as tx:
            result=tx.run("MATCH (a:Subnode)-[r:type]->(a:Subnode) Delete r RETURN a")
            

import mammoth
with open(r"C:\Users\user\Desktop\Anthem.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion
f = open(r"C:\Users\user\Desktop\Anthem.html","w")
f.write(html)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html.parser')
#soup.prettify()

blacklist = ["img",'table']
for tag in soup.findAll():
        if tag.name.lower() in blacklist:
            # blacklisted tags are removed in their entirety
            tag.extract()




from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")



# =============================================================================
# 
# key_section={}
# for i in user_input_words:
#     temp=[]
#     for key,val in d_stem.items(): 
#         if i in val:
#             temp.append(key)
#     key_section[i]=temp
# # =============================================================================
# =============================================================================
# for item in word_sent[2:4]:
#         tokenized = nltk.word_tokenize(item)
#         tagged = nltk.pos_tag(tokenized)
#         print(tagged)
# 
# 
# =============================================================================

all_h1=soup.find_all('h1')

d_h1={}
for h1 in all_h1:
    first=h1
    second=first.find_next('h1')
    temp=""
    
    while first.findNext()!=second:
        if str(first.findNext().text) != "":
            temp+= str(first.findNext())+" "
        first=first.findNext()
    #if temp!=" Please see “Therapy Services” later in this section. " and temp!=' See “Therapy Services” later in this section. ' and temp!="":
    temp=temp.replace('.'," . ")
    temp=temp.replace('('," ( ")
    temp=temp.replace(')'," ) ")
    temp=temp.replace('<'," <")
    temp=temp.replace('>',"> ")
    d_h1[str(h1.text)]=temp


d_h2={}

for h1,h1_val in d_h1.items():
    d_unio={}
    soup2 = BeautifulSoup(h1_val,'html.parser')
    all_h2=soup2.find_all('h2')
    if len(all_h2)!=0 :
        for h2 in all_h2:
            first=h2
            second=first.find_next('h2')
            temp=""
        
            while first.findNext()!=second:
                if str(first.findNext().text) != "":
                    temp+= str(first.findNext())+" "
                first=first.findNext()
            #if temp!=" Please see “Therapy Services” later in this section. " and temp!=' See “Therapy Services” later in this section. ' and temp!="":
            temp=temp.replace('.'," . ")
            d_unio[h2.text]=temp
        d_h2[str(h1)]=d_unio
    else:
        d_h2[str(h1)]={str(h1):h1_val}
        print("--------------------")


    

for item,value in d_h2.items():
    print(item,"\n",value,'-----------------','\n')    
    



d_kwds={}
for key,val in d_h2.items():
#    print(val,"\n\n\n")
    for key2,val2 in val.items():
#        print("dsadad\n",key2)
        if val2 is not None:
            sents = sent_tokenize(val2)
            word_sent = word_tokenize(val2.lower())
            _stopwords = set(stopwords.words('english') + list(punctuation)+['·',
      '’',
      '“',
      '”'])
            section_words=[word for word in word_sent if word not in _stopwords]
            d_kwds[key2]=list(word for word in set(section_words) if (word.isalpha() and len(word)>2 and len(set(word))!=1))
        
        
        
    
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
    
    


    
    
#user_input=input("please enter your query:\n")
user_input="am i eligible for wheelchair benefits"
sents = sent_tokenize(user_input)
word_sent = word_tokenize(user_input.lower())
_stopwords = set(stopwords.words('english') + list(punctuation))
user_input_words=[word for word in word_sent if word not in _stopwords]
user_input_words=[stemmer.stem(i) for i in user_input_words]
user_input_words=[i for i in user_input_words if (i in new_bag and i not in ('claim','want','know','cover','elig'))]


key_section={}
for i in user_input_words:
    temp=[]
    for key,val in d_stem.items(): 
        if i in val:
            temp.append(key)
    key_section[i]=set(temp)


if len(key_section.keys())!=0:    
    final_cmn_section= list(set.intersection(*map(set,key_section.values())))





#for i in final_cmn_section:
#    #print(i)
#    if len(d_ms[i].split())>250:
#        sents = sent_tokenize(d_ms[i])
#    #print(sents)
#        for sen in sents:
#            checklist=sen.lower().split()
#            checklist=[stemmer.stem(y) for y in checklist]
#            
#        #print(checklist,"\n")
#            if all(x in checklist for x in user_input_words):
#                print(sen,"\n")
#    else:    
#        print(i,"\n",d_ms[i],"\n\n\n")

#            
print("Parents are-- \n",final_cmn_section)




#def find_parent_data(lis,kwds):
##    print(kwds,lis)
#    for i in lis:
#        for key,val in d_h2.items():
#            for key2,val2 in val.items():
#                if i==key2:
##                    print("---------",key2)
#                    soup4= BeautifulSoup(val2,'html.parser')
#                    ps=soup4.find_all('p')
#                    for p1 in ps:
#                        checklist=(str(p1)).lower().split()
#                        checklist=[stemmer.stem(y) for y in checklist]
##                        print(checklist)
##                        print(p1)
#                        if any(x in checklist for x in kwds):
#                            print(p1,"\n")
##                else:
##                    print("else")
##                    print("<strong>"+key2+" :</strong><br>\n")
##                    print(val2,"\n\n")
#            


def find_parent_data(lis,kwds):
#    print(kwds,lis)
    res=""
    for i in lis:
        for key,val in d_h2.items():
            for key2,val2 in val.items():
                if i==key2:
#                    print("---------",key2)
#                    print("---",key2)
                    soup4= BeautifulSoup(val2,'html.parser')
                    ps=soup4.find_all('p')
                    for p1 in ps:
#                        print(p1)
                        checklist=str(p1).lower().split()
                        checklist=[stemmer.stem(y) for y in checklist]
#                        print(checklist)
#                        print(p1)
                        if all(x in checklist for x in kwds):
#                            print(p1,"\n")
                            res+=str(p1.text)+"<br>"+"first if"
#                            print("iiffififif")
                        else:
                            if any(x in checklist for x in kwds):
                                res+=str(p1.text)+"<br>"
                                
    return res                      
#                    if len(res.strip())==0:
#                        for p1 in ps:
#                            checklist=str(p1).lower().split()
#                            checklist=[stemmer.stem(y) for y in checklist]
##                        print(checklist)
##                        print(p1)
#                        if any(x in checklist for x in kwds):
##                            print(p1,"\n")
#                            res+="dadsad"+str(p1)+"<br>"+"ddd"
                    

res=find_parent_data(final_cmn_section,user_input_words)    
#print(res)


soupt = BeautifulSoup(html,'html.parser')
trows = soupt.find_all('tr')

if len(final_cmn_section)==0:
    print("our customer representative will contact you shortly")
else:
    for i in final_cmn_section:
        temp=i.split('and')
#        print(temp)
        i=temp[0]
        print(i)
        for tr in trows:    
#            print(tr)
            if "See" in tr.text and i.strip() in tr.text:
                print("see sectuibn")
                continue
                
            elif i.strip() in tr.text:
                section_tr=tr
                print("\n\n------\n\n",section_tr)
            
     
        


print(d_h2)   

main_counter=0
for key,value in d_h2.items():
    main_counter+=1
    print(str(main_counter)+"out of "+str(len(d_h2)))
    parent=key.strip()
    createNode(parent,"root","")
    for key1,value1 in value.items():
        createNode(key1.strip(),parent,value1)    
        
        
createNode("root","","")    ## create root node
createMultipleRelations()
deleteSelfRelations()
            
  
