class Student:
    def __init__(self, first_name, last_name, domain, class_level):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name[0:1].lower() + last_name.lower() + domain
        self.class_level = class_level
        self.domain = domain

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.class_level}\n'
