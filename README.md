Structure:
```
.
├── app
│   ├── __init__.py
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
├── app.py
├── data
│   └── log
│       ├── master.log
│       └── startist.log
├── LICENSE
├── README.md
└── requirements.txt
```


Installation looks like this:

```
git clone https://github.com/jp-x-g/startist

```

Basic invocation of the program:
```
cd startist
python -m venv venv
source venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
```