from flask import Flask, render_template,request,redirect,url_for
from flaskwebgui import FlaskUI
import pandas as pd

app = Flask(__name__)
#This is for Desktop app
# ui = FlaskUI(app,start_server='flask')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/fileComparison', methods =['GET', 'POST'])
def fileComparison():
    if request.method == 'POST':
        print('Inside Post')
        full_file_path= request.files.get(u'file-upload-src')
        print(full_file_path.name)
        df = pd.read_csv(full_file_path)
        print(df)
        return redirect(url_for('fileComparison'))
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