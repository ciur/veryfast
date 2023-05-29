import datetime

from typing import List, Optional

from sqlalchemy import String, ForeignKey, Column, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .database import Base


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return " ".join([
            f"User(id={self.id!r}, name={self.name!r},",
            "fullname={self.fullname!r})"
        ])


class Address:
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


class CoreUser(Base):
    __tablename__ = "core_user"

    id: Mapped[str] = mapped_column(
        String(32),
        primary_key=True,
        index=True
    )
    username: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(128), default='')
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    first_name: Mapped[str] = mapped_column(String(150), default='')
    last_name: Mapped[str] = mapped_column(String(150), default='')
    home_folder = relationship(
        "Node",
        primaryjoin="and_(User.id==Node.user_id, "
        " Node.title=='.home')",
        uselist=False,
        viewonly = True,
    )
    inbox_folder = relationship(
        "Node",
        primaryjoin="and_(User.id==Node.user_id, "
        " Node.title=='.inbox')",
        viewonly=True,
        uselist=False
    )
    date_joined: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )


class Node(Base):
    __tablename__ = "core_basetreenode"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), primary_key=True, index=True)
    lang: Mapped[str] = mapped_column(String(8), default='deu')
    ctype: Mapped[str] = mapped_column(String(16), default='folder')
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )
    user_id: Mapped["User"] = mapped_column(
        String(32),
        ForeignKey("core_user.id")
    )
    user = relationship("User", foreign_keys=[user_id])
    parent_id = mapped_column(
        "parent_id",
        String(32),
        ForeignKey("core_basetreenode.id")
    )


class Folder(Base):
    __tablename__ = "core_folder"

    column_not_exist_in_db = Column(Integer, primary_key=True)
    basetreenode_ptr_id: Mapped["Node"] = mapped_column(
        String(32),
        ForeignKey("core_basetreenode.id")
    )
    basetreenode_ptr = relationship("Node", foreign_keys=[basetreenode_ptr_id])
