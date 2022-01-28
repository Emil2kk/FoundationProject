from flask import Flask,render_template
app=Flask(__name__)

datas=[
    {
        'ad':'Emil',
        'soyad':'Abdullayev',
        'yas':30,
        
    },

    {
        'ad':'Emil',
        'soyad':'Abdullayev',
        'yas':30,
        
    }
]

@app.route('/')

def home():
    return render_template('index.html',data=datas)

@app.route('/about')

def about():
    return render_template('about.html')


