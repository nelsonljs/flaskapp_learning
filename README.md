# Flask App serving API and dash apps as pages.

This is a flask app that grants some accessibility and visualization of data available on yahoo finance api.
For learning purposes, and to understand the folder structure of a dash app embedded in flask.

It uses the [yfinance package](https://aroussi.com/post/python-yahoo-finance) by Ran Aroussi.

### To use
Initialize the site with wsgi.py
Each dash app is a self-contained folder in the folder

Things to note:
1. Wrap the dash app inside a function. This will require rerouting many of the relative links in the folder.
2. The dash app use the assets folder in the same init.py file for the flask app (IE putting the css and .ico files in there will work by default. Alternatively, you may also append your own css in the external stylesheets argument when initializing the dash app. (Commented code in dashboard.py)

##When launching the app:

Go to conda environment.
run wsgi.py file 'python wsgi.py'
navigate to sample dash apps at localhost:8050/

### TO DO

- Include a Procfile if deployment on Heroku
- Include Dockerfile
- Azure deployment..?
