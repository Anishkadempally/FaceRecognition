import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendance-firebase-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "116":
        {
            "name": "Venu Madhav",
            "major": "Comedy",
            "starting_year" : 1999,
            "total_attendance" : 90,
            "CGPA" : 9,
            "year" : 4,
            "last_attendance_time" : "2024-05-02 00:54:34",

        },
    "118":
        {
            "name": "Elon Musk",
            "major": "Science",
            "starting_year" : 2008,
            "total_attendance" : 95,
            "CGPA" : 10,
            "year" : 6,
            "last_attendance_time" : "2024-03-02 00:12:34",

        },
    "260":
        {
            "name": "Andre Russell",
            "major": "Cricket",
            "starting_year" : 2012,
            "total_attendance" : 80,
            "CGPA" : 7,
            "year" : 2,
            "last_attendance_time" : "2024-03-02 11:12:34",

        },

    "588":
        {
            "name": "Anish",
            "major": "Engineering",
            "starting_year" : 2016,
            "total_attendance" : 88,
            "CGPA" : 8,
            "year" : 3,
            "last_attendance_time" : "2024-05-02 11:54:34",

        },

    "720":
        {
            "name": "Kane",
            "major": "Cricket",
            "starting_year" : 2018,
            "total_attendance" : 95,
            "CGPA" : 9,
            "year" : 4,
            "last_attendance_time" : "2024-05-02 01:24:34",

        },
}

for key,value in data.items():
    ref.child(key).set(value)
