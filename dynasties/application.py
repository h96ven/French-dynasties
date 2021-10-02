from flask import Flask
from flask import render_template
from dynasties import *


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/main')
def main_page():
	return render_template('main.html')

@app.route('/<name>')
def child_page(name=None, years=None, founder=None, image=None):
    for dynasty in dynasties_list:
        if dynasty[0] == name:
            years = dynasty[1]
            founder = dynasty[2]
            image = dynasty[3]
    return render_template('child.html', name=name, years=years, \
        founder=founder, image=image)

if __name__ == '__main__':
	app.run(debug=True)