from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''<html><body><h1> Welcome to homepage</h1></body></html>'''

@app.route(rule='/user', methods = ['GET'])
def get_user():
    return f'My name is {request.args.get("firstname")} {request.args.get("lastname")}'
    

@app.route('/home/<username>')
def username_display2(username):
    return username

@app.route(rule='/user', methods = ['POST'])
def username_display():
    print(request.json)
    data = request.json
    return f'My name is {data.get("firstname")} {data.get("lastname")}. You can call me on {data.get("contact")}.'

if __name__ == '__main__':
    app.run(debug=True, port=6666)
