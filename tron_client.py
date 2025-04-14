from tronpy import Tron

client = Tron()

async def get_wallet_info(address: str) -> dict:
    account = client.get_account(address)
    resource = client.get_account_resource(address)

    return {
        'balance': str(account.get('balance', 0) / 1000000),
        'energy': str(resource.get('EnergyLimit', 0)),
        'bandwidth': str(resource.get('free_net_limit', 0))
    }
