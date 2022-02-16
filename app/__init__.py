# JPxG, 2022 January 30

from flask import Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# Prevents us from throwing the dreaded "TypeError: '<' not supported between instances of 'int' and 'str'"

from app import views