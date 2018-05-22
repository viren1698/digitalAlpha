from flask import Flask, render_template, flash, request,Markup
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from Anthem_POC import data_parsing
from Anthem_POC import clean_up_sentence
from Anthem_POC import bow
from Anthem_POC import question_from_class
from keras.models import load_model
import numpy as np
import json
#### Neo 4j Integration ####
from neo4j.v1 import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "Viren@123"))

def getChildFromParent(name):
    data_dict={}
    with driver.session() as session:
         with session.begin_transaction() as tx:
            for record in tx.run("Match (p:subnode{title:{name}})-[:Types]->(s:subnode) return s",name=name):
                data_dict[record["s"]["title"]]=record["s"].properties            
    return data_dict

def getInformation(name):
    information_dict = {}
    with driver.session() as session:
         with session.begin_transaction() as tx:
            
             
#            print(str(tx.run("MATCH (tom {name: \"Tom Hanks\"}) RETURN tom")))
            for record in tx.run("Match (p:subnode) where p.title={name} return p",name=name):
#                print(record["s"].properties)
#                dicttt[record["p"]["title"]]=record["p"].properties
#                print(record["p"].properties)
                dd=record["p"].properties
                for k,v in dd.items():
                    if(k== "title" or k =="parent"):
                        pass                        
                    else:
                        information_dict[k]=v

    return information_dict



def doesNodeExist(name):
    with driver.session() as session:
         with session.begin_transaction() as tx:
             flag=False
             for record in tx.run("Match (p:subnode) where p.title={name} return p",name=name):
                flag=True
    return flag
                


   
# App config.
DEBUG = True
app = Flask(__name__,static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
class ReusableForm(Form):
    name = TextField('Query:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    child_data_dict = {}
    information_data_dict = {}
    print(form.errors)
    if request.method == 'POST':
        response = ''
        query = request.form['name']        
        model = load_model('anthem_model.h5')
        json_data = json.load(open('Anthem_data.json', 'r'))
        probability = model.predict(np.array(bow(query)).reshape(1, len(bow(query))))[0]
        """
        try:
            response = question_from_class(json_data, query, probability[0])
            
        except Exception:
            response = 'Please contact customer care representative.'
        """
        if form.validate():
            # Save the comment here
            if(doesNodeExist(query)):                
                child_data_dict = getChildFromParent(query)            
                if(child_data_dict == {}):
                    information_data_dict = getInformation(query)
                    for key,value in information_data_dict.items():
                        response += key
                        response +=":"
                        response +=value
                        response +="<br>"            
                else:
                    information_data_dict = getInformation(query)
                    if(information_data_dict!={}):
                        for key,value in information_data_dict.items():
                            response += key
                            response +=":"
                            response +=value
                            response +="<br>"                            
                    response+="<br>Were you looking for information on these?<br>"
                    for key,value in child_data_dict.items():                    
                        response += "<a href='#' onclick='submitChildData(this.textContent)'>"+str(key)+"</a>"+", "                    
            else:
                    response="Sorry, we dont' have this information with us"
            flash(query)
            flash(response)           
        else:
            flash('')
            flash('Please enter a query.')         
    
    return render_template('anthem_poc_template.html', form=ReusableForm())

if __name__ == "__main__":
    app.run()