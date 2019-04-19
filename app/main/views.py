from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/pitches/<id>')
def pitches(id):

    '''
    View pitches page function that returns the pitches page and its data
    '''
    # return render_template('pitches.html',id = id, category = category)