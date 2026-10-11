import os
from flask import Flask
app = Flask(__name__) 

# @app.route('/')
def hello():
    return 'Hello!'
# @app.route('/hello' )
def hello_world():
    return 'Hello, World!'
app.add_url_rule('/','hello',hello)
app.add_url_rule('/hello','hello_world',hello_world)

if __name__=='__main__':
    # Debug mode exposes an interactive code console; enable it only locally via FLASK_DEBUG=1
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1") 