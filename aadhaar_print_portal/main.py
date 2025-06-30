from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        password = request.form['password']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(filepath)
        try:
            reader = PdfReader(filepath)
            if reader.is_encrypted:
                reader.decrypt(password)
            return render_template('success.html', file=f.filename)
        except:
            return "Incorrect password or invalid file."
    return render_template('index.html')

app.run(host='0.0.0.0', port=81)
