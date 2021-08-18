from flask import Blueprint, request, render_template, flash
from pyhotel.pojo.hotelpojo import HotelManager,Hotel
from pyhotel.Dao import HotelManagerDaoImpl,HotelDaoImpl
import pyhotel.Md5 as Md5


admin = Blueprint('admin',__name__,url_prefix='/admin')

# 和adminmain.html页面配合使用
@admin.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        Id = int(request.form.get('Id'))
        if HotelManagerDaoImpl.getManagerById(Id)!=None:
            flash("已存在，添加失败")
            return render_template('AdmMain.html')
        Password = Md5.md5(request.form.get('Password'))
        HotelId = int(request.form.get('HotelId'))
        manager = HotelManager(Id,Password,HotelId)
        HotelManagerDaoImpl.Add(manager)
        flash("添加成功")
        return render_template('AdmMain.html')
        # return render_template('login.html')
    elif request.method == 'POST':
        Id=int(request.form.get('Id'))
        if HotelManagerDaoImpl.getManagerById(Id)!=None:
            flash("已存在，添加失败")
            return render_template('AdmMain.html')
        Password = Md5.md5(request.form.get('Password'))
        HotelId=request.form.get('HotelId')
        manager = HotelManager(Id,Password,HotelId)
        HotelManagerDaoImpl.Add(manager)
        flash("添加成功")
        return render_template('AdmMain.html')

@admin.route('/add',methods=['GET','POST'])
def add():
    message=None
    if request.method == 'GET':
        HotelId = int(request.form.get('HotelId'))
        if HotelDaoImpl.getHotelById(HotelId)!=None:
            message="已存在，添加失败"
            return render_template('AdmMain.html',message=message)
        Name = request.form.get('Name')
        Address = int(request.form.get('Address'))
        Phone = int(request.form.get('Phone'))
        Intro = int(request.form.get('Intro'))
        hotel = Hotel(HotelId,Name,Address,Phone,Intro)
        HotelDaoImpl.AddHotel(hotel)
        message="添加成功"
        return render_template('AdmMain.html',message=message)
        # return render_template('login.html')
    elif request.method == 'POST':
        HotelId = int(request.form.get('HotelId'))
        if HotelDaoImpl.getHotelById(HotelId) != None:
            message = "已存在，添加失败"
            return render_template('AdmMain.html', message=message)
        Name = request.form.get('Name')
        Address = int(request.form.get('Address'))
        Phone = int(request.form.get('Phone'))
        Intro = int(request.form.get('Intro'))
        hotel = Hotel(HotelId, Name, Address, Phone, Intro)
        HotelDaoImpl.AddHotel(hotel)
        message="添加成功"
        return render_template('AdmMain.html',message=message)

@admin.route('/logout')
def logout():
    pass
