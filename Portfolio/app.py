from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
from models import *
@app.route('/')
def index():
    from models import Experience
    experience = Experience.query.all()
    from models import Education
    education=Education.query.all()
    from models import Opinion
    opinion=Opinion.query.all()
    from models import Portfolio
    portfolio=Portfolio.query.all()
    from models import Blog
    blog=Blog.query.all()
    return render_template('app/index.html', experience=experience,education=education,opinion=opinion,portfolio=portfolio,blog=blog)


@app.route('/admin/experience',methods=["GET","POST"])
def admin_experience():
    from models import Experience
    experience=Experience.query.all()
    if request.method=='POST':
        experience=Experience(
            year=request.form["experience_year"],
            tittle=request.form["experience_title"],
            about=request.form["experience_about"]
        )
        db.session.add(experience)
        db.session.commit()
        return redirect("/admin/experience")
    return render_template('admin/exp.html', experience=experience)

@app.route("/admin/experience/delete/<int:id>")

def admin_experience_delete(id):
        from models import Experience
        experience=Experience.query.filter_by(id=id).first()
        db.session.delete(experience)
        db.session.commit()
        return redirect('/admin/experience')
    
@app.route("/admin/experience/update/<int:id>", methods=["GET", "POST"])
def admin_experience_update(id):
    from models import Experience
    experience=Experience.query.filter_by(id=id).first()
    if request.method=="POST":
        experience=Experience.query.filter_by(id=id).first()
        experience.year=request.form["experience_year"]
        experience.title=request.form["experience_title"]
        experience.about=request.form["experience_about"]
        db.session.commit()
        return redirect('/admin/experience')
    return render_template('admin/expUpdate.html', experience=experience)

@app.route('/admin/education',methods=["GET","POST"])
def admin_education():
    from models import Education
    education=Education.query.all()
    if request.method=='POST':
        education=Education(
            edu_year=request.form["education_year"],
            edu_tittle=request.form["education_tittle"],
            edu_about=request.form["education_about"]
        )
        db.session.add(education)
        db.session.commit()
        return redirect("/admin/education")
    return render_template('admin/edu.html', education=education)

@app.route("/admin/education/delete/<int:id>")

def admin_education_delete(id):
        from models import Education
        education=Education.query.filter_by(id=id).first()
        db.session.delete(education)
        db.session.commit()
        return redirect('/admin/education')
@app.route("/admin/education/update/<int:id>", methods=["GET", "POST"])
def admin_education_update(id):
    from models import Education
    education=Education.query.filter_by(id=id).first()
    if request.method=="POST":
        education=Education.query.filter_by(id=id).first()
        education.year=request.form["education_year"]
        education.title=request.form["education_title"]
        education.about=request.form["education_about"]
        db.session.commit()
        return redirect('/admin/education')
    return render_template('admin/eduUpdate.html', education=education)


@app.route("/admin/opinion", methods=['GET', 'POST'])

def admin_opinion():
    from models import Opinion
    opinion=Opinion.query.all()
    if request.method=='POST':
        file=request.files['opinion_img']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        opinion=Opinion(
            opinion_name=request.form["opinion_name"],
            opinion_text=request.form["opinion_text"],
            opinion_img=filename
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect('/admin/opinion')
    return render_template('admin/opinion.html', opinion=opinion)

@app.route("/admin/opinion/delete/<int:id>" )

def admin_opinion_delete(id):
        from models import Opinion
        opinion=Opinion.query.filter_by(id=id).first()
        db.session.delete(opinion)
        db.session.commit()
        return redirect('/admin/opinion')
    
    
@app.route("/admin/opinion/update/<int:id>",methods=["GET", "POST"])
def admin_opinion_update(id):
    from models import Opinion
    opinion=Opinion.query.filter_by(id=id).first()
    if request.method=="POST":
        opinion=Opinion.query.filter_by(id=id).first()
        opinion.opinion_text=request.form["opinion_text"]
        opinion.opinion_name=request.form["opinion_name"]
        db.session.commit()
        return redirect('/admin/opinion')
    return render_template('admin/opiUpdate.html',opinion=opinion)


@app.route("/admin/portfolio", methods=['GET', 'POST'])

def admin_portfolio():
    from models import Portfolio
    portfolio=Portfolio.query.all()
    if request.method=='POST':
        file=request.files['work_img']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        portfolio=Portfolio(
            portfolio_name=request.form["work_name"],
            portfolio_link=request.form["work_link"],
            portfolio_img=filename
        )
        db.session.add(portfolio)
        db.session.commit()
        return redirect('/admin/portfolio')
    return render_template('admin/portfolio.html', portfolio=portfolio)

@app.route("/admin/portfolio/delete/<int:id>" )
def admin_portfolio_delete(id):
        from models import Portfolio
        portfolio=Portfolio.query.filter_by(id=id).first()
        db.session.delete(portfolio)
        db.session.commit()
        return redirect('/admin/portfolio')
    
    
@app.route("/admin/portfolio/update/<int:id>",methods=["GET", "POST"])
def admin_portfolio_update(id):
    from models import Portfolio
    portfolio=Portfolio.query.filter_by(id=id).first()
    if request.method=="POST":
        portfolio=Portfolio.query.filter_by(id=id).first()
        portfolio.portfolio_name=request.form["portfolio_name"]
        portfolio.portfolio_link=request.form["portfolio_link"]
        db.session.commit()
        return redirect('/admin/portfolio')
    return render_template('admin/portfolioUpdate.html',portfolio=portfolio)

@app.route("/admin/blog", methods=['GET', 'POST'])

def admin_blog():
    from models import Blog
    blog=Blog.query.all()
    if request.method=='POST':
        file=request.files['blog_img']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        blog=Blog(
            blog_name=request.form["blog_name"],
            blog_text=request.form["blog_text"],
            blog_link=request.form["blog_link"],
            blog_img=filename
        )
        db.session.add(blog)
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/blog.html', blog=blog)

@app.route("/admin/blog/delete/<int:id>" )
def admin_blog_delete(id):
        from models import Blog
        blog=Blog.query.filter_by(id=id).first()
        db.session.delete(blog)
        db.session.commit()
        return redirect('/admin/blog')
    
@app.route("/admin/blog/update/<int:id>",methods=["GET", "POST"])
def admin_blog_update(id):
    from models import Blog
    blog=Blog.query.filter_by(id=id).first()
    if request.method=="POST":
        blog=BLog.query.filter_by(id=id).first()
        blog.blog_name=request.form["blog_name"]
        blog.blog_text=request.form["blog_text"]
        blog.blog_link=request.form["blog_link"]
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/blogUpdate.html',blog=blog)



if __name__=='__main__':
    db.create_all()
    app.run(debug=True)    




