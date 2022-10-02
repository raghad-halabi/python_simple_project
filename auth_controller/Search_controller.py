from model.users_db.Student import Student


class Search_controller:

    # You can pass the student list here, or access it directly from App_Auth file by App_Auth.studnets_list
    # Don't forget to check if list is empty for not
    def search_for_student_by_id(self, id: int, student_list: list[Student]):
        if student_list == None or len(student_list) == 0:
            return None
        else:
              for item in student_list:
                 if item.get_id() == id:
                      return item
