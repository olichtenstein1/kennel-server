class Employee():

    def __init__(self, id, name, location_id, location = None):
        self.id = id
        self.name = name
        self.location_id = location_id
        self.location = location
        
        
new_employee = Employee(1, "Tim McArthur",2)