from controllers import *

def loadRoutes(app):
    @app.route('/')
    def root():
       return rootCtrl()

    @app.route('/init')
    def init():
       return initCtrl()
