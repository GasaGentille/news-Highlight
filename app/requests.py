
import urllib.request,json
from .models import Source,Article
# from datetime import datetime

# Getting api key
api_key = None
# Getting the news base url
base_url = None

# Getting the article  url
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    article_url = app.config['ARTICLE_BASE_URL']

def get_source(language):
    '''
	Function that gets the json response to our url request
	'''
    