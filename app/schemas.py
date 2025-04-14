from pydantic import BaseModel


class WalletCreate(BaseModel):
    address: str


class WalletResponse(BaseModel):
    address: str
    balance: str
    energy: str
    bandwidth: str
    timestamp: str

    class Config:
        orm_mode: True
