import os
from flask import Flask, render_template, request, g

app = Flask(__name__)


DEBUG_ON = os.environ.get('flask_debug', True)


@app.route('/welcome', methods=['POST', 'GET'])
def register():
    return render_template('welcome.html')


@app.route('/login')
def login():
    if request.method == 'POST':
        print('Username : {}'.format(request.form['username']))
        print('Password : {}'.format(request.form['password']))
    return "<html>Hello, World!</html>"


if __name__ == '__main__':
    app.run(debug=DEBUG_ON)
