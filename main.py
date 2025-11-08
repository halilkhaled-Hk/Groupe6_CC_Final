from fastapi import FastAPI
from routes import post_project

app = FastAPI(title="ProjetAPI - TP GitHub DevOpss")

# Inclusion des routes
app.include_router(post_project.router)
app.include_router(get_projects.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur ProjetAPI - FastAPI"}


@app.get("/lint-test")
def lint_test():
   return {"message": "Erreur d'indentation volontaire pour test de CI et LLM"}  # 👈 indentation volontairement incorrecte (3 espaces)
