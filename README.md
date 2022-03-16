Structure:
```
├── app
├── __init__.py
│   ├── logProfile.py
│   ├── makeQueries.py
│   ├── parseParams.py
│   ├── renderPage.py
│   ├── search.py
│   ├── static
│   │   ├── css
│   │   │   ├── mw.ui.css
│   │   │   └── startist.css
│   │   ├── img
│   │   │   ├── favicon.png
│   │   │   └── startist-logo.png
│   │   └── js
│   │       ├── collapsers.js
│   │       ├── index.js
│   │       ├── sorting.js
│   │       └── tablesort.js
│   ├── templates
│   │   ├── index.html
│   │   └── results.html
│   └── views.py
├── LICENSE
├── README.md
├── requirements.txt
├── run.py



```

Basic invocation of the program:
```
cd startist
python -m venv venv
source venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
```