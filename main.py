from flask import Flask, render_template
from flaskwebgui import FlaskUI

app = Flask(__name__)
# ui = FlaskUI(app,start_server='flask')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/fileComparison')
def fileComparison():
    return render_template('fileComparison.html')


@app.route('/database')
def database():
    return render_template('database.html')


@app.route('/filePrimaryKeys')
def filePrimaryKeys():
    return render_template('filePrimaryKeys.html')


if __name__ == '__main__':
    app.run(debug=True)
    # ui.run()