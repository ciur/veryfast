from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from . import get_settings

settings = get_settings()

engine = create_engine(settings.database__url, echo=True)


class Base(DeclarativeBase):
    pass
