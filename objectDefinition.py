import sys, os, json

class User(object):
    '''
    id = int
    n = name, ty = type of user(0, 1, 2) -- int, em = email, birth = birthdate -- int, h = height -- double, w = weight -- double,
    al = list of strings for allergies, bloTy = bloodtype, medCond = list of strings, gen = gender -- binary
    '''
    def __init__(self, id, n, ty, em, birth, h, w, al, bloTy, medCond, gen, syst, dias):
        self.ID = id
        self.Name = n
        self.UsrType = ty
        self.Email = em
        self.Birthdate = birth
        self.Height = h
        self.Weight = w
        self.Allergies = al
        self.BloodType = bloTy
        self.MedicalConditions = medCond
        self.Gender = gen
        self.Systole = syst
        self.Diastole = dias

        #list of Ids
        self.appointments = []
        #list of medication objs , empty for doctor or authority
        self.medications = []

    # App is int ID for appointment that will be added to list of appointments
    def addAppointment(self, App):
        self.appointments.append(App)
    # Med is medication objects
    def addMed(self, Med):
        self.medications.append(Med)
    def calcAge(self):
        pass

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