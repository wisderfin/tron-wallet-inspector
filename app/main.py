from fastapi import FastAPI
from schemas import WalletCreate
from tron_client import get_wallet_info
from crud import create_wallet, get_wallets
from settings import settings

app = FastAPI()

@app.post('/')
async def create(wallet: WalletCreate):
    info = await get_wallet_info(wallet.address)
    return await create_wallet(address=wallet.address, data=info)


@app.get('/')
async def get(skip: int = 0, limit: int = 25):
    return await get_wallets(skip, limit)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host=settings.API_HOST, port=settings.API_PORT, reload=True)
