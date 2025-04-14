from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, func
from datetime import datetime

class Base(DeclarativeBase):
    pass

class WalletModel(Base):
    __tablename__ = 'wallets'

    address: Mapped[str] = mapped_column(String, index=True, primary_key=True)
    balance: Mapped[str] = mapped_column(String)
    energy: Mapped[str] = mapped_column(String)
    bandwidth: Mapped[str] = mapped_column(String)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
