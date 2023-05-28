from pydantic import BaseSettings


class Settings(BaseSettings):
    database__url: str = "sqlite+pysqlite:///:memory:"

