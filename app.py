from flask import Flask, jsonify, request, render_template
import requests

app = Flask("My First Application")

@app.route('/')
def hello():
    return "<b>Hello Ji!</b>"

@app.route('/sample')
def getSampleHtml():
    return render_template('sample.html')

@app.route('/username/<string:username>', methods=['GET'])
def greetUser(username):
    return render_template('greet.html', username=username)

if __name__ == "__main__":
    app.run(debug=True)