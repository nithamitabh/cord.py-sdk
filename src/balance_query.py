def query_account_balance(substrate, address):
    result = substrate.query('System', 'Account', [address])
    free_balance = result.value['data']['free']
    print(f"Account balance for {address}: {free_balance}")
    return free_balance
