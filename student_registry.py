class Student:
    def __init__(self,name,age=13,grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade  

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
            if type(new_name) != str:
               return
            if len(new_name) < 3:
               return
            if " " in new_name:
               return
            if not new_name.isalpha():
                raise Exception("Invlaid name.")
            if new_name.title() != new_name:
               return
            self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if type(new_age) != int:
            return
        if new_age < 11 or new_age> 18:
            return
        self._age = new_age
        
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, new_grade):
        grade_num = int(new_grade[:-2])
        if grade_num < 9 or grade_num > 12:
            return
        if not new_grade.endswith("th"):
            return
        self._grade = new_grade 
    
    def __str__(self):
        return f"Student 1: {self.name}, Age: {self.age}, Grade: {self.grade}"
    def advance(self):
        advance_age = int(self.grade[:-2]) + 1
        return f"{self.name} has advanced to {advance_age}th grade"
    def study(self, field):
        return f"{self.name} is studying {field}"