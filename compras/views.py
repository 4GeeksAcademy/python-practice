from fastapi import APIRouter, HTTPException, Response, status

from compras.controllers import ComprasController, ProductoNoEncontradoError
from compras.models import (
    ListaConQuery,
    ProductoActualizar,
    ProductoConQuery,
    ProductoCrear,
    RepositorioComprasDummy,
)


router = APIRouter()
controller = ComprasController(RepositorioComprasDummy())


def _producto_no_encontrado() -> HTTPException:
    return HTTPException(status_code=404, detail="Producto no encontrado")


@router.get("/", tags=["Estado"])
def inicio() -> dict[str, str]:
    return {
        "mensaje": "API de lista de compras disponible",
        "documentacion": "/docs",
    }


@router.get("/compras", response_model=ListaConQuery, tags=["Compras"])
def listar_compras() -> ListaConQuery:
    return controller.listar()


@router.get(
    "/compras/{producto_id}",
    response_model=ProductoConQuery,
    tags=["Compras"],
)
def obtener_compra(producto_id: int) -> ProductoConQuery:
    try:
        return controller.obtener(producto_id)
    except ProductoNoEncontradoError as error:
        raise _producto_no_encontrado() from error


@router.post(
    "/compras",
    response_model=ProductoConQuery,
    status_code=status.HTTP_201_CREATED,
    tags=["Compras"],
)
def crear_compra(datos: ProductoCrear) -> ProductoConQuery:
    return controller.crear(datos)


@router.put(
    "/compras/{producto_id}",
    response_model=ProductoConQuery,
    tags=["Compras"],
)
def actualizar_compra(
    producto_id: int, datos: ProductoActualizar
) -> ProductoConQuery:
    try:
        return controller.actualizar(producto_id, datos)
    except ProductoNoEncontradoError as error:
        raise _producto_no_encontrado() from error


@router.delete(
    "/compras/{producto_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Compras"],
)
def eliminar_compra(producto_id: int) -> Response:
    try:
        controller.eliminar(producto_id)
    except ProductoNoEncontradoError as error:
        raise _producto_no_encontrado() from error
    return Response(status_code=status.HTTP_204_NO_CONTENT)