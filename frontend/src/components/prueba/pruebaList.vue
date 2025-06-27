<template>
  <div class="articulos-page">
    <h1>Gestión de Articulos</h1>

    <div class="form-container">
      <h3>{{ isEditing ? 'Editar Articulo' : 'Añadir Nuevo Articulo' }}</h3>
      <form @submit.prevent="handleSubmit">
        <input type="text" placeholder="Nombre del articuloo" v-model="form.descripcion" required>
        <input type="number" placeholder="Precio" v-model.number="form.precio" required>
        <button type="submit" :disabled="articuloStore.loading">
          {{ articuloStore.loading ? 'Guardando...' : (isEditing ? 'Actualizar' : 'Añadir') }}
        </button>
        <button type="button" v-if="isEditing" @click="cancelEdit">Cancelar</button>
      </form>
    </div>

    <div v-if="articuloStore.loading" class="loading">Cargando articulos...</div>
    <div v-if="articuloStore.error" class="error">{{ articuloStore.error }}</div>

    <ul class="articulo-list">
      <li v-for="articulo in useArticuloStore.articulos" :key="articulo.id">
        <span>{{ articulo.descripcion }} - ${{ articulo.precio }}</span>
        <div class="actions">
          <button @click="startEdit(articulo)">Editar</button>
          <button @click="handleDelete(articulo.id)" :disabled="articuloStore.loading">Eliminar</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted, ref }   from 'vue';
import { useArticuloStore } from '../stores/articuloStore';

// 1. Instanciamos el store para tener acceso a su estado y acciones.
const articuloStore = useArticuloStore();

// 2. Estado local del componente para manejar el formulario.
const isEditing = ref(false);
const form = ref({
  id: null,
  descripcion: '',
  precio: '',
});

// 3. Cuando el componente se monta, llamamos a la acción para cargar los articulos.
onMounted(() => {
  articuloStore.getItemAll();
});

// 4. Lógica para manejar el envío del formulario.
const handleSubmit = async () => {
  if (isEditing.value) {
    // Si estamos editando, llamamos a la acción de actualizar.
    await articuloStore.updItem({ ...form.value });
  } else {
    // Si no, llamamos a la acción de añadir.
    const { id, ...newArticuloData } = form.value; // Excluimos el ID nulo
    await articuloStore.addItem(newArticuloData);
  }
  // Limpiamos el formulario después de la operación
  resetForm();
};

// 5. Lógica para eliminar un articulo.
const handleDelete = (id) => {
  if (confirm('¿Estás seguro de que quieres eliminar este articuloo?')) {
    articuloStore.delItem(id);
  }
};

// 6. Funciones auxiliares para el modo de edición.
const startEdit = (articulo) => {
  isEditing.value = true;
  form.value = { ...articulo }; // Copiamos los datos del articulo al formulario
};

const cancelEdit = () => {
  isEditing.value = false;
  resetForm();
};

const resetForm = () => {
  form.value = { id: null, descripcion: '', precio: '' };
  isEditing.value = false;
};
</script>

<style scoped>
/* Estilos para una mejor presentación */
.articulos-page {
  font-family: sans-serif;
  padding: 20px;
}
.form-container {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
}
.form-container form {
  display: flex;
  gap: 10px;
}
.articulo-list {
  list-style: none;
  padding: 0;
}
.articulo-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ccc;
}
.actions button {
  margin-left: 10px;
}
.loading, .error {
  text-align: center;
  padding: 10px;
  margin-bottom: 20px;
  border-radius: 8px;
}
.loading {
  background-color: #e0e7ff;
}
.error {
  background-color: #ffe4e6;
  color: #9f1239;
}
</style>