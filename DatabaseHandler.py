class LoginRequest:
    def __init__(self, s, uid, utype, rname):
        self.success = s
        self.userID = uid
        self.userType = utype
        self.realName = rname

class DatabaseHandler:
    def __init__(self):
        pass
    def login(self):
        pass
