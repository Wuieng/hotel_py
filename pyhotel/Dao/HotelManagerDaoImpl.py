import pymysql

from pyhotel.Dao.AdminDaoImpl import AdminDaoImpl
from pyhotel.pojo.hotelpojo import HotelManager

Host = "localhost"
User = "root"
Pass = "1234"
DbName = "hotel"

def getManagerById(Id):

    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：查询
    sql = "SELECT * FROM hotelmanager where Id = %d"%(Id)
    # 或者直接用  +   str()
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有的记录列表
        results = cursor.fetchall()

        for row in results:
            # 打印列表元素
            print(row)

            Id = row[0]

            Password = row[1]

            HotelId = row[2]

            global Manager

            Manager=HotelManager(Id,Password,HotelId)

    except :
        print('Uable to fetch data!')
    try:
        return Manager
    # 这里就是如果没有找到数据，就是查不到就返回一个NameError，那么就返回None
    # 或者也可以将return Manager放到Manager=HotelManager(Id,Password,HotelId)这个for循环之后
    except NameError:
        return None

    # 关闭数据库连接
    db.close()

def Add(Manager):
    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：插入，这里ID自增，所以不插入ID
    # //可以使用自增版本，或者添加判断Id是否存在
    sql = "INSERT INTO hotelmanager(Id, Password,HotelId)" \
          " VALUES ('%d', '%s','%d' )"\
          % (Manager.Id, Manager.Password, Manager.HotelId)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


print(getManagerById(2))
# a = AdminDaoImpl()
# for i in a.getAllAdmin():
#     print(i)