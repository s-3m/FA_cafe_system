from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import mapped_column, Mapped

from src.models import Base, IntIdPk


class Category(IntIdPk, Base):
    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(String(50), unique=True, index=True)

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.__class__.__name__} | id=({self.id}), title=({self.title})"


# class Dish(Base):
#
#     title: Mapped[str] = mapped_column(String(50), unique=True, index=True)
#     category: Mapped[str] = mapped_column(ForeignKey("categorys.id"))
#     description: Mapped[str] = mapped_column(Text(500))
#     composition: Mapped[str] = mapped_column(String(150))
#
#     categories:
#
#     def __str__(self):
#         return f"{self.title}"
#
#     def __repr__(self):
#         return f"{self.__class__.__name__} | id=({self.id}), title=({self.title})"
