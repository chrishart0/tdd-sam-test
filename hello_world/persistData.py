class PersistData:
    """Class for handling data persistance"""
    employee_dict = {}

    def persist_employee(self, first_name, middle_name, last_name, id):

        self.employee_dict[id] = {
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name
        }

        return {"is_recorded": True}

    def retrieve_employee(self, id):
        if id in self.employee_dict:
            return self.employee_dict[id]
        return None