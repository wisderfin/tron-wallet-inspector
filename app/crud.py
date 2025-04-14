from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc
from models import WalletModel
from schemas import WalletResponse
from database import with_session


@with_session
async def create_wallet(address: str, data: dict, session: AsyncSession) -> WalletModel:
    stmt = select(WalletModel).where(WalletModel.address == address)
    result = await session.execute(stmt)
    wallet = result.scalar_one_or_none()

    if wallet:
        wallet.balance = data['balance']
        wallet.energy = data['energy']
        wallet.bandwidth = data['bandwidth']
    else:
        wallet = WalletModel(
            address=address,
            balance=data['balance'],
            energy=data['energy'],
            bandwidth=data['bandwidth']
        )
        session.add(wallet)

    await session.commit()
    await session.refresh(wallet)
    return wallet


@with_session
async def get_wallets(skip: int = 0, limit: int = 25, session: AsyncSession = None) -> list[WalletModel]:
    result = await session.execute(
        select(WalletModel).order_by(desc(WalletModel.timestamp)).offset(skip).limit(limit)
    )
    return result.scalars().all()
