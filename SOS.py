from flask import Flask, request, jsonify
import hashlib
import random
import DatabaseHandler

from time import time


app = Flask(__name__)
db = DatabaseHandler()

@app.route('schema.sql', methods = ['GET'])
@app.route('login')
def login():
    if request.method == 'POST':
        loginrequest = db.login(request.form['username'],request.form['password'])
        token = hashlib.md5(str(random.random()).encode('utf-8')).hexdigest()
        db.setauthtoken(loginrequest.ID, token)
        if loginrequest.success:
            return Flask.jsonify( {"success": 1, "error": None, "userid": loginrequest.ID, "userType": loginrequest.type, "realName": loginrequest.name, "token": token})
        else:
            return Flask.jsonify(
                {"success": 0, "error": "Invalid Username or Password", "userID": -1, "userType": -1})
@app.route('logout')
def logout():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        db.logout(request.form['userid'])

@app.route('getinfo')
def getinfo():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        if request.form['infoforuserid'] != request.form['userid']:
            assert db.cangetinfo(request.form['userid'], request.form['infoforuserid'])
        usermodel = db.getUserData(request.form['userid'])
        return Flask.jsonify(usermodel)

@app.route('addappointment')
def addappointment():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        assert db.getUserType(request.form['userid']) == 1
        db.insertAppointment(request.form['appointmentid'], request.form['patientid'], request.form['doctorid'],
                             request.form['date'], request.form['type'], request.form['reason'], request.form['results'],
                             request.form['extradetails'], request.form['privatenotes'])

@app.route('addtest')
def addtest():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        db.insertTest(request.form['testid'], request.form['doctorid'], request.form['patientid'], request.form['type'],
                      request.form['date'], request.form['result'], request.form['privatenotes'], request.form['appid'])


@app.route('addmedication')
def addmedication():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        db.insertMedication(request.form['medid'], request.form['userid'], request.form['medtype'], request.form['dosage'],
                            request.form['dosageunits'], request.form['frequency'], request.form['frequencyunit'])

@app.route('adddoctorshare')
def adddoctorshare():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        db.insertDoctor(request.form['userid'], request.form['useremail'], request.form['userpassword_salt'],
                            request.form['userpasssword_hash'], 1, None, None,
                            None, None, request.form['doctortype'])


@app.route('logemergency')
def logemergency():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
        db.insertEmergency((request.form['userid']), time(), request.form['latitude'], request.form['longitude'])
'''
@app.route('arriveemergency')
def arriveemergency():
    if request.method == 'POST':
        assert db.confirmtoken(request.form['userid'], request.form['token'])
'''



if __name__ == '__main__':
    app.run()