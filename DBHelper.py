import sqlite3


class Helper:

    def __init__(self, db_path:str):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    #attempts to write student to the db using a tuple passed in
    def write_new_student(self, new_info: tuple) -> bool:
        try:
            self.c.execute("INSERT INTO StudentDB(FirstName,LastName,GPA,Major,FacultyAdvisor,isDeleted)"
                           "VALUES(?,?,?,?,?,?);", new_info)
            self.conn.commit()
            return True
        except Exception as e:
            return False
    def get_all_students(self):
        try:
            results = self.c.execute("SELECT StudentId,FirstName,LastName,GPA,Major,FacultyAdvisor "
                                     "FROM StudentDB "
                                     "WHERE isDeleted = 0;")
            results = results.fetchall()
            return results
        except:
            return None
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
