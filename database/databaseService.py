import mysql.connector

from classes.Menago import Menago
from classes.Robol import Robol


class DatabaseService:
    def __init__(self, host="localhost", user="root", password="maslo", database="korpo"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def add_manager(self, manager):
        if not isinstance(manager, Menago):
            raise ValueError("Manager must be instance of Menago class")

        with mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                                    INSERT INTO employees (id,name, surname, salary, energy)
                                    VALUES (%s,%s, %s, %s, %s)
                                """, (manager.employee_id,manager.name, manager.surname, manager.salary, manager.energy))

                cursor.execute("""
                    INSERT INTO managers (employee_id, team_size)
                    VALUES (%s, %s)
                """, (manager.employee_id, manager.team_size))

                connection.commit()

    def add_robol(self, robol):
        if not isinstance(robol, Robol):
            raise ValueError("Worker must be instance of Worker class")
        with mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                                                    INSERT INTO employees (id,name, surname, salary, energy)
                                                    VALUES (%s,%s, %s, %s, %s)
                                                """, (robol.employee_id,robol.name, robol.surname, robol.salary, robol.energy))

                cursor.execute("""
                                    INSERT INTO workers (employee_id, quota, manager_id)
                                    VALUES (%s, %s, %s)
                                """, (robol.employee_id, robol.quota, robol.manager_id))

                connection.commit()

    def add_employee(self, employee):
        if isinstance(employee, Robol):
            self.add_robol(employee)

        elif isinstance(employee, Menago):
            self.add_manager(employee)

        else:
            raise ValueError("Employee must be instance of Worker or Menago class")

    def get_robols(self):
        with mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT employee_id,name,surname,salary,energy,quota,manager_id FROM employees JOIN workers ON employees.id = workers.employee_id
                """)
                return cursor.fetchall()

    def get_managers(self):
        with mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT employee_id,name,surname,salary,team_size,energy FROM employees JOIN managers ON employees.id = managers.employee_id
                """)
                return cursor.fetchall()

    def remove_employee(self, worker):
        with mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM employees WHERE id = %s
                """, (worker.employee_id,))
                connection.commit()
                cursor.execute("""
                    DELETE FROM workers WHERE employee_id = %s
                """, (worker.employee_id,))
                connection.commit()
                cursor.execute("""
                    DELETE FROM managers WHERE employee_id = %s
                """, (worker.employee_id,))
                connection.commit()
                print(f"Usunieto pracownika {worker.name} {worker.surname}")

    def edit_employee(self, employee):
        with mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM employees WHERE id = %s
                """, (employee.employee_id,))
                if cursor.fetchone() is None:
                    raise ValueError("Employee does not exist")

        self.remove_employee(employee)
        self.add_employee(employee)

        print(f"Zkrawędziowano pracownika {employee.name} {employee.surname}")


