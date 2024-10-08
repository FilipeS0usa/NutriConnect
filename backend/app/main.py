from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user, patient

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(patient.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to NutriConnect API"}
