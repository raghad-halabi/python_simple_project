from model.users_db.Person import Person


class Student(Person):

    def __init__(self, id, name, age, address, major, phone_number):
        self.__age = age
        self.__address = address
        self.__major = major
        super(Student, self).__init__(id=id, name=name, phone_number=phone_number)

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address
