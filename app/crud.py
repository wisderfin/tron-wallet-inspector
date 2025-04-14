from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc
from .models import WalletModel
from .schemas import WalletResponse
from app.database import with_session

@with_session
async def create_wallet(address: str, data: dict, session: AsyncSession) -> WalletResponse:
    wallet = WalletResponse(
        address=address,
        balance=data['balance'],
        energy=data['energy'],
        bandwith=data['bandwidth']
    )
    session.add(wallet)
    await session.commit()
    await session.refresh(wallet)
    return wallet

@with_session
async def get_wallets(skip: int = 0, limit: int = 25, session: AsyncSession = None):
    result = await session.execute(
        select(WalletModel).order_by(desc(WalletModel.timestamp)).offset(skip).limit(limit)
    )
    return result.scalars().all()
