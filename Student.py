
#works
class Student:
    def __init__(self,new_first:str,new_last:str,new_gpa:float,new_major:str,new_advisor:str):
        self.first_name = new_first
        self.last_name = new_last
        self.gpa = new_gpa
        self.major = new_major
        self.advisor = new_advisor
        self.is_deleted = 0
    def get_name(self) -> str:
        returner = self.first_name + " " + self.last_name
        return returner
    def get_first(self) -> str:
        return self.first_name
    def get_last(self) -> str:
        return self.last_name
    def get_gpa(self) -> float:
        return self.gpa
    def get_major(self) -> str:
        return self.major
    def get_advisor(self) -> str:
        return self.advisor
    def get_deleted(self) ->bool:
        return self.is_deleted
    def set_first(self,new_first:str):
        self.first_name = new_first
    def set_last(self, new_last: str):
        self.last_name = new_last
    def set_gpa(self, new_gpa: float):
        self.gpa = new_gpa
    def set_major(self,new_major:str):
        self.major = new_major
    def set_advisor(self, new_advisor: str):
        self.advisor = new_advisor
    def set_deleted(self,new_bool:bool):
        self.is_deleted = new_bool
    def get_tuple(self) -> tuple:
        return (self.get_first(),self.get_last(),self.get_gpa(),self.get_major(),self.get_advisor(),self.get_deleted())

