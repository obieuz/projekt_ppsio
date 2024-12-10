from abc import ABC, abstractmethod

class Worker(ABC):
    def __init__(self,employee_id,name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.output = 0
        self.employee_id = employee_id

    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def shout(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_into(self):
        pass