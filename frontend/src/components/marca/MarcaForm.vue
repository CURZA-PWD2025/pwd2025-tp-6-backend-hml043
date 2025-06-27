<template>
  <form @submit.prevent="onSubmit" class="form">
    <h2>{{ isEdit.value ? 'editar Marca' : 'crear Marca' }}</h2>

    <label for="nombre">Nombre:</label><br>
    <input v-model="item.nombre" placeholder="Ingrese un nombre" type="text" class="input" required autofocus/>

    <button type="submit" class="boton">Confirmar</button>
    <button type="reset" class="boton">Limpiar</button>
    <button type="button" class="boton" @click="goBack">Cancelar</button>
  </form>
</template>

<script setup lang="ts">
import { ref, computed }  from 'vue'
import { storeToRefs }    from 'pinia'
import { useMarcaStore }  from '@/stores/marcaStore'
import { useRouter }      from 'vue-router'

const router  = useRouter();
const isEdit  = ref(false)

/****** DEBUG ******/
const item    = {id: 1, nombre: 'Marca 1'}
/****** DEBUG ******/

const onSubmit = async () => {
  alert('onSubmit')
}

const goBack = () => {  
  router.back()
}

/*
import { ref } from 'vue';
import { useMarcaStore } from '@/stores/marcaStore';

const store = useMarcaStore();
const nombre = ref('');

const onSubmit = async () => {
  await store.create({ nombre: nombre.value });
  nombre.value = '';
};
*/
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