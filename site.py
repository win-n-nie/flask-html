from flask import Flask, render_template
import requests
from jinja2 import Template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/other/')
def other_page():
    return render_template('other_page.html')
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)