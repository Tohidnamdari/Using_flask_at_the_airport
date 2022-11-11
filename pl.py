from flask import Flask,render_template,request,redirect,make_response,flash
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
user_s = ["tohid", "matin"]
pas_s = ["1234", "1235"]
app.config['SECRET_KEY']='jhvhijghlkbvhjvjkjhvcj'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///../name.db'
db=SQLAlchemy(app)
@app.route('/logout',methods=['GET','POST'])
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie("userr")
    flash("user logout","danger")
    return response
@app.route('/',methods=['GET','POST'])
def login():
    result=''
    user=''
    pas=''
    if request.method=='POST':
        user = request.form.get('user')
        pas = request.form.get('pas')
        for u in range(len(user_s)):
            if user==user_s[u] and pas==pas_s[u]:
                flash("user login","success")
                response=make_response(redirect('/panel'))
                response.set_cookie("userr",user)
                return response
            else:
                flash("user or pass wrong","danger")
                return render_template('login.html', result=result)
    return render_template('login.html')
@app.route('/panel',methods=['GET','POST'])
def panel():
    if request.cookies.get("userr"):
        return render_template('panel.html',use=request.cookies.get("userr"))
    else:
        return redirect('/')
if __name__=='__main__':
    app.run()