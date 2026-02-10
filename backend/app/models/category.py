# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from ..database import Base


# class Category(Base):
#     __tablename__ = "categories"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, nullable=False, index=True)
#     slug = Column(String, unique=True, nullable=False, index=True)

#     products = relationship("Product", back_populates="category")

#     def __repr__(self):
#         return f"<Category(id={self.id}, name='{self.name}')>"


from __future__ import annotations  # обязательно первой строкой
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from ..database import Base
from ..models.product import Product  # импорт для Pylance и runtime

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)

    products: Mapped[list[Product]] = relationship("Product", back_populates="category")

    def __repr__(self) -> str:
        return f"<Category(id={self.id}, name='{self.name}')>"