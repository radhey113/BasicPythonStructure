from flask import Flask
import utils
import api
import controllers
import config

app = Flask(__name__)
api.loadRoutes(app)
app.debug = True

def run():
    if __name__ == "bin.server":
       app.run('0.0.0.0', config.SERVER_PORT)
