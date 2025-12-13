from fastapi import FastAPI

from app.api.page_routes import router as page_router
from app.api.post_routes import router as post_router
from app.core.database import engine
from app.models.base import Base

app = FastAPI(
    title="LinkedIn Insights Service",
    version="1.0.0"
)

# ✅ CREATE TABLES AT STARTUP
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# ✅ REGISTER ROUTES
app.include_router(page_router, prefix="/api")
app.include_router(post_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Service is running"}
