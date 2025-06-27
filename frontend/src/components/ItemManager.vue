<!-- components/ItemManager.vue -->
<template>
  <div>
    <h1>Item Manager</h1>
    <p v-if="itemStore.loading">Loading items...</p>
    <p v-if="itemStore.error">Error: {{ itemStore.error.message }}</p>

    <ul>
      <li v-for="item in itemStore.items" :key="item.id">
        {{ item.name }}
        <button @click="editItem(item)">Edit</button>
        <button @click="itemStore.removeItem(item.id!)">Delete</button>
      </li>
    </ul>

    <form @submit.prevent="submitItem">
      <input type="text" v-model="newItemName" placeholder="New item name" />
      <button type="submit">{{ editingItem ? 'Update Item' : 'Add Item' }}</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useItemStore } from '../stores/itemStore'; // Adjust path as needed

const itemStore = useItemStore();
const newItemName = ref('');
const editingItem = ref<any | null>(null);

onMounted(() => {
  itemStore.fetchAllItems();
});

const submitItem = async () => {
  if (editingItem.value) {
    await itemStore.modifyItem(editingItem.value.id!, { ...editingItem.value, name: newItemName.value });
    editingItem.value = null;
  } else {
    await itemStore.addItem({ name: newItemName.value });
  }
  newItemName.value = '';
};

const editItem = (item: any) => {
  editingItem.value = { ...item };
  newItemName.value = item.name;
};
</script>