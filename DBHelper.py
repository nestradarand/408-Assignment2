import sqlite3

'''
The DBHelper module serves to act as an object to abstract the majority of interactions with the StudentDB table
Must have a valid path to database passed to constructor to function correctly.
'''

##main class is helper
class Helper:
    ##pass path to db in to establish connection
    def __init__(self, db_path:str):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    #attempts to write student to the db using a tuple passed in
    #returns true for success and false for failure to write
    def write_new_student(self, new_info: tuple) -> bool:
        try:
            self.c.execute("INSERT INTO StudentDB(FirstName,LastName,GPA,Major,FacultyAdvisor,isDeleted)"
                           "VALUES(?,?,?,?,?,?);", new_info)
            self.conn.commit()
            return True
        except Exception as e:
            return False
    #attempts to return all students with the exception of isDeleted attribute
    #returns null if this fails for some reason
    def get_all_students(self):
        try:
            results = self.c.execute("SELECT StudentId,FirstName,LastName,GPA,Major,FacultyAdvisor "
                                     "FROM StudentDB "
                                     "WHERE isDeleted = 0;")
            results = results.fetchall()
            return results
        except:
            return None
    #Updates major for given student id number
    #returns true if success, false if failure
    def update_major(self,student_id:int,new_major:str) -> bool:
        new_tuple = (new_major,student_id,)
        try:
            self.c.execute("UPDATE StudentDB "
                           "SET Major = ? "
                           "WHERE StudentId = ?;",new_tuple)
            self.conn.commit()
            return True
        except:
            return False
    #updates the advisor for specified student
    #returns true if success, false if failure
    def update_advisor(self,student_id:int,new_advisor:str):
        new_tuple = (new_advisor,student_id,)
        try:
            self.c.execute("UPDATE StudentDB "
                           "SET FacultyAdvisor = ? "
                           "WHERE StudentId = ?;",new_tuple)
            self.conn.commit()
            return True
        except:
            return False
    #sets a student's isDeleted field to True
    #returns true if success false if not
    def delete_student(self,student_id:int):
        new_tuple = (student_id,)
        try:
            self.c.execute("UPDATE StudentDB "
                           "SET isDeleted = 1 "
                           "WHERE StudentDB.StudentId = ?",new_tuple)
            self.conn.commit()
            return True
        except Exception as e:
            return False
    ###querys students info by advisor
    #returns None if the operation fails
    def get_students_advisor(self,advisor_name:str):
        new_tuple = (advisor_name,)
        try:
            results = self.c.execute("SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor "
                                     "FROM StudentDB "
                                     "WHERE FacultyAdvisor = ? ",new_tuple)
            results = results.fetchall()
            return results
        except:
            return None
    #returns students based on a specified major
    #returns None if fails
    def get_students_major(self,major_name:str):
        new_tuple = (major_name,)
        try:
            results = self.c.execute("SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor "
                                     "FROM StudentDB "
                                     "WHERE Major = ? ",new_tuple)
            results = results.fetchall()
            return results
        except:
            return None
    #returns students by a given GPA
    #returns None if operation fails or if ID not found
    def get_students_GPA(self,gpa:float):
        new_tuple = (gpa,)
        try:
            results = self.c.execute("SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor "
                                     "FROM StudentDB "
                                     "WHERE GPA = ? ",new_tuple)
            results = results.fetchall()
            return results
        except:
            return None
