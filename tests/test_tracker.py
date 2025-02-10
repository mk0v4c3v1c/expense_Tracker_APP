import unittest
from services.tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_transaction(self):
        self.tracker.add_transaction(500, "Food", "Lunch")
        self.assertEqual(len(self.tracker.transactions), 1)

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            self.tracker.add_transaction(100, "Wrong food", "Test")

if __name__ == "__main__":
    unittest.main()