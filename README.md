Structure:
```
├── app
│   ├── __init__.py
│   ├── static
│   │   ├── css
│   │   │   ├── mw.ui.css
│   │   │   └── startist.css
│   │   ├── img
│   │   │   └── startist-logo.png
│   │   └── js
│   │       └── index.js
│   ├── templates
│   │   └── index.html
│   └── views.py
├── app-old.py
├── LICENSE
├── README.md
├── requirements.txt
├── run.py
└── setup.sh
```

Basic invocation of the program:
```
cd startist
python -m venv env
source env/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
```