from fastapi import FastAPI
from routes import post_project
from routes import Get_Project
app = FastAPI(title="ProjetAPI - TP GitHub DevOps")

# Inclusion des routes
app.include_router(post_project.router)


@app.get("/")
def root():
    return {"message": "Bienvenue sur ProjetAPI - FastAPI"}
