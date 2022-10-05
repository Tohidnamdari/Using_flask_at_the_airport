from flask import Flask,render_template,request,redirect,make_response
app=Flask(__name__)
number=["123456","664455","771456","101023","798523"]
watch=["22:14","12:18","14:17","15:56","11:23"]
user_s = ["tohid", "matin"]
pas_s = ["1234", "1235"]
@app.route("/logout")
def logout():
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
        for u in range(len(user_s)):
            if user==user_s[u] and pas==pas_s[u]:
                response=make_response(redirect('/add'))
                response.set_cookie("userr",user)
                return response
            else:
                result="wrong user or pass"
                return render_template('login.html', result=result)
    return render_template('login.html')

@app.route('/')
def flaskhtm():
        return render_template('flaskhtm.html',too=number,op=watch,items=len(number))
@app.route('/add_list',methods=['POST','GET'])
def add_list():
    val1=''
    val2=''
    result=""
    if request.method=='POST':
        val1=request.form.get('number')
        val2=request.form.get('time')
        if len(val1)==int(6):
            number.append(val1)
            watch.append(val2)
            return redirect('/add')
        else:
            result="wrong fight number or time"
            print(result)
            return render_template('add.html',result=result)
@app.route('/add')
def add():
    if request.cookies.get("userr"):
        return render_template('add.html',use=request.cookies.get("userr"))
    else:
        return redirect('/login')
@app.route('/signup',methods=['POST','GET'])
def signup():
    user_name=''
    password=''
    re_password = ''
    result=''
    if request.method=='POST':
        user_name = request.form.get('user')
        password = request.form.get('pas')
        re_password = request.form.get('pass')
        if password==re_password:
            user_s.append(user_name)
            pas_s.append(password)
            return redirect('/add')
        else:
            result = "not found"
            return render_template('signup.html', result=result)
    else:
        return render_template('signup.html',result=result)
@app.errorhandler(404)
def showerror(error):
    return render_template("error-404.html"),404
if __name__=='__main__':
    app.run(host='192.168.174.211',port=1414)
