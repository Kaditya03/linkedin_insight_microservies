from fastapi import FastAPI
from app.api.page_routes import router as page_router
from app.api.post_routes import router as post_router

app = FastAPI(
    title="LinkedIn Insights Service",
    version="1.0.0"
)

app.include_router(page_router, prefix="/api")
app.include_router(post_router, prefix="/api")  # ✅ THIS LINE IS REQUIRED

@app.get("/")
async def root():
    return {"message": "Service is running"}
