<template>
  <div class="list-container">
    
    <header class="list-header">
      <h2>Listado actualizado</h2>
      <button class="add-button" @click="agregarItem">
        <Icon icon="tabler:circle-plus" class="add-icon" />
        <span>Agregar</span>
      </button>
    </header>

    <!-- Modal aqui -->
    <div id="myModal" class="modal">      
      <div class="modal-content">
        <span class="close">&times;</span>
        <p id="art_id">.</p>
        <p id="art_des">.</p>
        <p id="art_pre">.</p>
        <p id="art_sto">.</p>
      </div>
    </div>

    <div class="table-wrapper">
      <table class="data-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Descripción</th>
            <th>Precio</th>
            <th>Stock</th>
            <th class="actions-header">opciones</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="item in items" :key="item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.descripcion }}</td>
            <td>{{ $filters.formatNumberWithCommas(item.precio, 20) }}</td>            
            <td>{{ item.stock }}</td>
            <td class="action-icons">
              <button @click="editarItem(item.id)" title="Editar">
                <Icon icon="tabler:edit" />
              </button>
              <button @click="detalleItem(item.id)" title="Ver detalle">
                <Icon icon="mdi:magnify-plus-outline" />
              </button>
              <button @click="eliminarItem(item.id)" title="Eliminar">
                <Icon icon="tabler:trash" />
              </button>
            </td>
          </tr>
          <tr v-if="items.length === 0">
            <td colspan="3" class="no-data">No hay registros para mostrar.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Icon }           from '@iconify/vue';
import { storeToRefs }    from 'pinia'
import { useRouter }      from 'vue-router';  //, useRoute
import { useMarcaStore }  from '@/stores/marcaStore'

const router  = useRouter();  //router check //const route = useRoute(); Access current route
const store   = useMarcaStore()
const { esEditar, idEditar }  = storeToRefs(store)
const { esLoading, esError, getItemAll, delItem } = store
//const { esLoading, esError, getItemAll, getItemId, addItem, updItem, delItem } = store
// You need storeToRefs when destructuring, properties created with `ref` or `computed`
// But you don't need it when destructuring methods
const modal   = ref(null)
const span    = ref(null)


//const items   = ref<Marca[]>([]);
//const loading = ref(false);
const error   = ref<string | null>(null);
const newItem = ref<Omit<Marca, 'id'>>( { nombre: '', email: '' } );
const ediItem = ref<Marca | null>(null);

// --- Funciones para los botones ---

const agregarItem = () => {
  store.esEditar  = false 
  store.idEditar  = 0
  //router.push( {name: 'marca_create'} );
  router.push({name: 'articulo_create'});
/*router.push({name: 'categoria_create'});
  router.push( {name: 'proveedor_create'} ); */

  //alert(router.currentRoute.value.name)
  //alert(router.options.routes)
  //console.log('Current route:', route.value);   
};

const editarItem = (id:number) => {
  store.esEditar  = true
  store.idEditar  = id
  router.push( {name: 'marca_edit', params: {id: id}} )
  //console.log(`Editando artículo con ID: ${id}`);
};

const eliminarItem = (id?:number) => {
  if (!id) return;
  error.value = null;
  if (confirm(`Eliminar el registro con ID ${id} ?`)) {
    try { store.delItem(id); console.log(`Registro con ID ${id} eliminado`); }  //await loadUsers(); // Refrescar la lista    
    catch (err: any) {error.value = err.message || 'Falló al eliminar el registro';}
  }
};

/*
const eliminarItem = (id:number) => {
  console.log(`Eliminando artículo con ID: ${id}`);
  // Lógica de ejemplo para borrarlo de la lista
  // items.value = items.value.filter(a => a.id !== id);
};
*/

const detalleItem = (id:number) => {
  //console.log(items.value[0]);
  //console.log(typeof items.value)
  modal.value.style.display = "block";
  let itemTmp = items.value.filter(a => a.id === id);
  console.log(itemTmp[0])
  if (itemTmp) {
    let tmp1 = document.getElementById("art_id");
    tmp1.innerHTML = 'ID: '+ id;
    let tmp2 = document.getElementById("art_des");
    tmp2.innerHTML = itemTmp[0].descripcion;
    let tmp3 = document.getElementById("art_pre");
    tmp3.innerHTML = 'Precio: '+ itemTmp[0].precio;
    let tmp4 = document.getElementById("art_sto");
    tmp4.innerHTML = 'Stock: '+ itemTmp[0].stock;
  }
  //console.log(`Mostrando artículo con ID: ${id}`);
};

