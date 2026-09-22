from fastapi import FastAPI

from compras.views import router


app = FastAPI(
    title="API de lista de compras",
    description="CRUD MVC con respuestas dummy de queries MySQL.",
    version="1.0.0",
)

app.include_router(router)