from model.users_db.Person import Person


class Employer(Person):

    def __init__(self, id, name, salary, phone_number, employment_type , username, password ):
        self.__salary = salary
        self.__employment_type = employment_type
        super(Employer, self).__init__(id=id, name=name, phone_number=phone_number
                                       , user_name = username , password = password)


