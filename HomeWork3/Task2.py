class TestPaper:
    subject = ["Math", "Chemistry", "Computing"]
    mark_scheme = {"Math": ["1D", "2C", "3A", "4B", "5A"],
                   "Chemistry": ["1A", "2C", "3A", "4B", "5D"],
                   "Computing": ["1B", "2D", "3A", "4B", "5C"]
                   }
    pass_mark = {"Math": "60%",
                 "Chemistry": "75%",
                 "Computing": "75%"
                 }

    def __init__(self, min_point, subject_name, correct_answers=[]):
        self.min_point = min_point
        self.subject_name = subject_name
        self.min_point = correct_answers




class Student(TestPaper):
    tests_taken = 'No tests taken'

    def __init__(self, min_point, subject_name, students_answers=[]):
        super().__init__(min_point, subject_name)
        self.students_answers = students_answers

    def take_test(self):
        if self.students_answers ==

