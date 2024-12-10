from classes.Worker import Worker


class Robol(Worker):
    def __init__(self, employee_id, name, surname, salary, quota=40, energy=20):
        super().__init__(employee_id,name, surname, salary)
        self.manager_id = None
        self.quota = quota
        self.energy = energy

    def work(self):
        if self.energy < 0:
            self.energy = 0
            print(f"{self.name} {self.surname} aura mu sie skonczyla.")
            return;
        self.energy -= 2

        if self.quota < self.output:
            print(f"{self.name} {self.surname} nie jest kaktusem i tez moze sie napic.")
        self.output += 1

    def rest(self):
        self.energy += 1

    def shout(self):
        print(f'Wiek nie ma znaczenia, chyba że jesteś serem - {self.name} {self.surname}')

    def get_into(self):
        return f"Robol {self.name} {self.surname} zrobil {self.output / self.quota * 100}% wymagan."

    def calculate_salary(self):
        return self.salary * self.output
