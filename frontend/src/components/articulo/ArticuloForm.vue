<template>
  <form @submit.prevent="onSubmit" class="form">
    <h2>{{ isEdit.value ? 'editar Artículo' : 'crear Artículo' }}</h2>

    <label for="descripcion">Descripcion:</label><br>
    <input v-model="item.descripcion" placeholder="Ingrese una descripción" class="input" type="text"required autofocus/><br>

    <label for="precio">Precio:</label><br>
    <input v-model="item.precio" placeholder="Indique el precio" class="input" type="number" min="0"/><br>

    <label for="stock">Stock:</label><br>
    <input v-model="item.stock" placeholder="Ingrese el stock disponible" class="input" type="number" min="0"/><br>

    <label for="marca">Marcas:</label><br>
    <select v-model.number="item.marca_id" class="input" min="0">
      <option disabled value="0">Seleccione Marca</option>
      <option v-for="m in marcas" :key="m.id" :value="m.id">{{ m.nombre }}</option>
    </select><br>

	<label for="proveedor">Proveedores:</label><br>
    <select v-model.number="item.proveedor_id" class="input">
      <option disabled value="0">Seleccione Proveedor</option>
      <option v-for="p in proveedores" :key="p.id" :value="p.id">{{ p.nombre }}</option>
    </select><br>

    <label for="categoria">Categorias: (ctrl + clic = mas de 1)</label><br>
    <select v-model="item.categorias" multiple>
    	<option disabled value="0">Seleccione Categoria(s)</option>
    	<option v-for="c in categorias" :key="c.id" :value="c.id">{{ c.nombre }}</option>
    </select><br>  	

    <button type="submit" class="boton">Confirmar</button>
    <button type="reset" class="boton">Limpiar</button>
    <button type="button" class="boton" @click="goBack">Cancelar</button>
  </form>
</template>

<script setup lang="ts">
import { ref, computed }  	from 'vue'
import { storeToRefs }    	from 'pinia'
import { useArticuloStore } from '@/stores/articuloStore'
import { useRouter } 		from 'vue-router'

const router = useRouter();
const isEdit = ref(false)

/****** DEBUG ******/
const item = {id: 101, descripcion: 'Teclado Mecánico RGB', precio: 125000.00, stock: 13, marca_id: 2, proveedor_id: 1, categorias: []}

const marcas 		= [{id: 1, nombre: 'Marca 1'}, {id: 2, nombre: 'Marca 2'}]
const proveedores 	= [{id: 1, nombre: 'Proveedor 1'}, {id: 2, nombre: 'Proveedor 2'}]
const categorias 	= [{id: 1, nombre: 'Categoria 1'}, {id: 2, nombre: 'Categoria 2'}]
/****** DEBUG ******/

const onSubmit = async () => {
	alert('onSubmit')
}

const goBack = () => {
  router.back()
}
</script>

<style scoped>
.form {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1.5rem;
  background-color: #f7fafc;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  color: #000; 
}

.form h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #333;
}

.input, select {
  width: 100%;
  padding: 0.6rem;
  margin-bottom: 1rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  color: #000;
}

.boton {
  background-color: #d7d9db;
  color: #222;
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  margin-right: 10px;
}

.boton:hover {
  background-color: #f3f582;
 }
</style>