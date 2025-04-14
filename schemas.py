from pydantic import BaseModel
from typing import List


class WalletCreate(BaseModel):
    address: str


class WalletResponse(BaseModel):
    id: int
    address: str
    balance: str
    energy: str
    bandwidth: str
    timestamp: str

    class Config:
        orm_mode: True
        
