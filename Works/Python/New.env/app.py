from flask import Flask,render_template
import random
class News:
    def __init__(self,_id,_img,_title,_shorttext):
        self.id=_id
        self.img=_img
        self.title=_title
        self.shorttext=_shorttext
        

news=[
    News(
        random.randint(1, 1000),
        'https://www.imgacademy.com/themes/custom/imgacademy/images/helpbox-contact.jpg',
        'title',
        'detail'
    )
]  


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html',allnews=news)


        