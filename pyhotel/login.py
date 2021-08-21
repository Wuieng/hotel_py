from flask import Flask, render_template, request, flash, url_for, session, redirect, jsonify
from  pyhotel.Service import Login
from pyhotel.Admin import admin as admin_bluprint
from pyhotel.Manager import manager as manager_bluprint
import hashlib

app = Flask(__name__)

app.register_blueprint(admin_bluprint)
app.register_blueprint(manager_bluprint)
app.config['SECRET_KEY']='123456'
@app.route('/')
def index():
    if not session.get('adm') and not session.get('manager'):
        return render_template('login.html')
    elif session.get('adm'):
        return render_template('AdmMain.html')
    elif session.get('manager'):
        return render_template('ManagerMain.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        Id=int(request.form.get('Id'))
        Password=request.form.get('Password')
        type=request.form.get('type')

        if type == 'adm':
            if(Login.Admlogin(Id,Password)):
                session['adm']=Id
                #在session存入对应ID
                return render_template('AdmMain.html')
            else:
                flash("login failed")
                return redirect(url_for('login'))
        #     重定向回到login对应的页面
        elif type == 'manager':
            if (Login.Managerlogin(Id,Password)):
                session['manager']=Id
                manager=Login.GetManagerBy(Id)
                rooms = Login.GetFlashRoom(manager.HotelId)
                # session.get()
                return render_template('ManagerMain.html',HotelId=manager.HotelId,rooms=rooms)
            else:
                flash("login failed")
                return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash("退出成功")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
