import { type Categoria }   from "./categoria"
import { type Marca }       from "./marca"
import { type Proveedor }   from "./proveedor"

export interface Articulo {
    id?: number;
    descripcion: string;
    precio: float;
    stock: number;
    marca_id: number;
    proveedor_id: number;
    marca?: Marca;
    proveedor?: Proveedor;
    categorias?: Categoria[];
}
