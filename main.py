from fastapi import FastAPI, Response
from routes import post_project, get_projects, get_project_by_id, put_projects_id_grade, get_projects_by_course, delete_project

app = FastAPI(title="ProjetAPI - TP GitHub DevOps")

# Inclusion des routes
app.include_router(post_project.router)
app.include_router(get_projects.router)
app.include_router(get_project_by_id.router)
app.include_router(put_projects_id_grade.router)
app.include_router(get_projects_by_course.router)
app.include_router(delete_project.router)



@app.get("/", response_class=Response)
def root():
    html_content = """
    <html>
        <head>
            <title>🚀 ProjetAPI - FastAPI</title>
            <style>
                body {
                    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                    color: white;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    text-align: center;
                }
                h1 {
                    color: #00e676;
                    font-size: 2.8em;
                    margin-bottom: 0.3em;
                    animation: fadeInDown 1s ease-out;
                }
                p {
                    color: #e0e0e0;
                    font-size: 1.2em;
                    animation: fadeInUp 1.2s ease-out;
                }
                .btn {
                    background-color: #00e676;
                    color: #0f2027;
                    padding: 12px 24px;
                    border-radius: 25px;
                    font-weight: bold;
                    text-decoration: none;
                    margin-top: 25px;
                    transition: all 0.3s ease;
                }
                .btn:hover {
                    background-color: #1de9b6;
                    transform: scale(1.05);
                }
                @keyframes fadeInDown {
                    from { opacity: 0; transform: translateY(-20px); }
                    to { opacity: 1; transform: translateY(0); }
                }
                @keyframes fadeInUp {
                    from { opacity: 0; transform: translateY(20px); }
                    to { opacity: 1; transform: translateY(0); }
                }
            </style>
        </head>
        <body>
            <h1>🌍 Bienvenue sur ProjetAPI - FastAPI</h1>
            <p>Une API REST moderne construite avec <strong>FastAPI</strong> et intégrée à GitHub CI/CD 🚀</p>
            <a href="/docs" class="btn">Accéder à la Documentation</a>
        </body>
    </html>
    """
    return Response(content=html_content, media_type="text/html")


@app.get("/lint-test")
def lint_test():
    return {
        "message": "Erreurs d'indentation volontaire pour test de CI et LLM"
    }