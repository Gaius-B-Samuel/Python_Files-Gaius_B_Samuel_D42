# Question 1: University Course Catalog
class Course:
    def __init__(self,course_code,course_name,credit_hours):
        self.course_code=course_code
        self.course_name=course_name
        self.credit_hours=credit_hours

    def display_info(self):
        return f"{self.course_code}: {self.course_name} ({self.credit_hours} credit hours)"

class CoreCourse(Course):
    def __init__(self,course_code,course_name,credit_hours,required_for_major):
        self.course_code=course_code
        self.course_name=course_name
        self.credit_hours=credit_hours
        self.required_for_major=required_for_major

    def display_info(self):
        return f"{self.course_code}: {self.course_name} ({self.credit_hours} credit hours) - Major Requirement: {self.required_for_major}"

class ElectiveCourse(Course):
    def __init__(self,course_code,course_name,credit_hours,elective_type):
        Course.__init__(self,course_code,course_name,credit_hours)
        self.elective_type=elective_type

    def display_info(self):
        return f"{self.course_code}: {self.course_name} ({self.credit_hours} credit hours) - Elective Type: {self.elective_type}"

core=CoreCourse("CS101","Introduction to Computer Science",3,True)
elective=ElectiveCourse("HIST202","World History",2,"liberal arts")
print(core.display_info())
print(elective.display_info())

# Question 2: Employee Module
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary

if __name__ == "__main__":
    emp = Employee("John Tom",50000)
    print("Employee Name:",emp.get_name())
    print("Employee Salary:",emp.get_salary())
