from functools import wraps
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import Any, AsyncGenerator, Callable, Coroutine, TypeVar
from settings import settings


engine = create_async_engine(
    f'{settings.DATABASE_DRIVER}://'
    f'{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@'
    f'{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/'
    f'{settings.DATABASE_NAME}'
)

async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


T = TypeVar('T', bound=Callable[..., Coroutine[Any, Any, Any]])


def with_session(func: T) -> T:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        session: AsyncSession = kwargs.get('session')
        if session is None:
            async with async_session_maker() as session:
                kwargs['session'] = session
                return await func(*args, **kwargs)
        else:
            return await func(*args, **kwargs)

    return wrapper
