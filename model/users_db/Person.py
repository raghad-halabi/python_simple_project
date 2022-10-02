class Person:

    def __init__(self, id, name, phone_number, user_name="", password=""):
        self.__id = id
        self.__name = name
        self.__phone_number = phone_number
        self.__user_name = user_name
        self.__password = password

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__user_name


    def get_name(self):
        return self.__name


    def get_password(self):
        return self.__password
