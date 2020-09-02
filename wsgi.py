"""Application entry point."""
from flaskapp import create_app

app = create_app()
#CORS support
from flask_cors import CORS, cross_origin
CORS(app)

## Serves on https
# if __name__ == '__main__':
#       app.run(host='0.0.0.0', port=8050, ssl_context='adhoc')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8050)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8050)