const setModal = () => {
  // Modal
  modal.value = document.getElementById("myModal");
  // Get the button that opens the modal
  //let btn = document.getElementById("myBtn");
  // Get the <span> element that closes the modal
  span.value = document.getElementsByClassName("close")[0];
  // When the user clicks on <span> (x), close the modal
  span.value.onclick = function() {modal.value.style.display = "none";}
  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal.value) {
      modal.value.style.display = "none";
    }
  }
}

onMounted(() => {
  try { store.getItemAll(); console.log('Carga registros finalizada'); }
  catch (err: any) { error.value = err.message || 'Falló al cargar los registros'; }

  setModal();
});



/****** DEBUG ************************************************************************ */
// --- Lógica y Datos de Ejemplo ---

// Definimos la estructura de un artículo para mayor claridad con TypeScript
interface Articulo {
  id: number;
  descripcion: string;
}
// Datos de ejemplo. En una aplicación real, esto vendría de una API.
const items = ref<Articulo[]>([
  { id: 101, descripcion: 'Teclado Mecánico RGB', precio: 125000.00, stock: 13 },
  { id: 102, descripcion: 'Mouse Inalámbrico Ergonómico', precio: 35000.00, stock: 7 },
  { id: 103, descripcion: 'Monitor Ultrawide 34"', precio: 450000.00, stock: 25 },
  { id: 104, descripcion: 'Webcam 4K con Micrófono', precio: 57000.00, stock: 0 },

  { id: 101, descripcion: 'Teclado Mecánico RGB', precio: 125000.00, stock: 13 },
  { id: 102, descripcion: 'Mouse Inalámbrico Ergonómico', precio: 35000.00, stock: 7 },
  { id: 103, descripcion: 'Monitor Ultrawide 34"', precio: 450000.00, stock: 25 },
  { id: 104, descripcion: 'Webcam 4K con Micrófono', precio: 57000.00, stock: 0 },
  { id: 101, descripcion: 'Teclado Mecánico RGB', precio: 125000.00, stock: 13 },
  { id: 102, descripcion: 'Mouse Inalámbrico Ergonómico', precio: 35000.00, stock: 7 },
  { id: 103, descripcion: 'Monitor Ultrawide 34"', precio: 450000.00, stock: 25 },
  { id: 104, descripcion: 'Webcam 4K con Micrófono', precio: 57000.00, stock: 0 },
  { id: 101, descripcion: 'Teclado Mecánico RGB', precio: 125000.00, stock: 13 },
  { id: 102, descripcion: 'Mouse Inalámbrico Ergonómico', precio: 35000.00, stock: 7 },
  { id: 103, descripcion: 'Monitor Ultrawide 34"', precio: 450000.00, stock: 25 },
  { id: 104, descripcion: 'Webcam 4K con Micrófono', precio: 57000.00, stock: 0 },
  { id: 101, descripcion: 'Teclado Mecánico RGB', precio: 125000.00, stock: 13 },
  { id: 102, descripcion: 'Mouse Inalámbrico Ergonómico', precio: 35000.00, stock: 7 },
  { id: 103, descripcion: 'Monitor Ultrawide 34"', precio: 450000.00, stock: 25 },
  { id: 104, descripcion: 'Webcam 4K con Micrófono', precio: 57000.00, stock: 0 },
  { id: 101, descripcion: 'Teclado Mecánico RGB', precio: 125000.00, stock: 13 },
  { id: 102, descripcion: 'Mouse Inalámbrico Ergonómico', precio: 35000.00, stock: 7 },
  { id: 103, descripcion: 'Monitor Ultrawide 34"', precio: 450000.00, stock: 25 },
  { id: 104, descripcion: 'Webcam 4K con Micrófono', precio: 57000.00, stock: 0 },
  { id: 101, descripcion: 'Teclado Mecánico RGB', precio: 125000.00, stock: 13 },
  { id: 102, descripcion: 'Mouse Inalámbrico Ergonómico', precio: 35000.00, stock: 7 },
  { id: 103, descripcion: 'Monitor Ultrawide 34"', precio: 450000.00, stock: 25 },
  { id: 104, descripcion: 'Webcam 4K con Micrófono', precio: 57000.00, stock: 0 },
  { id: 101, descripcion: 'Teclado Mecánico RGB', precio: 125000.00, stock: 13 },
  { id: 102, descripcion: 'Mouse Inalámbrico Ergonómico', precio: 35000.00, stock: 7 },
  { id: 103, descripcion: 'Monitor Ultrawide 34"', precio: 450000.00, stock: 25 },
  { id: 104, descripcion: 'Webcam 4K con Micrófono', precio: 57000.00, stock: 0 },
]);
/****** DEBUG ************************************************************************ */
</script>

