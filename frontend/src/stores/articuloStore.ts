import { ref, computed }  from 'vue'
import { defineStore }    from 'pinia';
import Api                from '@/services/ApiService';
import type { Articulo }  from '@/interfaces/articulo'

export const useArticuloStore = defineStore('articulo', () => {  

  const url       = '/articulos'
  const msgError  = 'Error storeArticulo '
  const esError   = ref<string|null>(null)
  const esLoad    = ref(false)
  const esEditar  = ref(false)
  const idEditar  = ref(0)
  const item      = ref<Articulo>( {id: 0, descripcion: '', precio: 0, stock: 0, marca_id: 0, proveedor_id: 0, categorias: []} )
  const items     = ref<Articulo[]>([])

  async function getItemAll() {
      esLoad.value  = true
      esError.value = null
      try { items.value = await Api.getItemAll(url); }
      catch (error) { esError.value = error; console.log(msgError+'getItemAll:', esError.value); }
      finally { esLoad.value = false; }
  }

  async function getItemId() {
      esLoad.value  = true
      esError.value = null
      try { items.value = await Api.getItemId(url, id); }
      catch (error) { esError.value = error; console.log(msgError+'getItemId:', esError.value); }
      finally { esLoad.value = false; }
  }

  async function addItem(data:any) {
      esLoad.value  = true
      esError.value = null
      try { await Api.addItem(url+'/', data);
          items.value = await Api.getItemAll(url); }
      catch (error) { esError.value = error; console.log(msgError+'addItem:', esError.value); }
      finally { esLoad.value = false; }
  }

  async function updItem(id:number, data:any) {
      esLoad.value  = true
      esError.value = null
      try { await Api.updItem(url, id, data);
          items.value = await Api.getItemAll(url); }
      catch (error) { esError.value = error; console.log(msgError+'updItem:', esError.value); }
      finally { esLoad.value = false; }
  }

  async function delItem(id:number) {
      esLoad.value  = true
      esError.value = null
      try { await Api.delItem(url, id);
          items.value = await Api.getItemAll(url); }
      catch (error) { esError.value = error; console.log(msgError+'delItem:', esError.value); }
      finally { esLoad.value = false; }
  }

  return {
    //items:   computed(() => items.value),
    esLoad:  computed(() => esLoad.value),
    esError: computed(() => esError.value),
    items, item, esEditar, idEditar, getItemAll, getItemId, addItem, updItem, delItem
  }
})