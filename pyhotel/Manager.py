from flask import Blueprint, request, render_template, flash, session, redirect,url_for
from pyhotel.pojo.hotelpojo import HotelManager,Hotel
from pyhotel.Dao import RoomDaoImpl,HotelDaoImpl
import hashlib


manager = Blueprint('manager',__name__,url_prefix='/manager')

@manager.route('/hotelact',methods=['GET','POST'])
def hotelact():
    # session.get()
    # 不用session
    # 不使用<int：Id>的方式
    print(request.form)
    print("========")
    print(request.method)
    # 其实这里是不是form都无所谓，
    # 因为实际上这里args是从url也就是query里面拿值的
    # 但是下面update方法报错，确实是需要去hotelInfo里去设定method的
    hotelId=int(request.args.get('HotelId'))
    hotel=HotelDaoImpl.getHotelById(hotelId)
    return render_template('HotelInfo.html',hotel=hotel)

@manager.route('/hotelupdate',methods=['GET','POST'])
def update_hotel():
    print(request.form)
    print("========")
    print(request.method)
    hotelId=int(request.form.get('HotelId'))
    hotel=HotelDaoImpl.getHotelById(hotelId)
    HotelName=request.form.get('HotelName')
    Address=request.form.get('Address')
    Phone=request.form.get('Phone')
    Intro=request.form.get('Intro')
    if hotel.Name==HotelName and hotel.Address==Address and hotel.Phone==Phone and hotel.Intro==Intro:
        flash("修改失败,数据一致")
        # hotel = HotelDaoImpl.getHotelById(hotelId)
        # return render_template('HotelInfo.html', hotel=hotel)
    elif HotelName==None or Address==None or Phone==None or Intro ==None:
        flash("修改失败，数据为空")
        # return render_template('HotelInfo.html', hotel=hotel)
    else:
        hotel.Name=HotelName
        hotel.Address=Address
        hotel.Intro=Intro
        hotel.Phone=Phone
        HotelDaoImpl.UpdateHotel(hotel)
        flash("修改成功")
        # return render_template('HotelInfo.html', hotel=hotel)
    #     原来有三个这个return，发现重复了，没必要,最后取下数据返回下就好
    hotel=HotelDaoImpl.getHotelById(hotelId)
    return render_template('HotelInfo.html', hotel=hotel)


@manager.route('/roomact',methods=['GET','POST'])
def roomact():
    print("adsasdasdasdas")
    print(request.url)
    print(request.form)
    print(request.method)
    # 这里get请求  要用另外一个方法  从url中拿  也就是query中要加参数
    # 后来改成post，发现可也可以用form取值
    # 这里其实也可以拿confirm的值，只不过我忘了
    hotelId = int(request.args.get('HotelId'))
    rooms = RoomDaoImpl.getRoomById(hotelId)
    return render_template('roomInfo.html', rooms=rooms)

@manager.route('/roomupdate',methods=['GET','POST'])
def update_room():
    print(request.form)
    print("========")
    print(request.method)
    # 前面前端某处指定get之后，后面就用不了post了
    roomId = int(request.form.get('confirm'))
    room = RoomDaoImpl.getRoomByRoomId(roomId)
    Type = request.form.get('Type')
    price =int(request.form.get('roomPrice'))
    NumOfMan = int(request.form.get('NumOfMan'))
    NumofRoom = int(request.form.get('NumofRoom'))
    if room.Type == Type and room.Price == price and room.NumofMan == NumOfMan and room.NumofRoom == NumofRoom:
        flash("修改失败")
        # rooms = RoomDaoImpl.getRoomById(room.HotelId)
        # return render_template('roomInfo.html', rooms=rooms)
    elif Type==None or price==None or NumOfMan==None or NumofRoom==None:
        flash("修改失败，数据为空")
        # rooms = RoomDaoImpl.getRoomById(room.HotelId)
        # return render_template('roomInfo.html', rooms=rooms)
    else:
        room.Type=type
        room.Price=price
        room.NumofRoom=NumofRoom
        room.NumofMan=NumOfMan
        RoomDaoImpl.UpdateHotel(room)
        flash("修改成功")
    #与上面同一个道理，原来有三个这个return，发现重复了，没必要,最后取下数据返回下就好

    rooms = RoomDaoImpl.getRoomById(room.HotelId)
    return render_template('roomInfo.html', rooms=rooms)