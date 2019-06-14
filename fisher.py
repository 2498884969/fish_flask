from flask import Flask


app = Flask(__name__)

from mapp.mweb import book
if __name__ == '__main__':
    # nginx + uwsgi
    app.run(host='0.0.0.0', debug=False)
