// stores/itemStore.ts
import { defineStore } from 'pinia';
import { apiService } from '../apiService'; // Adjust path as needed

interface Item {
  id?: number;
  name: string;
  // Add other properties as needed
}

interface ItemState {
  items: Item[];
  loading: boolean;
  error: any | null;
}

export const useItemStore = defineStore('itemStore', {
  state: (): ItemState => ({
    items: [],
    loading: false,
    error: null,
  }),
  actions: {
    async fetchAllItems() {
      this.loading = true;
      this.error = null;
      try {
        this.items = await apiService.getAllItems();
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = false;
      }
    },

    async addItem(item: Item) {
      this.loading = true;
      this.error = null;
      try {
        const newItem = await apiService.insertItem(item);
        this.items.push(newItem);
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = false;
      }
    },

    async modifyItem(id: number, updatedItem: Item) {
      this.loading = true;
      this.error = null;
      try {
        const modifiedItem = await apiService.updateItem(id, updatedItem);
        const index = this.items.findIndex(item => item.id === id);
        if (index !== -1) {
          this.items[index] = modifiedItem;
        }
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = false;
      }
    },

    async removeItem(id: number) {
      this.loading = true;
      this.error = null;
      try {
        await apiService.deleteItem(id);
        this.items = this.items.filter(item => item.id !== id);
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = false;
      }
    },
  },
});