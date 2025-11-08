from fastapi import FastAPI
from routes import post_project

app = FastAPI(title="ProjetAPI - TP GitHub DevOps")

# Inclusion des routes
app.include_router(post_project.router)


@app.get("/")
def root():
    return {"message": "Bienvenue sur ProjetAPI REST- FastAPI"}


@app.get("/lint-test")
def lint_test():
    return {
        "message": "Erreurs d'indentation volontaire pour test de CI et LLM"
    }  # 👈 indentation volontairement incorrecte (3 espaces)
