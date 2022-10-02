from model.users_db.Employeer import Employer
from model.users_db.Student import Student
from utils.Utils import Constatns


class App_Auth:

    employers_list: list[Employer] = [
        Employer(1, "Ahmad", 223, "3123", Constatns.FULL_TIME, "Bahaa", "123"),
        Employer(2, "Sami", 223, "3123", Constatns.FULL_TIME, "Sami", "456"),
        Employer(3, "Zain", 223, "3123", Constatns.FULL_TIME, "Zain", "789")
    ]

    studnets_list: list[Student] = [
        Student(1, "Ahmad", 223, "3123", Constatns.FULL_TIME, "3213"),
        Student(2, "Sami", 223, "3123", Constatns.FULL_TIME, "12d"),
        Student(3, "Zain", 223, "3123", Constatns.FULL_TIME, "3214")
    ]

    def get_last_id(self) -> int:
        return self.studnets_list[len(self.studnets_list) - 1].get_id()

    def login(self, username: str, password: str) -> bool:
        for item in self.employers_list:
            if username == item.get_username() and password == item.get_password():
                return True
        return False

    def register_new_user(self, user: Employer):
        if not self.check_if_user_exsist(user.get_username()):
            self.employers_list.append(user)
        else:
            print("User already Used!")

    def register_new_studnet(self, user: Student):
        if not self.check_if_user_exsist(user.get_username()):
            self.studnets_list.append(user)
        else:
            print("User already Used!")

        print(len(self.studnets_list))

    def check_if_user_exsist(self, username: str):
        for item in self.employers_list:
            if item.get_username() == username:
                return True
        return False


    def get_student_list(self):
        return self.studnets_list