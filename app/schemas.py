from pydantic import BaseModel
from datetime import datetime

class WalletCreate(BaseModel):
    address: str


class WalletResponse(BaseModel):
    address: str
    balance: str
    energy: str
    bandwidth: str
    timestamp: datetime

    class Config:
        orm_mode: True
