import pymysql

from pyhotel.Dao import AdminDaoImpl
from pyhotel.pojo.hotelpojo import  Hotel

Host = "localhost"
User = "root"
Pass = "1234"
DbName = "hotel"

# 链接查询，链接manager表和hotelInfo表
# 或者不用连接查询，可以通过mannager表得到hotelID来查出所有hotel
def getHotelById(Id):
    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：查询
    sql = "SELECT * FROM hotelinfo where Id = %d "%(Id)

    # 异常处理
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有的记录列表
        results = cursor.fetchall()
        for row in results:
            # 打印列表元素
            print(row)
            Id = row[0]
            Name = row[1]
            Address = row[2]
            Phone = row[3]
            Intro = row[4]
            global  hotel
            hotel=Hotel(Id,Name,Address,Phone,Intro)
        return hotel
    except:
        print('Uable to fetch data!')

    # 关闭数据库连接
    db.close()
# 添加酒店
def AddHotel(Hotel):
    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：插入，这里ID自增，所以不插入ID
    sql = "INSERT INTO hotelinfo(Name, Address, Phone, Intro)" \
          " VALUES ('%s', '%s','%s', '%s' )"\
          % (Hotel.Name, Hotel.Address, Hotel.Phone, Hotel.Intro)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

# hotel表需要被更新
def UpdateHotel(Hotel):
    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：插入，这里ID自增，所以不插入ID
    sql = "UPDATE  hotelinfo set Name = %s, " \
          "Address = %s,  Phone = %s," \
          "Intro =%s where Id = %d"\
          %(Hotel.Name,Hotel.Address,Hotel.Phone,Hotel.Intro,Hotel.HotelId)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


