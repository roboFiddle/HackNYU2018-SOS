import sys, os, json
from datetime import date

class User(object):
    '''
    id = int
    n = name, ty = type of user(0, 1, 2) -- int, em = email, birth = birthdate -- int, h = height -- double,
    w = weight -- double,
    al = list of strings for allergies, bloTy = bloodtype, medCond = list of strings, gen = gender -- binary
    syst = systole bp, dias = diastole bp
    emgCont = emergency Contact, emgContNum = phone number of emg contact
    '''
    def __init__(self, id, n, em, birth, h, w, al, bloTy, medCond, gen):
        self.ID = id
        self.Name = n
        self.Email = em
        self.age = birth
        self.Height = h
        self.Weight = w
        self.Gender = gen
        self.BloodType = bloTy
        self.MedicalConditions =  al
        self.Allergies = medCond

    def calcAge(self,birthdate):
        today = date.today()
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Medication(object):
    '''
    cmNme = common name of drug
    sciNme = scientific name for drug
    tmeLastIng = time at last ingestion
    dos = doasge
    freq = frequency of recoomentdewojiejrgj ingestion
    '''
    def __init__(self, id, cmNme, sciName, tmeLastIng, dos, freq):
        self.ID = id
        self.CommonName = cmNme
        self.ScientificName = sciName
        self.LastIngestionTime = tmeLastIng
        self.Dosage = dos
        self.Frequency = freq

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def calcTimeToIngestion(self):
        pass


class Test(object):
    '''
    dt = date of test
    drNm = name of doctor
    typ = type of test
    rslt = result of test
    extra = extra information
    app = appointment test happenned
    '''
    def __init__(self, id, dt, drNm, typ, rslt, extra, app):
        self.ID = id
        self.Date = dt
        self.DRName = drNm
        self.TestType = typ
        self.TestResult = rslt
        self.ExtraInfo = extra
        self.Appoint = app

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class Appointment(object):
    '''
    dt = date of app
    patient = id of the client
    dt = date
    rea = reason for appointment
    rs = results of app
    doc = doctor id
    typ = type of appointment
    extra = extrainfo
    priv = privaet info
    '''
    def __init__(self, id, patient, dt, rea , rs, doc, typ, extra, priv):
        self.ID = id
        self.Date = dt
        self.Patient = patient
        self.Doctor = doc
        self.Reason = rea
        self.Results = rs
        self.Type = typ
        self.ExtraInfo = extra
        self.PrivateNotes = priv

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)