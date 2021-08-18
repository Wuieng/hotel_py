from pyhotel.Dao import AdminDaoImpl
from pyhotel.Dao import HotelManagerDaoImpl
import pyhotel.Md5 as Md5
# 要不要用类来完成后台操作是关键
def Admlogin(Id,Password):
    Admin=AdminDaoImpl.getAdminById(Id)
    pasw = Md5.md5(Password)
    # 登录成功
    if Admin.Password == pasw:
        return True
    else:
        return False

def Managerlogin(Id,Password):

    pasw=Md5.md5(Password)
    Manager=HotelManagerDaoImpl.getManagerById(Id)
    if Manager.Password == pasw:
        return True
    else:
        return False

def GetManagerBy(Id):
    return HotelManagerDaoImpl.getManagerById(Id)

