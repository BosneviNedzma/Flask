from flask import Flask, jsonify, redirect, abort
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.example.com')

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)