<style scoped>
/* --- Paleta de Colores (Azules y Grises) --- */
:root {
  --color-background: #f8fafc; /* Gris muy claro para el fondo general */
  --color-container-bg: #ffffff; /* Blanco para el contenedor principal */
  --color-primary-text: #2d3748; /* Gris oscuro para el texto principal */
  --color-secondary-text: #718096; /* Gris medio para texto secundario */
  --color-border: #e2e8f0; /* Gris claro para bordes */
  --color-table-header-bg: #edf2f7; /* Azul/Gris muy pálido para encabezado */
  --color-icon-primary: #4a5568; /* Gris/Azul oscuro para iconos */
}

/* --- Estructura Principal --- */
.list-container {
  background-color: var(--color-container-bg);
  border-radius: 8px;
  padding: 1.5rem 2rem;
  /* box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); */
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid var(--color-border);
  padding-bottom: 1rem;
}

.list-header h2 {
  color: var(--color-primary-text);
  margin: 0;
  font-size: 1.5rem;
}

/* --- Botón de Alta --- */
.add-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background-color: transparent;
  border: none;
  color: var(--color-primary-text);
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 6px;
  transition: background-color 0.3s ease;

  /* --- El efecto clave --- */
  opacity: 0.5; /* Estado inicial atenuado */
  transition: opacity 0.3s ease, transform 0.2s ease;
}

.add-button:hover {
  background-color: var(--color-table-header-bg);

  opacity: 1; /* Estado nítido al pasar el cursor */
  transform: scale(1.3); /* Un pequeño efecto de zoom para dar feedback */
}

.add-button .add-icon {
  font-size: 1.5rem; /* Icono más grande */
  color: var(--color-icon-primary);
}

/* --- Tabla --- */

tr :nth-child(3),
tr :nth-child(4) {
  text-align: right;
  width: 15%;
}

.table-wrapper {
  overflow-x: auto; /* Para responsividad en pantallas pequeñas */
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  color: var(--color-primary-text);
}

.data-table th, .data-table td {
  padding: 0.75rem 1rem;
  text-align: left;
  border-bottom: 1px solid var(--color-border);
}

.data-table thead {
  background-color: #f7fafc; /* var(--color-table-header-bg); */
}

.data-table th {
  font-weight: 600;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-secondary-text);
}

.data-table tbody tr:hover {
  background-color: #f7fafc; /* Un sutil hover en la fila */
}

.no-data {
  text-align: center;
  color: var(--color-secondary-text);
  padding: 2rem;
  font-style: italic;
}

/* --- Iconos de Acción en cada Fila --- */
.actions-header {
  text-align: right;
}

.action-icons {
  text-align: right;
  white-space: nowrap;
}

.action-icons button {
  background: none;
  border: none;
  margin-left: 0.5rem;
  color: var(--color-icon-primary);
  font-size: 1.25rem; /* Tamaño de los iconos de acción */
  padding: 0.25rem;
  
  /* --- El efecto clave --- */
  opacity: 0.5; /* Estado inicial atenuado */
  transition: opacity 0.3s ease, transform 0.2s ease;
  cursor: pointer;
}

.action-icons button:hover {
  opacity: 1; /* Estado nítido al pasar el cursor */
  transform: scale(1.5); /* Un pequeño efecto de zoom para dar feedback */
}

/* --- The Modal (background) --- */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/***** Modal Content *****/

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 35%; /* 80% */
  font-size: 20px;
}

/* The Close Button */
.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
</style>