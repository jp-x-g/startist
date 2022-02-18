# JPxG, 2022 January 30
# This is very confusing, but WSGI compliance requires there be an entrypoint named "app".
# To break it down for you: this "app.py" is importing "__init__" from the directory "app".
# This __init__ happens to define an "app" (i.e. Flask(__name__)). Sorry!

from app import app

if __name__ == "__main__":
	app.run()