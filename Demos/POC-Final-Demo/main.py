from flask import Flask, render_template, flash, request,Markup
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter


def create_rasa_nlu_model():
	training_data = load_data('data/trainingDataRaw.json')
	trainer = Trainer(RasaNLUConfig("config/nlu_model_config.json"))
	trainer.train(training_data)
	model_directory = trainer.persist('models/', fixed_model_name="poc")
	return(model_directory)
	

def train_dialogue(domain_file="domain.yml",
                   model_path="models/dialogue",
                   training_data_file="stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(),KerasPolicy()])

    agent.train(
            training_data_file,
            max_history=3,
            epochs=400,
            batch_size=10,
            validation_split=0.2
    )

    agent.persist(model_path)    
# App config.
DEBUG = True
app = Flask(__name__,static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
class ReusableForm(Form):
    name = TextField('Query:', validators=[validators.required()])



@app.before_first_request
def initialize():
    global model_directory
    model_directory = create_rasa_nlu_model()
    train_dialogue()
    
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    
    interpreter = RasaNLUInterpreter(model_directory)
    agent = Agent.load('./models/dialogue', interpreter = interpreter)    
    

    
    print(form.errors)
    if request.method == 'POST':
        response = ''
        query = request.form['name']
        try:
            response = agent.handle_message(query)[0]
        except Exception:
            response=" Something went wrong with your query, Please try again later"
        
        if form.validate():
            flash(query)
            flash(response)
        else:
            flash('')
            flash('Please enter a query.')         
    
    return render_template('anthem_poc_template.html', form=ReusableForm())

if __name__ == "__main__":
    app.run()