# 实体类用于存储数据，简便操作
# 管理员来注册酒店管理人员
class Administrator:
    def __init__(self,Id,Password):
        self.Id=Id
        self.Password=Password
#酒店管理人员要管理自己的酒店，所以登录时要带上hotelId,并且通过这个参数操作修改room
class HotelManager:
    def __init__(self,Id,Password,HotelId):
        self.Id=Id
        self.Password=Password
        self.HotelId=HotelId

class Hotel:
    def __init__(self,HotelId,Name,Address,Phone,Intro):
        self.HotelId=HotelId
        self.Name=Name
        self.Address=Address
        self.Phone=Phone
        self.Intro=Intro

class Room:
    def __init__(self,RoomId,HotelId,Type,Price,NumofRoom,NumofMan):
        self.RoomId=RoomId
        self.HotelId=HotelId
        self.Type=Type
        self.Price=Price
        self.NumofRoom=NumofRoom
        self.NumofMan=NumofMan