import unittest
from classes.Menago import Menago
from classes.Robol import Robol
from classes.Worker import Worker

class TestMenago(unittest.TestCase):

    def setUp(self):
        self.worker1 = Robol(1, "John", "Doe", 3000)
        self.worker1.output = 10
        self.worker2 = Robol(2, "Jane", "Doe", 3500)
        self.worker2.output = 15
        self.menago = Menago(3, "Manager", "Smith", 5000, [self.worker1, self.worker2], 5)

    def test_calculate_salary(self):
        expected_output = (self.worker1.output + self.worker2.output) * self.menago.salary
        self.assertEqual(self.menago.calculate_salary(), expected_output)

    def test_work(self):
        initial_energy = self.menago.energy
        initial_output = self.menago.output
        self.menago.work()
        self.assertEqual(self.menago.energy, initial_energy - 3)
        self.assertEqual(self.menago.output, initial_output + 1)

    def test_rest(self):
        initial_energy = self.menago.energy
        self.menago.rest()
        self.assertEqual(self.menago.energy, initial_energy + 1)

    def test_add_worker(self):
        new_worker = Robol(4, "New", "Worker", 4000)
        self.assertTrue(self.menago.add_worker(new_worker))
        self.assertIn(new_worker, self.menago.workers)

        # Test adding worker when team is full
        self.menago.team_size = 2
        self.assertFalse(self.menago.add_worker(new_worker))

    def test_remove_worker(self):
        self.assertTrue(self.menago.remove_worker(self.worker1))
        self.assertNotIn(self.worker1, self.menago.workers)

        # Test removing worker not in team
        self.assertFalse(self.menago.remove_worker(self.worker1))

if __name__ == '__main__':
    unittest.main()