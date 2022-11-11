from flask import Flask,render_template,request,redirect,make_response,flash
from database import db
from database import app
from database import Users,flight

db.create_all()

@app.route("/logout")
def logout():
    flash("user log out","danger")
    response = make_response(redirect('/login'))
    response.delete_cookie("userr")
    return response
@app.route('/login',methods=['GET','POST'])
def login():
    result=''
    user=''
    pas=''
    if request.method=='POST':
        user = request.form.get('user')
        pas = request.form.get('pas')
        found=False
        for u in range(len(Users.query.all())):
            print(user,"-",Users.query.all()[u].username,",",pas,"-",Users.query.all()[u].password)
            if user==Users.query.all()[u].username and pas==Users.query.all()[u].password:
                flash("user login","success")
                response=make_response(redirect('/add'))
                response.set_cookie("userr",user)
                found = True
                return response
        if found==False:
                flash("user or pass wrong", "danger")
                return render_template('login.html', result=result)
    return render_template('login.html')

@app.route('/')
def flaskhtm():

    return render_template('flaskhtm.html',flight=flight.query.all(),items=len(flight.query.all()))


@app.route('/add_list',methods=['POST','GET'])
def add_list():
    val1=''
    val2=''
    result=""
    if request.method=='POST':
        val1=request.form.get('number')
        val2=request.form.get('time')
        if len(val1)==6:
            flight1=flight(flight_number=val1,flight_time=val2)
            db.session.add(flight1)
            db.session.commit()
            flash("flight add","success")
            return redirect('/add')
        else:
            flash("wrong fight number or time","danger")
            print(result)
            return render_template('add.html',result=result)
@app.route('/add')
def add():
    if request.cookies.get("userr"):
        return render_template('add.html',use=request.cookies.get("userr"))
    else:
        return redirect('/login')


@app.route('/delete',methods=['GET','POST'])
def deleet():
    if request.cookies.get("userr"):
        if request.method == 'POST':
            number_del = request.form.get('number_del')
            for i in range(len(flight.query.all())):
                if number_del == flight.query.all()[i].flight_number:
                    flight1 = flight.query.filter_by(flight_number=number_del).first()
                    db.session.delete(flight1)
                    db.session.commit()
                    return redirect('/delete')
                    # list.remove(list[i])
                    # list1.remove(list1[i])
        return render_template('deleet.html',use=request.cookies.get("userr"))

    else:
        return redirect('/login')
@app.route('/signup',methods=['POST','GET'])
def signup():
    user_name=''
    password=''
    re_password = ''
    if request.method=='POST':
        user_name1 = request.form.get('user')
        password1 = request.form.get('pas')
        re_password = request.form.get('pass')
        if password1==re_password:
            admin1=Users(username=user_name1,password=password1)
            db.session.add(admin1)
            db.session.commit()
            flash("user rigester","success")
            return redirect('/add')
        else:
            flash("password not== re_password","danger")
            return render_template('signup.html')
    else:
        return render_template('signup.html')
@app.errorhandler(404)
def showerror(error):
    return render_template("error-404.html"),404
if __name__=='__main__':
    app.run()
