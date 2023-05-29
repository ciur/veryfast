import logging
from sqlalchemy import insert, select

from veryfast.models import User


logger = logging.getLogger(__name__)


def test_insert1(db_connection):
    statement = insert(User)

    logger.info(f"Performing now {statement}")

    db_connection.execute(
        statement,
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patric", "fullname": "Patrick Star"}
        ]
    )

    user_table = User.__table__
    statement = select(user_table).where(user_table.c.name == "spongebob")
    logger.info(f"Performing now {statement}")
    db_connection.execute(statement)
