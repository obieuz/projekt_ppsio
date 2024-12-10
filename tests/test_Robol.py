import unittest
from classes.Robol import Robol

class TestRobol(unittest.TestCase):

    def setUp(self):
        self.robol = Robol(1, "John", "Doe", 5000, 40, 20)

    def test_calculate_salary(self):
        self.robol.output = 10
        expected_salary = self.robol.salary * self.robol.output
        self.assertEqual(self.robol.calculate_salary(), expected_salary)

    def test_work(self):
        initial_energy = self.robol.energy
        initial_output = self.robol.output

        self.robol.work()
        self.assertEqual(self.robol.energy, initial_energy - 2)
        self.assertEqual(self.robol.output, initial_output + 1)

        # Test when energy is less than 0
        self.robol.energy = -1
        self.robol.work()
        self.assertEqual(self.robol.energy, 0)

if __name__ == '__main__':
    unittest.main()