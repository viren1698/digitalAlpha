from flask import Flask, render_template, flash, request,Markup
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from Anthem_POC import data_parsing
from Anthem_POC import clean_up_sentence
from Anthem_POC import bow
from Anthem_POC import question_from_class
from keras.models import load_model
import numpy as np
import json
   
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
    print(form.errors)
    if request.method == 'POST':
        response = ''
        query = request.form['name']        
        model = load_model('anthem_model.h5')
        json_data = json.load(open('Anthem_data.json', 'r'))
        probability = model.predict(np.array(bow(query)).reshape(1, len(bow(query))))[0]        
        try:
            response = question_from_class(json_data, query, probability[0])
            
        except Exception:
            response = 'Please contact customer care representative.'
        
        if form.validate():
            # Save the comment here
            flash(query)
            flash(response)           
        else:
            flash('')
            flash('Please enter a query.')         
    
    return render_template('anthem_poc_template.html', form=ReusableForm())

if __name__ == "__main__":
    app.run()