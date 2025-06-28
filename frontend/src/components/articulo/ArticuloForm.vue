<template>
  <form @submit.prevent="onSubmit" class="form">
    <h2>{{ store.esEditar ? 'editar Artículo' : 'crear Artículo' }}</h2>

    <label for="descripcion">Descripcion:</label><br>
    <input v-model="store.item.descripcion" placeholder="Ingrese una descripción" class="input" type="text"required autofocus/><br>

    <label for="precio">Precio:</label><br>
    <input v-model="store.item.precio" placeholder="Indique el precio" class="input" type="number" min="0"/><br>

    <label for="stock">Stock:</label><br>
    <input v-model="store.item.stock" placeholder="Ingrese el stock disponible" class="input" type="number" min="0"/><br>

    <label for="marca">Marcas:</label><br>
    <select v-model.number="store.item.marca_id" class="input" min="0">
      <option disabled value="0">Seleccione Marca</option>
      <option v-for="x in storeM.items" :key="x.id" :value="x.id">{{ x.nombre }}</option>
    </select><br>

	<label for="proveedor">Proveedores:</label><br>
    <select v-model.number="store.item.proveedor_id" class="input">
      <option disabled value="0">Seleccione Proveedor</option>
      <option v-for="x in storeP.items" :key="x.id" :value="x.id">{{ x.nombre }}</option>
    </select><br>

    <label for="categoria">Categorias: (ctrl + clic = mas de 1)</label><br>
    <select v-model="store.item.categorias" multiple>
    	<option disabled value="0">Seleccione Categoria(s)</option>
    	<option v-for="x in storeC.items" :key="x.id" :value="x.id">{{ x.nombre }}</option>
    </select><br>  	

    <button type="submit" class="boton">Confirmar</button>
    <button type="reset" class="boton">Limpiar</button>
    <button type="button" class="boton" @click="goBack">Cancelar</button>
  </form>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { storeToRefs }    	from 'pinia'
import { useRouter } 		    from 'vue-router'
import { useArticuloStore } from '@/stores/articuloStore'

import { useMarcaStore }      from '@/stores/marcaStore';
import { useProveedorStore }  from '@/stores/proveedorStore'
import { useCategoriaStore }  from '@/stores/categoriaStore';

const router  = useRouter();
const store   = useArticuloStore()
const { items, item, esEditar, idEditar } = storeToRefs(store)
const { addItem, updItem }                = store

const storeM   = useMarcaStore()
const storeP   = useProveedorStore()
const storeC   = useCategoriaStore()
/*
const { getItemAll }  = storeM
const { getItemAll }  = storeP
const { getItemAll }  = storeC
*/

if (store.esEditar) {
  store.item = store.items.find(x => x.id === store.idEditar); }
else {
  store.item = {id: 0, descripcion: '', precio: 0, stock: 0, marca_id: 0, proveedor_id: 0, categorias: []}; } //{ ...store.item };

const onSubmit = async () => {
  console.log('articulo :', store.idEditar, store.item)
  if (!confirm('Confirme por favor')) return;
  try {
    if (store.esEditar) {
      store.updItem(store.idEditar, store.item); }
    else {
      store.addItem(store.item); }    
  }
  catch (error) { alert('Error: ', error.message); }  
  finally { goBack() }
}

const goBack = () => {  
  router.back()
}

onMounted(() => {
  storeM.getItemAll();
  storeP.getItemAll();
  storeC.getItemAll();
});
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