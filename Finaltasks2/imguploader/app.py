from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Gallery.db'
db = SQLAlchemy(app)

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Imgname= db.Column(db.String(80))
    Imgurl = db.Column(db.String(120))
# db.create_all()

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        file=request.files['file']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        _imgnames=request.form['ad']
        imgadress=filename  
        image=Gallery(Imgname=_imgnames,Imgurl=imgadress)
        db.session.add(image)
        db.session.commit()
        return redirect('/gallery')
    return render_template('add.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')