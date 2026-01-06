existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

from flask import Flask

app = Flask(__name__)

"""
Set up ‘/’ route.
Route will return “Welcome to Flatiron Cars”
"""
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

"""
Takes model variable
Using model variable and given existing_models array
If model exist in existing_models array returns
‘Flatiron {model} is in our fleet!’
If model does not exist in existing_models array return
‘No models called {model} exists in our catalog’
"""
@app.route('/<model>')
def check_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'
    