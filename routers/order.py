from fastapi import APIRouter, Depends , HTTPException

from typing import Annotated

from schema.order import Order, OrderCreate, orders, checkOutCreate, OrderStatus
from services.order import order_service

order_router = APIRouter()

# list all order
# create an order 

@order_router.get('/', status_code=200)
def list_orders():
    response = order_service.order_parser(orders)
    return {'message': 'success', 'data': response}

@order_router.post('/', status_code=201)
def create_order(payload: OrderCreate = Depends(order_service.check_availability)):
    customer_id: int = payload.customer_id
    product_ids: list[int] = payload.items

    # get curr order id
    order_id = len(orders) + 1

    new_order = Order(
        id=order_id,
        customer_id=customer_id,
        items=product_ids,
        order_status="pending"  # Update order_status to completed
    )
    orders.append(new_order)

    return {'message': 'Order created successfully', 'data': new_order}

# to checkout and change the status from pending to completed
#to checkout order, you have to place order
#to place order , you have to check if the order is available
#if the order is available, you can add to the order to order create
#then place the order and update the order status to completed

# @order_router.post("/{order_id}", status_code=200)
# def checkoutOrder(order_id:int, ):

# @order_router.put("/{order_id}")
# def checkOutOrder(order_id: int, payload: checkOutCreate = Depends(order_service.checkCheckoutAvailable)):
#     current_order = None
#     for key, order in orders.items():
        
#         if order.id == order_id:
#             current_order = order
#             break
    
#     if not current_order:
#         raise HTTPException(status_code=404, detail="order not found")

#     current_order.order_status = payload.order_status
   

#     return {'message': 'Product edited Successfully', 'data':current_order}


@order_router.put('/process_order/{order_id}', status_code=201)
def process_order(order_id: int = Depends(order_service.does_order_exist)):
    for order in orders:
        if order.id == order_id:
            order.status = OrderStatus.completed.value
            return {'message':'Order completed successfully', 'data' : order}
            
        
    