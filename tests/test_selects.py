import logging
from sqlalchemy import insert, select

from veryfast.models import User


logger = logging.getLogger(__name__)


def test_select1(db_connection, db_session):
    statement = insert(User)

    logger.info(f"Performing now {statement}")

    db_connection.execute(
        statement,
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patric", "fullname": "Patrick Star"}
        ]
    )

    user = db_session.scalar(
        select(User).where(User.name == "sandy")
    )

    assert user.name == "sandy"

