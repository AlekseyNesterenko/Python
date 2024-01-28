class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid name: {self.value}. Name should be a non-empty string.'

class InvalidAgeError(Exception):
    pass

class InvalidIdError(Exception):
    pass


class Person:
    def __init__(self, last_name, name, second_name, age):
        if (not last_name) or (not isinstance(last_name, str)):
            raise  InvalidNameError(last_name)
        if (not name) or (not isinstance(name, str)):
            raise  InvalidNameError(name)
        if (not second_name) or (not isinstance(second_name, str)):
            raise  InvalidNameError(second_name)
        if age <= 0:
            raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')
        self.last_name = last_name
        self.name = name
        self.second_name = second_name
        self.age = age

    def birthday(self):
        self.age = +1
    
    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, last_name, name, second_name, age, id):
        super().__init__(last_name, name, second_name, age)
        if not (100000 < id <= 999999):
            raise InvalidIdError(f'Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.')
        self.id = id

    def get_level(self):
        result = 0
        for chr in str(self.id):
            result += int(chr)
        return (result % 7)    







employee = Employee("Bob", "Johnson", "Brown", 40, 12345)




print()