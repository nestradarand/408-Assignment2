import pandas as pd
from pandas import DataFrame
from Student import Student
from DBHelper import Helper
from InputChecker import Checker

DB_PATH = "C:\\Users\\noahe\\PycharmProjects\\Assignment1_408\\venv\\StudentDB.sqlite"



def main():
    main_menu = "Welcome to the Student Catalog System, the following are available:\n"
    options = "1.) Display all students in database\n2.) Register New Student" \
              "\n3.) Update Student Information\n4.) Delete Student By ID" \
              "\n5.) Search + Display Students by Category\n6.) Exit application"
    running = True
    db_helper = None
    try:
        db_helper = Helper(DB_PATH)
    except Exception as e:
        print("!!!!Error connecting to database, aborting!!!!")
        running = False

    print(main_menu)
    while running:
        print(options)
        try:
            user_choice = int(input("Command:"))
            ###quits the app
            if(user_choice==6):
                print("---Application Exited---")
                break
            elif(user_choice == 1):
                result = db_helper.get_all_students()
                res_df = DataFrame(result,columns = ["StudentId","First Name",
                                                     "Last Name","GPA","Major","Advisor"])
                if(len(res_df) == 0):
                    print("!!!No Students to Display!!!")
                else:
                    print(res_df)
            elif(user_choice == 4):
                try:
                    result = int(input("Enter the id number of the student to delete:>"))
                    worked = db_helper.delete_student(result)
                    if(worked):
                        print("Student successfully removed.")
                    else:
                        print("A student with that ID was not found")
                except ValueError:
                    print("!!!Ivalid input entered!!!")
            elif user_choice == 5:
                print("You can search students by entering\n"
                      "1 for GPA\n"
                      "2 for Major\n"
                      "3 for Faculty Advisor")
                try:
                    user_choice = int(input("Enter your choice:>"))
                    if user_choice == 3:
                        advisor = input("Enter the advisor to search by:>")
                        result = db_helper.get_students_advisor(advisor)
                        if result:
                            df = DataFrame(result,columns = ["StudentId","First Name",
                                                     "Last Name","GPA","Major","Advisor"])
                            print(df)
                        else:
                            print("---No student to display---")
                    elif user_choice == 2:
                        major = input("Enter the major to search by:>")
                        result = db_helper.get_students_major(major)
                        if result:
                            df = DataFrame(result, columns=["StudentId", "First Name",
                                                            "Last Name", "GPA", "Major", "Advisor"])
                            print(df)
                        else:
                            print("---No student to display---")
                    elif user_choice == 1:
                        try:
                            gpa = float(input("Enter the GPA value to match students:>"))
                            result = db_helper.get_students_GPA(gpa)
                            if result:
                                df = DataFrame(result, columns=["StudentId", "First Name",
                                                                "Last Name", "GPA", "Major", "Advisor"])
                                print(df)
                            else:
                                print("---No student to display---")
                        except ValueError:
                            print("!!!Invalid GPA entered!!!")
                except ValueError:
                    print("!!!Invalid choice entered")

            elif(user_choice == 2):
                first_name = input("Enter the student's first name:>")
                if(Checker.is_pure_text(first_name)):
                    last_name = input("Enter the student's last name:>")
                    if(Checker.is_pure_text(last_name)):
                        try:
                            gpa = float(input("Enter the student's GPA:>"))
                            major = input("Enter the student's major:>")
                            if(Checker.is_pure_text(major)):
                                advisor = input("Enter the name of the student's advisor:")
                                if(Checker.is_pure_text(advisor)):
                                    try:
                                        new_stud = Student(first_name,last_name,gpa,major,advisor)
                                        db_helper.write_new_student(new_stud.get_tuple())
                                        print("---New Student Successfully Added--")
                                    except:
                                        print("Error adding student to database")
                                else:
                                    print("!!!Invalid advisor entered!!!")
                            else:
                                print("!!!Invalid major entered!!!")
                        except:
                            print("!!!Invalid GPA entered!!!")
                    else:
                        print("!!!Invalid last name entered!!!")

                else:
                    print("!!!Invalid first name entered!!!")

            elif(user_choice == 3):
                try:
                    choice = int(input("You can either edit a student's Major or Advisor:\n"
                                     "Enter 1 for Major or 2 for Advisor\nCommand:>"))
                    if choice == 1 or choice == 2:
                        student_id = int(input("Enter the ID of the student you wish to edit:>"))
                        if choice == 1:
                            new_maj = input("Enter the new major of the student:>")
                            if Checker.is_pure_text(new_maj):
                                result = db_helper.update_major(student_id,new_maj)
                                if result:
                                    print("---Student successfully updated---")
                                else:
                                    print("!!!Failed to update student's major---")
                            else:
                                print("!!!Invalid Major entered!!!")
                        elif choice == 2:
                            new_advisor = input("Enter the new faculty advisor for the student:>")
                            if Checker.is_pure_text(new_advisor):
                                result = db_helper.update_advisor(student_id,new_advisor)
                                if result:
                                    print("---Student successfully updated---")
                                else:
                                    print("!!!Failed to update student's advisor!!!")
                            else:
                                print("!!!Invalid advisor entered!!!")
                    else:
                        print("!!!Invalid command entered!!!")

                except ValueError:
                    print("!!!Invalid input entered!!!")
        except ValueError:
            print("!Invalid input entered, please try again!")


if __name__ == "__main__":
    main()
