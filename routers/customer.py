from fastapi import APIRouter, HTTPException, Depends

from schema.customer import Customer, CustomerCreate, customers
from typing import Annotated

customer_router = APIRouter()

# Create customer 
# List customer
# edit customer

# dependency to check user when registering
#we pass in the class CustomerCreate, which is for creating users
#ther we check if the customer creating is available inside the below, customer.py
#that is list of the Customer class data type,that is holding the data

# customers: list[Customer] = [
#     Customer(id=1, username="damilare", address="3, olusola str"),
#     Customer(id=2, username="sweetboy", address="23, johnson str")
# ]
#if found raise an Exception
#if not found then, create user
def checkUserName(payload: CustomerCreate):
            # get the customer
    for customer in customers:
        if customer.username == payload.username:
            raise HTTPException(status_code=400, detail="Username Already exists")
            
        return True
    
# create customer
@customer_router.post('/', status_code=201)
def create_customer(payload: CustomerCreate, is_unique: bool = Depends(checkUserName)):
    customer_id = len(customers) + 1
    new_customer = Customer(
        id=customer_id, 
        username=payload.username, 
        address=payload.address
    )
    customers.append(new_customer)
    return {'message': 'customer created successfully', 'data': new_customer}

@customer_router.get('/', status_code=200)
def list_customers():
    return {'message': 'success', 'data': customers}

@customer_router.put('/{customer_id}', status_code=200)
def edit_customer(customer_id: int, payload: CustomerCreate):
    curr_customer = None
    # get the customer
    for customer in customers:
        if customer.id == customer_id:
            curr_customer = customer
            break

    if not curr_customer:
        raise HTTPException(status_code=404, detail="customer not found")
    curr_customer.username = payload.username
    curr_customer.address = payload.address
    return {'message': 'customer edited successfully', 'data': curr_customer}
