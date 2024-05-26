def create_balance_transfer(substrate, dest_address, amount):
    call = substrate.compose_call(
        call_module='Balances',
        call_function='transfer',
        call_params={
            'dest': dest_address,
            'value': amount
        }
    )
    return call

def submit_extrinsic(substrate, call, keypair):
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    try:
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Extrinsic '{receipt.extrinsic_hash}' sent and included in block '{receipt.block_hash}'")
        return receipt
    except Exception as e:
        print(f"Failed to send extrinsic: {e}")
        return None
