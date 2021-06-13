from flask import Flask, render_template
from flaskwebgui import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app,start_server='flask')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/csvexcel')
def csvexcel():
    return 'This is where you will compare csv and excel'


if __name__ == '__main__':
    #app.run(debug=True)
    ui.run()