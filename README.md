# API de lista de compras

Mini API MVC desarrollada con FastAPI. Los datos se guardan en memoria y
el repositorio devuelve información dummy de las queries que se ejecutarían en
MySQL, por lo que no necesita un servidor de base de datos.

## Arquitectura

```text
fast.py                 Punto de entrada de FastAPI
compras/
├── models.py           Modelos Pydantic y persistencia MySQL dummy
├── controllers.py      Lógica y casos de uso de compras
└── views.py            Interfaz HTTP y rutas de FastAPI
```

## Ejecutar

```bash
pipenv install
pipenv run uvicorn fast:app --reload
```

La documentación interactiva estará disponible en <http://127.0.0.1:8000/docs>.

## Endpoints

| Método | Ruta | Acción |
| --- | --- | --- |
| `GET` | `/compras` | Listar productos |
| `GET` | `/compras/{id}` | Consultar un producto |
| `POST` | `/compras` | Agregar un producto |
| `PUT` | `/compras/{id}` | Reemplazar un producto |
| `DELETE` | `/compras/{id}` | Eliminar un producto |

Ejemplo para crear un producto:

```bash
curl -X POST http://127.0.0.1:8000/compras \
	-H 'Content-Type: application/json' \
	-d '{"nombre":"Leche","cantidad":2,"comprado":false}'
```