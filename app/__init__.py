# JPxG, 2022 January 30
# All this does is create a new Flask called "app", and then import views.py from the directory "app".
# A little confusing because it uses the name "app" multiple times. Blame uWSGI.

from flask import Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# Prevents us from throwing the dreaded "TypeError: '<' not supported between instances of 'int' and 'str'"

from app import views