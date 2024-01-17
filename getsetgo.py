from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return <html><body><h1> Welcome to homepage</h1></body></html>
    

@app.route('/home/<username>')
def username_display(username):
    return username


if __name__ == '__main__':
    app.run(debug=True)
