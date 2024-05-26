import unittest
from src.substrate_connection import create_connection
from src.transaction import create_balance_transfer, submit_extrinsic
from substrateinterface import Keypair

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.substrate = create_connection()
        self.dest_address = '5EYCAe5iji3Y3Ht9qXpjQ6Dsj72qDnnQQv5kDPcXc6C3rj3F'
        self.transfer_amount = 1 * 10**12  # Amount in smallest unit (e.g., Planck for DOT)
        self.keypair = Keypair.create_from_uri('//Alice')

    def test_create_balance_transfer(self):
        call = create_balance_transfer(self.substrate, self.dest_address, self.transfer_amount)
        self.assertIsNotNone(call)

    def test_submit_extrinsic(self):
        call = create_balance_transfer(self.substrate, self.dest_address, self.transfer_amount)
        receipt = submit_extrinsic(self.substrate, call, self.keypair)
        self.assertIsNotNone(receipt)

if __name__ == '__main__':
    unittest.main()
