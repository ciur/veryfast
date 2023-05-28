from veryfast.database import engine
from sqlalchemy import text


def test_engine_1():
    with engine.connect() as conn:
        result = conn.execute(
            text("select 'hello world'")
        )
        first = result.all()[0]

    assert first[0] == 'hello world'


def test_engine_2():
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
            )
        conn.commit()
