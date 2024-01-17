from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return <html><body><h1> Welcome to homepage</h1></body></html>

@app.route(rule='/user', methods = ['GET'])
def get_user():
    return '''
        <form method="POST">
        <div><label> Enter first name: <input type='text' name='firstname'> </label></div>
        <div><label> Enter last name: <input type='text' name='lastname'> </label></div>
        <input type='submit' value='Submit'>
        </form>'''


@app.route(rule='/user', methods = ['POST'])
def username_display():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    name = {1: firstname, 2: lastname}
    return '''
    <html><body><h1> The name associated with {1} is: {2} </h1></body></html>'''.format_map(name)



if __name__ == '__main__':
    app.run(debug=True)
