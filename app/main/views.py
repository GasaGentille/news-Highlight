from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_source,search_source
from .forms import SourceForm
from ..models import Article

# Views
@main.route('/')
def index():