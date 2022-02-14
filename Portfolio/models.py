from app import db

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(50))
    tittle = db.Column(db.String(50))
    about = db.Column(db.String(200))
    
    

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    edu_year = db.Column(db.String(50))
    edu_tittle = db.Column(db.String(50))
    edu_about = db.Column(db.String(200))


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opinion_name = db.Column(db.String(50))
    opinion_text = db.Column(db.String(100))
    opinion_img = db.Column(db.String(200))
    
    
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    portfolio_name = db.Column(db.String(50))
    portfolio_link = db.Column(db.String(100))
    portfolio_img = db.Column(db.String(200))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(50))
    blog_text = db.Column(db.String(100))
    blog_link = db.Column(db.String(100))
    blog_img = db.Column(db.String(200))

