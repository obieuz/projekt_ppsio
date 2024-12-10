from classes.KorpoManager import KorpoManager
from classes.Menago import Menago
from classes.Robol import Robol
from database.database_init import init_tables
from database.databaseService import DatabaseService

init_tables()

manager = KorpoManager()


robol1 = Robol(1,"Adam", "Nowak", 25)
robol2 = Robol(2,"Pies", "Tesla", 25, 80)
robol3 = Robol(3,"Moskwa", "Kot", 25, 120)

menago = Menago(4,"Jan", "Kowalski", 100, [], 3)

manager.add_employee(menago)
manager.add_employee(robol1)
manager.add_employee(robol2)
manager.add_employee(robol3)

DatabaseService = DatabaseService()

print(DatabaseService.get_robols())
print(DatabaseService.get_managers())

manager.edit_employee(Robol(1, "Maciek", "Nowak", 25, 80))

print(manager.get_workers())

manager.edit_employee(Robol(10, "Maciek", "Nowak", 25, 80))


