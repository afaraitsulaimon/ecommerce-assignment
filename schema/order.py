from typing import Union
from pydantic import BaseModel
from schema.customer import Customer
from enum import Enum

from schema.product import Product

class OrderStatus(Enum):
    completed = "COMPLETED"
    pending = "PENDING"

class Order(BaseModel):
    id: int
    customer_id: Union[int, Customer]
    items: list[int]
    status: str = OrderStatus.pending.value

class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]

class checkOutCreate(BaseModel):
    order_status: str

orders = [
    Order(id=1, customer_id=1, items=[1, 2]),
    Order(id=2, customer_id=1, items=[2, 3])
]