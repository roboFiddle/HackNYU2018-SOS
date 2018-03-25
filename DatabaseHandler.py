import mysql.connector
import hashlib
import time
from objectDefinition import *

class LoginRequest:
    def __init__(self, s, uid, utype, rname):
        self.success = s
        self.userID = uid
        self.userType = utype
        self.realName = rname

class DBH:
    def __init__(self):
        # fucking took long enough
        self.c = mysql.connector.connect(user='root', password='ilovecaffine42',
                                    host='35.227.38.69', database='sosapp')
        self.cursor = self.c.cursor()
    def login(self, name, password):
        query = "SELECT * FROM usertable WHERE useremail = '" + name+"'"
        self.cursor.execute(query)
        for a in self.cursor:
            user = a
        #if hashlib.md5(str(user[2] + password).encode('utf-8')).hexdigest() == user[3]:
        return LoginRequest(1,user[0],0,user[4])
        #else:
        #    return LoginRequest(0,None, None, None)

    def logout(self, userid):
        query = "UPDATE usertable SET authtoken='' WHERE id = '" + str(userid) + "'"
        self.cursor.execute(query)
        self.c.commit()
    def setauthtoken(self, userid, token):
        query = "UPDATE usertable SET authtoken='" + token + "' WHERE id = '" + str(userid) + "'"
        print(query)
        self.cursor.execute(query)
        self.c.commit()
    def confirmtoken(self, userid, token):
        query = "SELECT authtoken FROM usertable WHERE id = '" + str(userid) + "'"
        self.cursor.execute(query)
        t = [0]
        for a in self.cursor:
            t = a
        print(t)
        if t[0] == token:
            return True
        return False
    def getUserData(self, userid):
        query = "SELECT * FROM usertable WHERE id = '" + str(userid) + "'"
        self.cursor.execute(query)
        t = [0]
        for a in self.cursor:
            t = a
        print(t)
        print(len(t))
        s = User(t[0], t[3], t[1], t[5], t[15], t[16], t[18], t[7], t[17], t[19])
        return s
    def insertMedication(self):
        pass
    def insertEmergency(self, userid, tin, lat, long):
        query = "INSERT INTO emergencylog (patientID, calltime, locationlatitude, locationlongitude) VALUES (" + \
            userid + ", '" + tin.strftime('%Y-%m-%d %H:%M:%S') + "'," + lat + "," + long + ")"
        print(query)
        self.cursor.execute(query)
        self.c.commit()