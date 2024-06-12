from logging import debug
from flask import Flask, render_template,request, redirect, url_for

import pandas as pd
import os

app = Flask(__name__)

headings=('S.No','Course Name','Name of the faculty member','Section','No. of Students appeared','No. of Students Passed','Pass Percentage','Course wise percentage')

app.config['UPLOAD_FOLDER'] = 'upload'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'File {filename} uploaded successfully'

@app.route("/")
def hello_world():
    #return render_template('table.html',headings=headings)
    return render_template('input.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True) 