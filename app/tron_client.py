from tronpy import Tron, providers
from settings import settings


provider = providers.HTTPProvider(
    api_key=settings.TRONGRID_API_KEY
)
client = Tron(provider=provider)


async def get_wallet_info(address: str) -> dict:
    account = client.get_account(address)
    resource = client.get_account_resource(address)

    return {
        'balance': f'{float(account.get("balance", 0)) / 1000000:.10f}',
        'energy': str(resource.get('TotalEnergyLimit', 0) - resource.get('TotalEnergyWeight', 0)),
        'bandwidth': str(resource.get('freeNetLimit', 0) - resource.get('freeNetUsed', 0))
    }
