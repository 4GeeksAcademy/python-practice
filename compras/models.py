from threading import Lock

from pydantic import BaseModel, Field


class ProductoBase(BaseModel):
    nombre: str = Field(min_length=1, max_length=120, examples=["Leche"])
    cantidad: int = Field(default=1, ge=1, examples=[2])
    comprado: bool = False


class ProductoCrear(ProductoBase):
    pass


class ProductoActualizar(ProductoBase):
    pass


class Producto(ProductoBase):
    id: int


class ResultadoMySQL(BaseModel):
    query: str
    parametros: list[object]
    filas_afectadas: int


class ProductoConQuery(BaseModel):
    producto: Producto
    mysql: ResultadoMySQL


class ListaConQuery(BaseModel):
    productos: list[Producto]
    total: int
    mysql: ResultadoMySQL


class RepositorioComprasDummy:
    """Modelo de persistencia que simula las respuestas de un cliente MySQL."""

    def __init__(self) -> None:
        self._productos: dict[int, Producto] = {
            1: Producto(id=1, nombre="Pan", cantidad=1, comprado=False),
            2: Producto(id=2, nombre="Café", cantidad=2, comprado=True),
        }
        self._siguiente_id = 3
        self._lock = Lock()

    @staticmethod
    def _resultado(
        query: str, parametros: list[object], filas_afectadas: int
    ) -> ResultadoMySQL:
        return ResultadoMySQL(
            query=query,
            parametros=parametros,
            filas_afectadas=filas_afectadas,
        )

    def listar(self) -> tuple[list[Producto], ResultadoMySQL]:
        productos = list(self._productos.values())
        resultado = self._resultado(
            "SELECT id, nombre, cantidad, comprado FROM compras ORDER BY id",
            [],
            len(productos),
        )
        return productos, resultado

    def obtener(self, producto_id: int) -> tuple[Producto | None, ResultadoMySQL]:
        producto = self._productos.get(producto_id)
        resultado = self._resultado(
            "SELECT id, nombre, cantidad, comprado FROM compras WHERE id = %s",
            [producto_id],
            int(producto is not None),
        )
        return producto, resultado

    def crear(self, datos: ProductoCrear) -> tuple[Producto, ResultadoMySQL]:
        with self._lock:
            producto = Producto(id=self._siguiente_id, **datos.model_dump())
            self._productos[producto.id] = producto
            self._siguiente_id += 1

        resultado = self._resultado(
            "INSERT INTO compras (nombre, cantidad, comprado) VALUES (%s, %s, %s)",
            [datos.nombre, datos.cantidad, datos.comprado],
            1,
        )
        return producto, resultado

    def actualizar(
        self, producto_id: int, datos: ProductoActualizar
    ) -> tuple[Producto | None, ResultadoMySQL]:
        with self._lock:
            if producto_id not in self._productos:
                return None, self._resultado(
                    "UPDATE compras SET nombre = %s, cantidad = %s, comprado = %s WHERE id = %s",
                    [datos.nombre, datos.cantidad, datos.comprado, producto_id],
                    0,
                )

            producto = Producto(id=producto_id, **datos.model_dump())
            self._productos[producto_id] = producto

        resultado = self._resultado(
            "UPDATE compras SET nombre = %s, cantidad = %s, comprado = %s WHERE id = %s",
            [datos.nombre, datos.cantidad, datos.comprado, producto_id],
            1,
        )
        return producto, resultado

    def eliminar(self, producto_id: int) -> ResultadoMySQL:
        with self._lock:
            producto = self._productos.pop(producto_id, None)

        return self._resultado(
            "DELETE FROM compras WHERE id = %s",
            [producto_id],
            int(producto is not None),
        )