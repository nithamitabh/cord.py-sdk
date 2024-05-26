from substrate_connection import create_connection
from balance_query import query_account_balance
from transaction import create_balance_transfer, submit_extrinsic
from substrateinterface import Keypair

def main():
    # Connect to Substrate node
    substrate = create_connection()

    # Replace with your actual addresses and amounts
    source_address = '5F3sa2TJAWMqDhXG6jhV4N8ko9n5kDEGKSF8TH2KJXPEx2M3'
    dest_address = '5EYCAe5iji3Y3Ht9qXpjQ6Dsj72qDnnQQv5kDPcXc6C3rj3F'
    transfer_amount = 1 * 10**12  # Amount in smallest unit (e.g., Planck for DOT)

    # Query balance
    query_account_balance(substrate, source_address)

    # Create balance transfer
    call = create_balance_transfer(substrate, dest_address, transfer_amount)

    # Create keypair from a known secret URI (e.g., for Alice)
    keypair = Keypair.create_from_uri('//Alice')

    # Submit the extrinsic
    submit_extrinsic(substrate, call, keypair)

if __name__ == "__main__":
    main()
