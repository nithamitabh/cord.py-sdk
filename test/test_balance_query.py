import unittest
from src.substrate_connection import create_connection
from src.balance_query import query_account_balance

class TestBalanceQuery(unittest.TestCase):
    def setUp(self):
        self.substrate = create_connection()
        self.address = '5F3sa2TJAWMqDhXG6jhV4N8ko9n5kDEGKSF8TH2KJXPEx2M3'

    def test_query_account_balance(self):
        balance = query_account_balance(self.substrate, self.address)
        self.assertIsNotNone(balance)

if __name__ == '__main__':
    unittest.main()
