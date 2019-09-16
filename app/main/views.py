from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source
from ..models import Article


# from flask import render_template
# from app import app

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    
    # Getting News source
    title = ' Welcome to online news highlight website'
    source = get_source('technology')
    sports_source = get_source('sports')
    business_source = get_source('business')
    entertainment_source = get_source('entertainment')
    
    return render_template('index.html',title = title, technology = source,sports = sports_source,business = business_source,entertainment= entertainment_source)

@main.route('/source/<int:id>')
def source(id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(id)
    
    return render_template('article.html',id = id, article = article)