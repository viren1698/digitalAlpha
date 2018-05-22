from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem.snowball import SnowballStemmer
import numpy as np
stemmer = SnowballStemmer("english")

template_response = ["Here are the benefits you asked for.","The benefits for your plan are as follows:",
                     "These are the benefits you asked for","This is the list of all the benefits under your plan",
                     "Below are all the benefits you asked for","These are the expected benefits in your plan",
                     "You can have a look at your benefits here","Here you go",
                     "Your benefits are:","These are all the benefits"]


#import pandas as pd
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
#from initialprocess import *

class ActionBenefit(Action):
    def __init__(self):
        f = open(r"C:\Users\user\Desktop\POC-UI-master\Anthem_prototype_1\Anthem1.html","r")
        self.html=f.read()
        self.soup = BeautifulSoup(self.html,'html.parser')
    def name(self):
        return 'action_benefit'
    
    def tokenize_user_input(self,user_input,new_bag):
        word_sent = word_tokenize(user_input.lower())
        _stopwords = set(stopwords.words('english') + list(punctuation))
        user_input_words=[word for word in word_sent if word not in _stopwords]
        user_input_words=[stemmer.stem(i) for i in user_input_words]
        user_input_words=[i for i in user_input_words if (i in new_bag and i not in ('health','claim','want','know','cover','elig','insur','plan'))]
        return user_input_words
    
    def get_key_section(self,user_input_words,d_stem):
        key_section={}
        for i in user_input_words:
            temp=[]
            for key,val in d_stem.items():
                 if i in val:
                     temp.append(key)
            key_section[i]=set(temp)
        return key_section

    def get_dh1(self,soup):
        d_h1={}
        all_h1=soup.find_all('h1')
        for h1 in all_h1:
            first=h1
            second=first.find_next('h1')
            temp=""
        
            while first.findNext()!=second:
                if str(first.findNext().text) != "":
                    temp+= str(first.findNext())+" "
                first=first.findNext()
            temp=temp.replace('.'," . ")
            temp=temp.replace('('," ( ")
            temp=temp.replace(')'," ) ")
            temp=temp.replace('<'," <")
            temp=temp.replace('>',"> ")
            d_h1[str(h1.text)]=temp
        d_h1.pop('Section 4. Table of Contents')
        return d_h1

    def get_dh2(self,d_h1):
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
                    temp=temp.replace('.'," . ")
                    d_unio[h2.text]=temp
                d_h2[str(h1)]=d_unio
            else:
                d_h2[str(h1)]={str(h1):h1_val}
        return d_h2
    
    
    def get_kwds(self,d_h2):
        d_kwds={}
        for key,val in d_h2.items():
            for key2,val2 in val.items():
                if val2 is not None:
                    word_sent = word_tokenize(val2.lower())
                    _stopwords = set(stopwords.words('english') + list(punctuation)+['·',
              '’',
              '“',
              '”'])
                    section_words=[word for word in word_sent if word not in _stopwords]
                    d_kwds[key2]=list(word for word in set(section_words) if (word.isalpha() and len(word)>2 and len(set(word))!=1))
        return d_kwds
    
    
    def get_stem(self,d_kwds):
        d_stem={}
        for key,val in d_kwds.items():
            singles = [stemmer.stem(i) for i in val]
            temp=set(singles)
            d_stem[key]=list(temp)
        return d_stem
    
    def get_bag_of_words(self,d_stem):
        bag_of_words2=[]
        for i,j in d_stem.items():
            bag_of_words2.append(j)
        new_bag=[]
        for list_word in bag_of_words2:
            for i in list_word:
                if i.isalpha():
                    new_bag.append(i) 
        new_bag=list(set(new_bag))
        return new_bag
    
    
    def find_parent_data(self,lis,kwds,d_h2):
        res=""
        res2=""
        for i in lis:
            res+="<h3>"+i+"</h3>"
            res2+="<h3>"+i+"</h3>"
            for key,val in d_h2.items():
                for key2,val2 in val.items():
                    if i==key2:
                        soup4= BeautifulSoup(val2,'html.parser')
                        ps=soup4.find_all('p')
                        for p1 in ps:
                            checklist=str(p1).lower().split()
                            checklist=[stemmer.stem(y) for y in checklist]
                            if all(x in checklist for x in kwds):
                                res+=p1.prettify()
                                res2+=p1.prettify()
        return res
    
    def final_output_data(self,key_section,user_input_words,d_h2):
        final_cmn_section=[]
        final_output=""
        if len(key_section.keys())!=0:    
                final_cmn_section= list(set.intersection(*map(set,key_section.values())))
                final_output+=self.find_parent_data(final_cmn_section,user_input_words,d_h2)   
#                soupTable= BeautifulSoup(self.html,'html.parser')
#                trows = soupTable.find_all('tr')
#                if len(final_cmn_section)==0:
#                    final_output+="our customer representative will contact you shortly"
#                else:
#                    for i in final_cmn_section:
#                        temp=i.split()
#                        if len(temp)>=3:
#                            temp=" ".join(temp[0:3])
#                        else:
#                            temp=i
#                        for tr in trows:
#                            if "See" in tr.text and temp.strip() in tr.text:
#                                continue
#                            elif temp.strip() in tr.text and ("Coinsurance" in tr.text or "Copayment" in tr.text):
#                                final_output+="<br><h4>"+"Coinsurance/Copayment details of : "+i.strip()+"</h4>"
#                                section_tr=tr
#                                final_output+=section_tr.prettify()
                            
        else:
            final_output+="our customer representative will contact you shortly"
        return final_output


    
    
            
    def run(self, dispatcher, tracker, domain):
        output = template_response[np.random.randint(len(template_response))]
        d_h1=self.get_dh1(self.soup)
        d_h2=self.get_dh2(d_h1)
        kwds=self.get_kwds(d_h2)
        stem=self.get_stem(kwds)
        bog=self.get_bag_of_words(stem)
        query=tracker.get_slot('service')                
        words=self.tokenize_user_input(query,bog)
        key_section=self.get_key_section(words,stem)        
        output += "<br><br>"
        output += self.final_output_data(key_section,words,d_h2)						        
        dispatcher.utter_message(output)
        return [SlotSet('service',query)]
        
        