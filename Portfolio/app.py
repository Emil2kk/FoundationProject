from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(50))
    tittle = db.Column(db.String(50))
    about = db.Column(db.String(200))








@app.route('/',methods=["GET","POST"])
def appmain():
    return render_template('index.html')
@app.route('/admin',methods=["GET","POST"])
def admin():
    return render_template('admin.html')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
db = SQLAlchemy(app)


