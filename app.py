from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/sample')
def getSampleHtml():
    return render_template('sample.html')

@app.route('/username/<string:username>', methods=['GET'])
def greetUser(username):
    return render_template('greet.html', username=username)

# This is only needed for local development
if __name__ == "__main__":
    app.run(debug=True)