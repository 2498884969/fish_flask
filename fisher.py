
from mapp import create_app

app = create_app()

if __name__ == '__main__':
    # nginx + uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], threaded=True)
