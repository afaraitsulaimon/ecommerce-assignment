from fastapi import APIRouter, HTTPException

from schema.product import Product, ProductCreate, products

product_router = APIRouter()

# create product
# list all products

@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
    # get the product id
    product_id = len(products) + 1
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_available=payload.quantity_available
    )
    products[product_id] = new_product
    return {'message': 'Product created successfully', 'data': new_product}

@product_router.get('/', status_code=200)
def list_products():
    return {'message': 'success', 'data': products}

@product_router.put('/{product_id}', status_code=200)
def edit_product(product_id: int, payload: ProductCreate):
    current_product = None

    #get the products and loop through it
    #then check if the product id is equal to the present
    #one is looping through 
    #then update it or throw exception when not the product
#     products.items() returns a view object that displays a list of key-value pairs in the dictionary.
# key corresponds to the key (product ID) in the dictionary.
# product corresponds to the value (product object) in the dictionary.
# We check if product.id is equal to 3. If it is, we print a message and break out of the loop.
# If the loop completes without finding a product with ID 3, we print a message indicating that the product was not found.
    for key, product in products.items():
        print(product.id)
        if product.id == product_id:
            current_product = product
            break

    if not current_product:
        raise HTTPException(status_code=404, detail="Product not found")

    current_product.name = payload.name
    current_product.price = payload.price
    current_product.quantity_available = payload.quantity_available

    return {'message': 'Product edited Successfully', 'data':current_product}
    