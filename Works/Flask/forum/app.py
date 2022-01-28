from flask import Flask,redirect,url_for,render_template,request
mesajlar=[]

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def add():
    return render_template('index.html')

@app.route('/messages',methods=['GET','POST'] )
def messages():
    if request.method=='POST':
        _ad=request.form['firstname']
        _email=request.form['lastname']
        _mesaj=request.form['subject']
        
        mesaj={
            'firstname':_ad,
            'lastname':_email,
            'subject':_mesaj
        }
        mesajlar.append(mesaj)
        return  render_template('data.html',messages=mesajlar)
    return render_template('data.html')
if __name__=='__main__':
    app.run(port=5000,debug=True)