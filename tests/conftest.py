import logging
import pytest

from sqlalchemy.orm import Session

from veryfast.database import Base, engine

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def setup_db_schema():
    logger.info("SETUP")
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
    logger.info("TEARDOWN")


@pytest.fixture()
def db_connection():
    with engine.begin() as conn:
        yield conn


@pytest.fixture()
def db_session():
    with Session(engine) as session:
        yield session
