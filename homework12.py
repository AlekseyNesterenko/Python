import csv

class Student:
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)
        
        

    def __setattr__(self, name, value):
        if name.istitle():
            raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        for char in name:
            if char.isdigit():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        
        return object.__setattr__(self, name, value)

    def __getattr__(self, name):
        
        return object.__getattribute__(self, name)
    
    
    def __str__(self):
        subjects = ', '.join(list(self.subjects.keys()))
        return f'Студент: {self.name}\nПредметы: {subjects}'

    def load_subjects(self, subjects_file):
            with open(subjects_file, 'r', encoding='utf-8') as file:
                data = file.readline().strip('\n').split(',')
                subject_data = {'grades':[], 'tests': []}
                return {k:subject_data for k in data}

    def add_grade(self, subject, grade):
        
        if grade < 2 and grade > 5:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        else:
            self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in list(self.subjects.keys()):
            raise ValueError(f'Предмет {subject} не найден')
        if test_score < 0 and test_score > 100:
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        else:
            self.subjects[subject]['tests'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in list(self.subjects.keys()):
            raise ValueError(f'Предмет {subject} не найден')
        res = self.subjects[subject]['tests']
        return (sum(res))/len(res)

    def get_average_grade(self): 
        res = []
        for i in self.subjects.values():
            res.extend(i['grades'])
        return (sum(res))/len(res)


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    print(student.subjects)
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("История")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
