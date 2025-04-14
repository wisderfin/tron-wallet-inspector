import pytest
from crud import create_wallet


@pytest.mark.asyncio
async def test_create_wallet():
    data = {'balance': '100', 'energy': '2000', 'bandwidth': '500'}
    wallet = await create_wallet('TEST_ADDRESS', data)

    assert wallet.address == 'TEST_ADDRESS'
    assert wallet.balance == '100'
    assert wallet.energy == '2000'
    assert wallet.bandwidth == '500'
