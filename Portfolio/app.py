
from flask import Flask,render_template
import random
class Exp:
    def __init__(self,_year,_title,_shorttext):
        self.year=_year
        self.title=_title
        self.shorttext=_shorttext
        
exp=[
    Exp(
        '2017',
        'yazdim',
        'mence bir gun alinacaq'
    )
] 


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html',allexp=exp)
