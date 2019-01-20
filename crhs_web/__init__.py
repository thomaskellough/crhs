from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd5e8ddf6cf1a71d142f385b8acce166d'

from crhs_web import routes
