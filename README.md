## Flask App serving API and dash apps as pages.

Initialize the site with wsgi.py
Each dash app is a self-contained folder in the folder

Things to note:
1. Wrap the dash app inside a function. This will require rerouting many of the relative links in the folder.
2. The dashapps use the assets folder in the same init.py file for the flask app (IE putting the css and .ico files in there will work by default. Alternatively, you may also append your own css in the external stylesheets argument when initializing the dashapp. (Commented code in dashboard.py)

##When launching the app:

Go to conda environment.
run wsgi.py file 'python wsgi.py'
navigate to sample dash apps at localhost:8050/dashapp

### TO DO

- Include a Procfile if deployment on Heroku
- Include Dockerfile
- Azure deployment..?
