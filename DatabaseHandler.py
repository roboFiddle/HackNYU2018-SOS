import mysql.connector

#fucking took long enough
c = mysql.connector.connect(user='root', password='ilovecaffine42',
                        host='35.227.38.69', database='sosapp')
cursor = c.cursor()


class LoginRequest:
    def __init__(self, s, uid, utype, rname):
        self.success = s
        self.userID = uid
        self.userType = utype
        self.realName = rname

class DBH:
    def __init__(self):
        pass
    def login(self):
        pass
    def setauthtoken(self):
        pass
    def confirmtoken(self):
        pass
    def cangetinfo(self):
        pass
    def getUserData(self):
        pass

    def insertAppointment(self):
        pass