""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.haxa6if.mongodb.net/pytech"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" three student documents"""
# Jacob Koscinski's data document 
jacob = {
    "student_id": "1007",
    "first_name": "Jacob",
    "last_name": "Koscinski",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.9",
            "start_date": "January 02, 2023",
            "end_date": "March 05, 2023",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Database Security",
                    "instructor": "Professor Henry Le",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Computer Forensics",
                    "instructor": "Professor Anthony Geron",
                    "grade": "A"
                }
            ]
        }
    ]

}

# John Wick data document 
john = {
    "student_id": "1008",
    "first_name": "John",
    "last_name": "Wick",
    "enrollments": [
          {
            "term": "Session 2",
            "gpa": "3.9",
            "start_date": "January 02, 2023",
            "end_date": "March 05, 2023",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Database Security",
                    "instructor": "Professor Henry Le",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Computer Forensics",
                    "instructor": "Professor Anthony Geron",
                    "grade": "A"
                }
            ]
        }
    ]
}

# Timothy Tim data document
timothy = {
    "student_id": "1009",
    "first_name": "Timothy",
    "last_name": "Tim",
    "enrollments": [
          {
            "term": "Session 2",
            "gpa": "3.9",
            "start_date": "January 02, 2023",
            "end_date": "March 05, 2023",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Database Security",
                    "instructor": "Professor Henry Le",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Computer Forensics",
                    "instructor": "Professor Anthony Geron",
                    "grade": "A"
                
                }
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
jacob_student_id = students.insert_one(jacob).inserted_id
print("  Inserted student record Jacob Koscinski into the students collection with document_id " + str(jacob_student_id))

john_student_id = students.insert_one(john).inserted_id
print("  Inserted student record John Wick into the students collection with document_id " + str(john_student_id))

timothy_student_id = students.insert_one(timothy).inserted_id
print("  Inserted student record Timothy Tim into the students collection with document_id " + str(timothy_student_id))

input("\n\n  End of program, press any key to exit... ")
