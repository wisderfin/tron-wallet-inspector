from fastapi import FastAPI, Depends
from .schemas import WalletCreate
from app.tron_client import get_wallet_info
from app.crud import create_wallet, get_wallets

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
    uvicorn.run('main:app', host='0.0.0.0', port='8000', reload=True)
