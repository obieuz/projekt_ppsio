import unittest
from unittest.mock import MagicMock
from classes.KorpoManager import KorpoManager
from classes.Worker import Worker
from classes.Menago import Menago
from classes.Robol import Robol

class TestKorpoManager(unittest.TestCase):

    def setUp(self):
        self.korpo_manager = KorpoManager()
        self.korpo_manager.DatabaseService = MagicMock()

    def test_add_employee(self):
        robol = Robol(1, "John", "Doe", "Engineer", 5000, 40)
        menago = Menago(2, "Jane", "Smith", "Manager", [], 7000, 50)

        self.korpo_manager.workers = [menago]

        self.korpo_manager.add_employee(robol)
        self.assertIn(robol, self.korpo_manager.workers)
        self.korpo_manager.DatabaseService.add_employee.assert_called_with(robol)

        with self.assertRaises(ValueError):
            self.korpo_manager.add_employee(robol)

        with self.assertRaises(ValueError):
            self.korpo_manager.add_employee("Not a Worker")

    def test_remove_employee_from_team(self):
        robol = Robol(1, "John", "Doe", "Engineer", 5000, 40)
        menago = Menago(2, "Jane", "Smith", "Manager", [robol], 7000, 50)

        self.korpo_manager.workers = [menago, robol]

        self.korpo_manager.remove_employee_from_team(robol)
        self.assertNotIn(robol, menago.workers)

        with self.assertRaises(ValueError):
            self.korpo_manager.remove_employee_from_team("Not a Worker")

    def test_fire_employee(self):
        robol = Robol(1, "John", "Doe", "Engineer", 5000, 40)
        menago = Menago(2, "Jane", "Smith", "Manager", [robol], 7000, 50)

        self.korpo_manager.workers = [menago, robol]

        self.korpo_manager.fire_employee(robol)
        self.assertNotIn(robol, self.korpo_manager.workers)
        self.korpo_manager.DatabaseService.remove_employee.assert_called_with(robol)

        with self.assertRaises(ValueError):
            self.korpo_manager.fire_employee("Not a Worker")

    def test_get_employee(self):
        robol = Robol(1, "John", "Doe", "Engineer", 5000, 40)
        self.korpo_manager.workers = [robol]

        self.assertEqual(self.korpo_manager.get_employee(1), robol)
        self.assertIsNone(self.korpo_manager.get_employee(2))

    def test_edit_employee(self):
        robol = Robol(1, "John", "Doe", "Engineer", 5000, 40)
        updated_robol = Robol(1, "John", "Doe", "Senior Engineer", 6000, 40)
        self.korpo_manager.workers = [robol]

        self.korpo_manager.edit_employee(updated_robol)
        self.assertIn(updated_robol, self.korpo_manager.workers)
        self.korpo_manager.DatabaseService.edit_employee.assert_called_with(updated_robol)

        with self.assertRaises(ValueError):
            self.korpo_manager.edit_employee("Not a Worker")

if __name__ == '__main__':
    unittest.main()