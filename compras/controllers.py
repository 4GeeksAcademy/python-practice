from compras.models import (
    ListaConQuery,
    ProductoActualizar,
    ProductoConQuery,
    ProductoCrear,
    RepositorioComprasDummy,
)


class ProductoNoEncontradoError(Exception):
    pass


class ComprasController:
    def __init__(self, repositorio: RepositorioComprasDummy) -> None:
        self._repositorio = repositorio

    def listar(self) -> ListaConQuery:
        productos, resultado = self._repositorio.listar()
        return ListaConQuery(
            productos=productos,
            total=len(productos),
            mysql=resultado,
        )

    def obtener(self, producto_id: int) -> ProductoConQuery:
        producto, resultado = self._repositorio.obtener(producto_id)
        if producto is None:
            raise ProductoNoEncontradoError
        return ProductoConQuery(producto=producto, mysql=resultado)

    def crear(self, datos: ProductoCrear) -> ProductoConQuery:
        producto, resultado = self._repositorio.crear(datos)
        return ProductoConQuery(producto=producto, mysql=resultado)

    def actualizar(
        self, producto_id: int, datos: ProductoActualizar
    ) -> ProductoConQuery:
        producto, resultado = self._repositorio.actualizar(producto_id, datos)
        if producto is None:
            raise ProductoNoEncontradoError
        return ProductoConQuery(producto=producto, mysql=resultado)

    def eliminar(self, producto_id: int) -> None:
        resultado = self._repositorio.eliminar(producto_id)
        if resultado.filas_afectadas == 0:
            raise ProductoNoEncontradoError