from flask import Flask, request, jsonify
import hashlib
import random
from DatabaseHandler import *
import contact
import json
import os

import datetime


app = Flask(__name__)
db = DBH()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        loginrequest = db.login(request.form['username'],request.form['password'])
        token = hashlib.md5(str(random.random()).encode('utf-8')).hexdigest()
        if loginrequest.success:
            db.setauthtoken(loginrequest.userID, token)
            return json.dumps( {"success": 1, "error": None, "userid": loginrequest.userID, "userType": loginrequest.userType, "realName": loginrequest.realName, "token": token})
        else:
            return json.dumps(
                {"success": 0, "error": "Invalid Username or Password", "userID": -1, "userType": -1})
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        db.logout(request.form['userid'])
    return ""

@app.route('/getinfo', methods=['GET', 'POST'])
def getinfo():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        usermodel = db.getUserData(request.form['userid'])
        return usermodel.toJSON()


@app.route('/addmedication', methods=['GET', 'POST'])
def addmedication():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        db.insertMedication(request.form['medid'], request.form['userid'], request.form['medtype'], request.form['dosage'],
                            request.form['dosageunits'], request.form['frequency'], request.form['frequencyunit'])
    return ""


@app.route('/logemergency', methods=['GET', 'POST'])
def logemergency():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        userid = request.form['userid']
        t = datetime.datetime.today()
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        db.insertEmergency(userid, t, latitude, longitude)
<<<<<<< HEAD
        contact.sendMessage(jsonToStr(str(db.getUserData(request.form['userid']))))
    return ""
=======
        contact.sendMessage(str(db.getUserData(request.form['userid'])))
    return "hi"
>>>>>>> 47768eaa61e386e9f7b51549661f1a2eed879241

'''
@app.route('arriveemergency')
def arriveemergency():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
'''



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)

#for json info that is prodiced by getInfo()
def jsonToStr(s):
    s = s[1:-1].split(",")
    #to return
    a = ""
    for i in s:
        if ":" not in i:
            a += i + " "
        else:
            a += os.linesep + " " + i

    return a