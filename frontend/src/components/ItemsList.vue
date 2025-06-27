<!-- components/ItemsList.vue -->
<template>
  <div>
    <h1>Items</h1>
    <p v-if="itemsStore.loading">Loading items...</p>
    <p v-if="itemsStore.error" class="error">{{ itemsStore.error }}</p>
    <ul>
      <li v-for="item in itemsStore.items" :key="item.id">
        {{ item.name }}
        <button @click="handleUpdate(item.id)">Edit</button>
        <button @click="handleDelete(item.id)">Delete</button>
      </li>
    </ul>
    <button @click="handleInsert">Add New Item</button>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useItemsStore } from '../stores/items';

const itemsStore = useItemsStore();

onMounted(() => {
  itemsStore.fetchAllItems();
});

const handleInsert = async () => {
  const newItem = { name: 'New Item ' + Date.now() }; // Example data
  await itemsStore.insertItem(newItem);
};

const handleUpdate = async (id) => {
  const updatedItem = { name: 'Updated Item ' + Date.now() }; // Example data
  await itemsStore.updateItem(id, updatedItem);
};

const handleDelete = async (id) => {
  await itemsStore.deleteItem(id);
};
</script>

<style scoped>
.error {
  color: red;
}
</style>