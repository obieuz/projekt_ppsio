from classes.Worker import Worker
from classes.Menago import Menago
from classes.Robol import Robol
from database.databaseService import DatabaseService


class KorpoManager:
    def __init__(self, host="localhost", user="root", password="maslo", database="korpo"):
        self.workers = []
        self.DatabaseService = DatabaseService(host, user, password, database)

        self.init_employees()

    def init_employees(self):
        for robol in self.DatabaseService.get_robols():

            employee = Robol(robol[0], robol[1], robol[2], robol[3], robol[4], robol[5])
            employee.manager_id = robol[6]
            self.workers.append(employee)

        for menago in self.DatabaseService.get_managers():
            workers = []
            for worker in self.workers:
                if isinstance(worker, Menago):
                    continue
                if worker.manager_id == menago[0]:
                    workers.append(worker)
            employee = Menago(menago[0], menago[1], menago[2], menago[3], workers, menago[4], menago[5])

            self.workers.append(employee)

    def add_employee(self, employee):
        if not isinstance(employee, Worker):
            raise ValueError("Worker must be instance of Worker class")

        for w in self.workers:
            if w.employee_id == employee.employee_id:
                raise ValueError("Nie tak szybko, ktos juz ma to id")

        if isinstance(employee, Robol):
            for w in self.workers:
                if isinstance(w, Menago):
                    if w.add_worker(employee):
                        print(f"{employee.name} {employee.surname} zostal dodany do zespolu {w.name} {w.surname}")
                        employee.manager_id = w.employee_id
                        break

        self.workers.append(employee)
        self.DatabaseService.add_employee(employee)

    def remove_employee_from_team(self, worker):
        if not isinstance(worker, Worker):
            raise ValueError("Worker must be instance of Worker class")

        for w in self.workers:
            if isinstance(w, Menago):
                if w.remove_worker(worker):
                    print(f"{worker.name} {worker.surname} zostal usuniety z zespolu {w.name} {w.surname}")
                    break

    def fire_employee(self, worker):
        if not isinstance(worker, Worker):
            raise ValueError("Worker must be instance of Worker class")

        self.remove_employee_from_team(worker)

        for w in self.workers:
            if w.employee_id == worker.employee_id:
                self.workers.remove(w)
                break

        self.DatabaseService.remove_employee(worker)

    def get_employee(self, employee_id):
        for worker in self.workers:
            if worker.employee_id == employee_id:
                return worker
        return None

    def edit_employee(self,employee):
        if not isinstance(employee, Worker):
            raise ValueError("Worker must be instance of Worker class")

        for w in self.workers:
            if w.employee_id == employee.employee_id:
                self.workers.remove(w)
                self.workers.append(employee)
                break

        self.DatabaseService.edit_employee(employee)

    def get_workers(self):
        for worker in self.workers:
            print(worker.get_into())

    def calculate_salaries(self):
        total = 0
        for worker in self.workers:
            total += worker.calculate_salary()
        return total

    def work(self, duration=1):
        for _ in range(duration):
            for worker in self.workers:
                worker.work()

    def rest(self):
        for worker in self.workers:
            worker.rest()

    def shout(self):
        for worker in self.workers:
            worker.shout()
