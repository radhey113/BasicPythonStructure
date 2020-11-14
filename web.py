from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
   return 'Server working fine!'

app.debug = True
if __name__ == '__main__':
   app.run('0.0.0.0', 2201)
