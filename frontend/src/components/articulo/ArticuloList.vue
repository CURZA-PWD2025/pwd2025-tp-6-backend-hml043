<template>
  <h1 class="titulo">Lista de Articulos</h1>
  <div class="crear-container">
    <router-link :to="{name:'articulo_create'}">CREAR</router-link>
  </div>
  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>Descripcion</th>
        <th>Precio</th>
        <th>Stock</th>
        <th>Marca</th>
        <th>Proveedor</th>
        <th>acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="articulo in articulos" :key="articulo.id">
        <td>{{ articulo.id }}</td>
        <td>{{ articulo.descripcion }}</td>
        <td>{{ articulo.precio }}</td>
        <td>{{ articulo.stock }}</td>
        <td>{{ articulo.marca?.nombre || 'Sin marca' }}</td>
        <td>{{ articulo.proveedor?.nombre || 'Sin proveedor' }}</td>
        <td>
          <router-link :to="{name:'articulo_update',params:{id:articulo.id}}">editar</router-link>
          <router-link :to="{name:'articulo_show',params:{id:articulo.id}}">mostrar</router-link>
          <button @click.prevent="eliminar(articulo.id as number)">Eliminar</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue'
import useArticuloStore   from '@/stores/articuloStore'
import useMarcaStore      from '@/stores/marcaStore'
import useProveedorStore  from '@/stores/proveedoreStore'
import useCategoriaStore  from '@/stores/categoriaStore'

const { articulos } = toRefs(useArticuloStore())
const { getAll: getAllMarcas } = useMarcaStore()
const { getAll: getAllArticulos, destroy } = useArticuloStore()
const { getAll: getAllProveedores } = useProveedorStore()
const { getAll: getAllCategorias } = useCategoriaStore()


onMounted(async () => {
  await getAllArticulos()
  await getAllMarcas()
  await getAllProveedores()
  await getAllCategorias()
})

async function eliminar(id: number) {
  if (confirm('¿Estás seguro de eliminar este articulo ' + id + '?')) {
    await destroy(id)
    await getAllArticulos()
  }
}


</script>

<style scoped>
.titulo {
  text-align: center;
  margin-top: 1rem;
}
.crear-container {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}
th, td {

  padding: 0.5rem;
  text-align: left;
  vertical-align: middle;
}
th {
  background: #f5f5f5;
}
/* Aplica flex solo a la celda de acciones */
td:last-child {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}
</style>
