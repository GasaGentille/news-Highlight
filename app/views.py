from flask import render_template
from app import app

Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = ' Welcome to online news highlight website'
    return render_template('index.html', title = title)
@app.route('/source/<int:id>')
def source(id):

    '''
    View source page function that returns the source details page and its data
    '''
    return render_template('source.html',id = id)