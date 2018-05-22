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

import pandas as pd 
import numpy as np

stemmer = SnowballStemmer("english")

templates_co = ["The coinsurance for this benefit is ","Coinsurance for your plan is ",
                "Your coinsurance is ","The coinsurance mentioned in your plan is ",
                ]

#import pandas as pd
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
#from initialprocess import *

class ActionCopi(Action):
    def __init__(self):
        f = open(r"data\Anthem1.html","r")
        self.html=f.read()
        self.soup = BeautifulSoup(self.html,'html.parser')
    def name(self):
        return 'action_copi'
    
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
        if len(key_section.keys())!=0:    
                final_cmn_section= list(set.intersection(*map(set,key_section.values())))
        return final_cmn_section


    
    
            
    def run(self, dispatcher, tracker, domain):
        d_h1=self.get_dh1(self.soup)
        d_h2=self.get_dh2(d_h1)
        kwds=self.get_kwds(d_h2)
        stem=self.get_stem(kwds)
        bog=self.get_bag_of_words(stem)
        query=tracker.get_slot('service')        
        words=self.tokenize_user_input(query,bog)
        key_section=self.get_key_section(words,stem)

        list_of_predicted_section = self.final_output_data(key_section,words,d_h2)           
        excel_file=pd.read_excel(r'data\coinsurance-data-final.xlsx','Sheet1')
        list_of_section=list(excel_file['sections'])
        excel_file.set_index("sections", inplace=True)						        
        
        
        for section in list_of_predicted_section:
            section = section.strip()
            section = section.split('and')[0]
            section = section.strip()
            for table_section in list_of_section:         
                if(section in table_section):
                    data = excel_file.loc[table_section]
                    if(data['coinsurance'] is np.nan):
                        response = "Coinsurance details are not availble for the given query"
                    else:
                        response = templates_co[np.random.randint(len(templates_co))]+ str(data['coinsurance'])
                    if (data['other-data'] is not np.nan):
                        response+= "<br><br>"
                        response += str(data['other-data'])
        dispatcher.utter_message(response)        
        return [SlotSet('service',query)]        
        
