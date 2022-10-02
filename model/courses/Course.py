

class Course:

    def __init__(self, id , hours , name , desc):
        self.__id = id
        self.__hours = hours
        self.__name = name
        self.__desc = desc


    def get_id(self):
        return self.__id