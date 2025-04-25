from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models import Base, IntIdPk


class Category(IntIdPk, Base):
    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(String(50), unique=True, index=True)

    dishes: Mapped[list["Dish"]] = relationship(back_populates="category_obj")

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.__class__.__name__} | id=({self.id}), title=({self.title})"


class Dish(IntIdPk, Base):
    __tablename__ = "dishes"

    title: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    category: Mapped[str] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE")
    )
    description: Mapped[str | None] = mapped_column(
        Text(), default="", server_default=""
    )
    composition: Mapped[str | None] = mapped_column(
        String(150), default="", server_default=""
    )

    category_obj: Mapped["Category"] = relationship(back_populates="dishes")

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.__class__.__name__} | id=({self.id}), title=({self.title})"
