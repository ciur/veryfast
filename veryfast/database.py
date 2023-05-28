from sqlalchemy import create_engine

from . import get_settings

settings = get_settings()

engine = create_engine(settings.database__url, echo=True)
