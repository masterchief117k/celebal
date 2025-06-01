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
    app.debug = True
    app.run()
    app.run(debug =True) 