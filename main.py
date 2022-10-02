from auth_controller.App_Auth import App_Auth
from auth_controller.Search_controller import Search_controller
from model.users_db.Student import Student
from utils.Utils import Methods_Utils


def get_input_from_user(app_auth: App_Auth):
    name = input("Enter studnet name: ")
    age = input("Enter studnet age: ")
    address = input("Enter studnet address: ")
    major = input("Enter studnet major: ")
    phone_number = input("Enter studnet phone_number: ")

    if Methods_Utils.check_value_is_empty(name, age, address, major, phone_number):
        print("Invaild inputs")
        return

    std = Student(name=name, age=age, address=address, major=major, phone_number=phone_number,
                  id=auth.get_last_id() + 1)
    app_auth.register_new_studnet(std)


print("Welcome,please add your crediual: ")

user_name = input("Username: ")
password = input("Password: ")

if Methods_Utils.check_value_is_empty(user_name, password):
    print("Empty fields")
    exit()

auth = App_Auth()
search_cont = Search_controller()

if auth.login(user_name, password):
    print("What you want to do: \n1_Add new student.\n2_ Search for user by id")

    emp_choice = input("User choice: ")
    if not Methods_Utils.check_value_is_empty(emp_choice):
        if emp_choice == "1":
            get_input_from_user(auth)
        elif emp_choice == "2":
            id_input = input("Enter user id: ")
            if not Methods_Utils.check_value_is_empty(id_input) and id_input.isdigit():
                search_student = search_cont.search_for_student_by_id(int(id_input), auth.get_student_list())

                if search_student != None:
                    print("Student Name: ", search_student.get_name()
                          , "\nStudent age: ", search_student.get_age())
