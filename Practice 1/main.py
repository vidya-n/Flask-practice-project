from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def index():
    return 'Welcome to Homepage!'

@app.route("/contact", methods= ['GET'])
def contactpage():
    if request.method == 'GET':
        if (request.args.get('firstname' and 'lastname') == None):
            return render_template('contact.html')
        """elif (request.args.get('firstname' or 'lastname') == ''):
            return "<html><body><h1> Invalid First Name or Last Name</h1></body></html>"
        elif (request.args.get('firstname')):
            return "<html><body><h1> First name entered</h1></body></html>"
        else:
            return "<html><body><h1> Last name entered</h1></body>"
""" #incomplete

if __name__ == "__main__":
    app.run(debug=True)
