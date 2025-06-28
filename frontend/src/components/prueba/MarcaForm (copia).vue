<template>
  <div>
    <h1>Lista de Marcas</h1>
    <button @click="loadUsers">Cargar Marcas</button>
    <p v-if="loading">Cargando marcas...</p>
    <p v-if="error">{{ error }}</p>

    <ul v-if="users.length">
      <li v-for="user in users" :key="user.id">
        {{ user.name }} ({{ user.email }})
        <button @click="editUser(user)">Editar</button>
        <button @click="removeUser(user.id)">Eliminar</button>
      </li>
    </ul>

    <h2>Crear Nueva Marca</h2>
    <form @submit.prevent="addNewUser">
      <input type="text" v-model="newUser.name" placeholder="Nombre" required />
      <input type="email" v-model="newUser.email" placeholder="Email" required />
      <button type="submit">Crear Marca</button>
    </form>

    <h2 v-if="editingUser">Editar Marca</h2>
    <form v-if="editingUser" @submit.prevent="saveEditedUser">
      <input type="text" v-model="editingUser.name" placeholder="Nombre" required />
      <input type="email" v-model="editingUser.email" placeholder="Email" required />
      <button type="submit">Guardar Cambios</button>
      <button type="button" @click="cancelEdit">Cancelar</button>
    </form>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { UserService } 		from '@/services/apiServices';

interface User {
  id?: number;
  name: string;
  email: string;
}

<ProductCard :zapatilla="props.zapatilla" />

const users 	= ref<User[]>([]);
const loading = ref(false);
const error 	= ref<string | null>(null);

const newUser = ref<Omit<User, 'id'>>({ name: '', email: '' });
const editingUser = ref<User | null>(null);

const loadUsers = () => {
  loading.value = true;
  error.value = null;
  try { users.value = getAllItems(); }
  catch (err: any) { error.value = err.message || 'Falló la carga de marcas.'; }
  finally { loading.value = false; }
};

const addNewUser = async () => {
  error.value = null;
  try {
    // Aquí el backend podría devolver el usuario creado con su ID
    const createdUser = await UserService.createUser(newUser.value);
    console.log('Marca creado:', createdUser);
    await loadUsers(); // Volver a cargar la lista para ver el nuevo usuario
    newUser.value = { name: '', email: '' }; // Limpiar formulario
  } 
  catch (err: any) { error.value = err.message || 'Falló al crear el usuario.'; }
};

const editUser = (user: User) => {
  editingUser.value = { ...user }; // Crea una copia para evitar mutar el original directamente
};

const saveEditedUser = async () => {
  if (!editingUser.value || !editingUser.value.id) return;

  error.value = null;
  try {
    await UserService.updateUser(editingUser.value.id, {
      name: editingUser.value.name,
      email: editingUser.value.email
    });
    console.log('Marca actualizado');
    await loadUsers(); // Refrescar la lista
    editingUser.value = null; // Resetear el modo de edición
  }
  catch (err: any) { error.value = err.message || 'Falló al actualizar el usuario.'; }
};

const cancelEdit = () => {
  editingUser.value = null;
};

const removeUser = async (userId?: number) => {
  if (!userId) return;

  error.value = null;
  if (confirm(`¿Estás seguro de que quieres eliminar al usuario con ID ${userId}?`)) {
    try {
      await UserService.deleteUser(userId);
      console.log(`Marca con ID ${userId} eliminado.`);
      await loadUsers(); // Refrescar la lista
    } catch (err: any) {
      error.value = err.message || 'Falló al eliminar el usuario.';
    }
  }
};

onMounted(() => {
  loadUsers();
});
</script>