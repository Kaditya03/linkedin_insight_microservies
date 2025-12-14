from fastapi import FastAPI
from app.api.page_routes import router as page_router

app = FastAPI(
    title="LinkedIn Insights Service",
    description="Service to fetch and store LinkedIn page insights",
    version="1.0.0"
)

app.include_router(page_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "LinkedIn Insights Service is running"}
