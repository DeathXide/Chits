from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from chits import chit_fun

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route("/",methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.filename = "chits.pdf"
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        k = chit_fun(file.filename)
        return render_template("sucess.html")
    return render_template("home.html",form = form)

@app.route('/front/')
def front():
    return send_file("static/files/Front.pdf",as_attachment=True)

@app.route('/back/')
def back():
    return send_file("static/files/Back.pdf",as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True,port=5001)
