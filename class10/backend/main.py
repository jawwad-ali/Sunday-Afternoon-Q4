from fastapi import FastAPI
from fastapi import Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, SQLModel, create_engine, Session
from typing import Optional, Generator
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    """Create the database and tables."""
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Get database session"""
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# SQL MODEL CLASS


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    in_stock: bool


class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


products_db = [
    {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
    {"id": 2, "name": "Smartphone", "price": 499.99, "in_stock": False},
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
async def read_root():
    return products_db


"""
Legacy in-memory create endpoint (kept for reference).
Commented out to avoid duplicate route definitions.
Beginner note: this version appends to a Python list only,
so data disappears when the server restarts.
"""
# @app.post("/products")
# async def create_products(product: Product):
#     print(type(product))
#     products_db.append(product.dict())
#     return {"message": "Products created successfully (in-memory)."}

@app.post("/products")
def create_product(product: Product, session: Session = Depends(get_session)):
    # Beginner-friendly: insert into DB using SQLModel session
    # Ensure id is None so DB can auto-generate if configured
    product.id = None
    session.add(product)
    session.commit()  # write changes
    session.refresh(product)  # get auto-generated fields like id
    return {"message": "Product created successfully.", "product": product}

    

    return {"message": "Products created successfully."}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    global products_db
    new_products = []
    for product in products_db:
        if product["id"] != product_id:
            new_products.append(product)
    products_db = new_products
    return {"message": "Product deleted successfully."}

@app.put("/products/{product_id}")
async def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products_db):
        if product["id"] == product_id:
            products_db[index] = updated_product.dict()
            return {"message": f"{updated_product.name} updated successfully."}
    return {"message": "Product not found."}

if __name__ == "__main__":
    main()
