import hashlib


def md5(str):
    if len(str) !=0:
        h = hashlib.md5(str.encode(encoding='utf-8'))
        h1 = h.hexdigest()
        return h1

def checkMd5(old,new):
    if len(new)!=0:
        h = hashlib.md5(new.encode(encoding='utf-8'))
        h1 = h.hexdigest()
        return h1==old

# class MD5:
#     def __init__(self,Str):
#         self.Str=Str
#
#     def md5(self):
#         if len(self.Str) !=0:
#             h = hashlib.md5(self.Str.encode(encoding='utf-8'))
#             h1 = h.hexdigest()
#             return h1
#
#     def md5(self,str):
#         if len(str) !=0:
#             h = hashlib.md5(str.encode(encoding='utf-8'))
#             h1 = h.hexdigest()
#             return h1
#
#     def checkMd5(self,old,new):
#         if len(new)!=0:
#             h = hashlib.md5(new.encode(encoding='utf-8'))
#             h1 = h.hexdigest()
#             return h1==old