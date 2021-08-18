import pymysql

from pyhotel.pojo.hotelpojo import  Room


Host = "localhost"
User = "root"
Pass = "1234"
DbName = "hotel"
# class RoomDaoImpl:

def getRoomById(HotelId):
    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：查询
    sql = "SELECT * FROM room where HotelId = %d "%(HotelId)

    # 异常处理
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有的记录列表
        results = cursor.fetchall()
        # 一个酒店的所有房间类型
        rooms=[]
        for row in results:

            roomId = row[0]
            HotelId = row[1]
            type = row[2]
            price = row[3]
            NumofRoom = row[4]
            NumofMan = row[5]
            rooms.append(Room(roomId,HotelId,type,price,NumofRoom,NumofMan))
        return rooms
    except:
        print('Uable to fetch data!')
    # 关闭数据库连接
    db.close()
# 添加房间
def AddRoom(Room):
    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：插入，这里ID自增，所以不插入ID

    sql = "INSERT INTO room(HotelId,type, price, NumofRoom, NumofMan)" \
          " VALUES ('%d',''%s', '%d','%d', '%d' )"\
          % (Room.HotelId, Room.Type, Room.Price, Room.NumofRoom,Room.NumofMan)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

# hotel表需要被更新
def UpdateHotel(Room):
    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：插入，这里ID自增，所以不插入ID
    sql = "UPDATE  room  set type= %s, " \
          "price = %d, NumofRoom= %d, NumofMan %d,  where roomId = %d"\
          %( Room.Type, Room.Price, Room.NumofRoom,Room.NumofMan,Room.RoomId)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def getRoomByRoomId(Id):
    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：查询
    sql = "SELECT * FROM room where roomId = %d "%(Id)

    # 异常处理
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有的记录列表
        results = cursor.fetchall()
        # 一个酒店的所有房间类型

        for row in results:

            roomId = row[0]
            HotelId = row[1]
            type = row[2]
            price = row[3]
            NumofRoom = row[4]
            NumofMan = row[5]
            global room
            room=Room(roomId,HotelId,type,price,NumofRoom,NumofMan)
        return room
    except:
        print('Uable to fetch data!')
    # 关闭数据库连接
    db.close()
