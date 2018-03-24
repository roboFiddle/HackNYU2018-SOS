from flask import Flask, request, jsonify
import hashlib
import random
import DatabaseHandler

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
@app.route('addtest')
@app.route('addmedication')
@app.route('adddoctorshare')
@app.route('logemergency')
@app.route('arriveemergency')



if __name__ == '__main__':
    app.run()