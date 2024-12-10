from classes.Worker import Worker

class Menago(Worker):
    def __init__(self,employee_id,name, surname, salary, workers, team_size, energy = 25):
        super().__init__(employee_id,name, surname, salary)
        self.workers = workers
        self.energy = energy
        self.team_size = team_size

    def work(self):
        if self.energy < 0:
            self.energy = 0
            print(f"{self.name} {self.surname} aura mu sie skonczyla.")
            return;
        self.energy -= 3

        self.output += 1

    def rest(self):
        self.energy += 1

    def add_worker(self, worker):
        if len(self.workers) >= self.team_size:
            return False

        self.workers.append(worker)
        return True

    def remove_worker(self, worker):
        for w in self.workers:
            if w.employee_id == worker.employee_id:
                self.workers.remove(w)
                return True
        return False



    def shout(self):
        print(f'Nie rozpaczaj, że ludzie Cię nie rozumieją. Martw się tym, że to ty nie rozumiesz ludzi - {self.name} {self.surname}' )

    def get_into(self):
        return f"Menago {self.name} {self.surname} zarzadzil {len(self.workers)} pracownikami."

    def calculate_salary(self):
        for worker in self.workers:
            self.output += worker.output

        return self.salary * self.output
