import uvicorn
import ssl
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.endpoints import request_item, hospital, item, search_hospitals, order, user
from src.utils.common_logger import logger
ssl._create_default_https_context = ssl._create_unverified_context

# Create API Application
app = FastAPI()


# Global error handler
@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    logger.error(base_error_message)
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}", "detail": f"{err}"})

# Add endpoints
app.include_router(request_item.router)
app.include_router(hospital.router)
app.include_router(item.router)
app.include_router(search_hospitals.router)
app.include_router(order.router)
app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
