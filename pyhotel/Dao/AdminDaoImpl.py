import pymysql

from pyhotel.pojo.hotelpojo import Administrator

Host = "localhost"
User = "root"
Pass = "1234"
DbName = "hotel"

# 用类实现的做法，之后看情况可以全部改成用类实现

class AdminDaoImpl:
    def __init__(self):
        self.Host = "localhost"
        self.User = "root"
        self.Pass = "1234"
        self.DbName = "hotel"
    def getAllAdmin(self):
        try:
            db = pymysql.connect(host=self.Host, user=self.User, password=self.Pass, database=self.DbName)
            print("数据库链接成功")
        except pymysql.Error as e:
            print("数据库链接异常" + e)

        cursor = db.cursor()

        # SQL语句：查询
        sql = "SELECT * FROM administrator  "

        list=[]
        # 异常处理
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有的记录列表
            results = cursor.fetchall()
            # print(type(results))
            # 遍历列表
            for row in results:
                # 打印列表元素
                print(row)

                Id = row[0]

                Password = row[1]
                list.append(Administrator(Id,Password))
                # 打印列表元素
                print(Id,Password )
        except:
            print('Uable to fetch data!')
        return list
        # 关闭数据库连接
        db.close()

def getAdminById(Id):

    try:
        db = pymysql.connect(host=Host, user=User, password=Pass, database=DbName)
        print("数据库链接成功")
    except pymysql.Error as e:
        print("数据库链接异常" + e)

    cursor = db.cursor()

    # SQL语句：查询
    sql = "SELECT * FROM administrator where Id = %d"%(Id)
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
            global administrator
            administrator=Administrator(Id,Password)
            # 打印列表元素
            print(administrator)
        return administrator
    except:
        print('Uable to fetch data!')
    return None
    # 关闭数据库连接
    db.close()

# a = AdminDaoImpl()
# for i in a.getAllAdmin():
#     print(i)