import sys, os

class User(object):
    '''
    id = int
    n = name, ty = type of user(0, 1, 2) -- int, em = email, birth = birthdate -- int, h = height -- float, w = weight -- float,
    al = list of strings for allergies, bloTy = bloodtype, medCond = list of strings, gen = gender -- binary
    '''
    def __init__(self, id, n, ty, em, birth, h, w, al, bloTy, medCond, gen):
        self.ID = id
        self.definition = {"Name": n, "UserType": ty, "Email": em, "BirthDate": birth, "Height": h,
                           "Weight":w, "Allergies": al, "BloodType": bloTy,
                           "MedicalConditions":medCond, "Gender":gen
                           }
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


class Medication