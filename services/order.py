from fastapi import HTTPException

from schema.product import Product, products
from schema.order import Order, OrderCreate, orders

from logger import logger

class OrderService:

    @staticmethod
    def order_parser(orders: list[Order]):

        for order in orders:
            order_items = order.items
            new_order = []
            for product_id in order_items:
                product = products.get(product_id)
                new_order.append(product)
            order.items = new_order
        return orders
    
    @staticmethod
    def check_availability(payload: OrderCreate):
        product_ids = payload.items
        for product_id in product_ids:
            product: Product = products.get(int(product_id))
            if product.quantity_available < 1:
                logger.warning("Product is no more available")
                raise HTTPException(status_code=400, detail='Product is unavailable')
            product.quantity_available -= 1
        return payload
    
    @staticmethod
    def check_availability(payload: OrderCreate):
        product_ids = payload.items
        for product_id in product_ids:
            product: Product = products.get(int(product_id))
            if product.quantity_available < 1:
                raise HTTPException(status_code=400, detail='Product is unavailable')
            product.quantity_available -= 1
        return payload

   #dependency for checking if order status is pending  
    @staticmethod
    def checkCheckoutAvailable(orderStatus: str):
        if orderStatus != "pending":
            raise HTTPException(status_code=403, detail="Order Not pending")
        return {orderStatus}
            
        
    @staticmethod
    def does_order_exist(order_id: int):
        order_set = set()
        for order in orders:
            order_set.add(order.id)
        if order.id not in order_set:
            raise HTTPException(status_code=404, detail="order does not exist")
        return order_id
            
    
order_service = OrderService()