import json
import os


# Function 1:
def names_of_registered_students(input_json_path, course_name):
    with open(input_json_path, 'r') as dataFile:
        dataFileDict = json.load(dataFile)
    registeredStudents = []
    for studentInfo in dataFileDict.values():
        studentName = studentInfo["student_name"]
        studentCourses = studentInfo["registered_courses"]
        if(course_name in studentCourses):
            registeredStudents.append(studentName)
    return registeredStudents
    pass


# Function 2:
def enrollment_numbers(input_json_path, output_file_path):
    with open(input_json_path, 'r') as dataFile:
        dataFileDict = json.load(dataFile)
    coursesEnrollment = {}
    courses = []
    for studentInfo in dataFileDict.values():
        studentCourses = studentInfo["registered_courses"]
        for course in studentCourses:
            if(course not in coursesEnrollment):
                coursesEnrollment[course] = 1
                courses.append(course)
            else:
                coursesEnrollment[course]+=1
        courses.sort()
        with open(output_file_path,'w')  as outputFile:
            for course in courses:
                outputFile.write("\"{}\" {}{}".format(course, coursesEnrollment[course],'\n'))
    pass


# Function 3:
def courses_for_lecturers(json_directory_path, output_json_path):
    jsonFiles = [jsonFile for jsonFile in os.listdir(json_directory_path) if jsonFile.endswith(".json")]
    lectureresAndTheirCourses = {}
    for jsonFile in jsonFiles:
        with open(jsonFile,'r') as dataFile:
            dataFileDict = json.load(dataFile)
        for courseInfo in dataFileDict.values():
            lecturers = courseInfo["lecturers"]
            for lecturer in lecturers:
                if(lecturer not in lectureresAndTheirCourses):
                    lectureresAndTheirCourses[lecturer] = [courseInfo["course_name"]]
                else:
                    if(courseInfo["course_name"] not in lectureresAndTheirCourses[lecturer]):
                        lectureresAndTheirCourses[lecturer] += [courseInfo["course_name"]]
    with open(output_json_path,'w') as outputFile:
        json.dump(lectureresAndTheirCourses, outputFile, indent = 4)
    pass