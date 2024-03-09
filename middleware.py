# import time

# from fastapi import Request

# from logger import logger

# async def ecommerce_middleware(request: Request, call_next):
#     logger.info("Starting ................")
#     start_time = time.time()
#     response = None  # Initialize response to None

#     try:
#         response = await call_next(request)
#         process_time = time.time() - start_time
#         response.headers["X-Process-Time"] = str(process_time)
#         logger.info(f"ended. process_time: {process_time}")

#     except Exception as e:
#         logger.error("An error occurred while processing")
    
#     return response

import time
from fastapi import Request
from fastapi.responses import JSONResponse
from logger import logger

async def ecommerce_middleware(request: Request, call_next):
    logger.info("Starting ................")
    start_time = time.time()
    response = None
    try:
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        logger.info(f"ended. process_time: {process_time}")
    except Exception as e:
        logger.error("An error occurred while processing")
        response = JSONResponse(status_code=500, content={"message": "Internal server error"})
    
    return response
