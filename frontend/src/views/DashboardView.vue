<template>
  <div class="dashboard-layout">
    <aside class="sidebar">
      <div class="titulo-contenedor">
        <img alt="Unco logo" class="logo" src="@/assets/Logo_UnCo_bn.png"/>
        <h1 class="app-title">PW2025</h1>
        <!-- <h1 class="app-title">PW2025</h1> -->
      </div>
      <nav>
        <ul>
          <li><router-link :to="{name: 'articulos'  }">Artículos</router-link></li>
          <li><router-link :to="{name: 'proveedores'}">Proveedores</router-link></li>
          <li><router-link :to="{name: 'marcas'     }">Marcas</router-link></li>
          <li><router-link :to="{name: 'categorias' }">Categorías</router-link></li>
          <li><hr></li>
          <li><router-link :to="{name: 'usuarios'   }">Usuarios</router-link></li>
          <li><hr></li>
          <li><router-link :to="{name: 'configuracion'}">Configuracion</router-link></li>
        </ul>
      </nav>
    </aside>

    <main class="main-content">
      <header class="top-navbar">
        <button class="auth-button">Login</button>
      </header>
      <div class="content-area">

        <router-view />

      </div>
    </main>
  </div>
</template>

<script setup>
</script>

<style scoped>
.dashboard-layout {  
  display: flex;  
  height: 100vh;
  width: 1200px;
}

@media (min-width: 900px) {
  width: 1500px;
}

/* --- Titulo e imagen --- */
.titulo-contenedor {
  display: flex;          /* Activa el modo Flexbox: los hijos se ponen en fila */
  align-items: center;    /* ALINEACIÓN VERTICAL: Centra los hijos verticalmente. Esta es la clave. */
  gap: 12px;              /* Espacio horizontal entre la imagen y el título. Más moderno que 'margin'. */
  margin-bottom: 2rem;
}

.titulo-contenedor img {
  height: 50px;           /* Ajusta la altura de la imagen según el tamaño de tu título */
  width: auto;            /* El ancho se ajusta automáticamente para mantener la proporción */
}

.titulo-contenedor h1 {
  margin: 0;              /* Quitamos el margen por defecto del h1 para un mejor control */
  font-size: 24px;        /* Ajusta el tamaño de la fuente */
  color: white; /* #333; */  
}

/* --- Barra Lateral --- */
.sidebar {
  width: 250px;
  background-color: #2d3748; /* Gris oscuro */
  color: white;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
}

.app-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 2rem;
  text-align: center;
}

.sidebar nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar nav li {
  margin-bottom: 0.5rem;
}

.sidebar nav a {
  display: block;
  color: white;
  text-decoration: none;
  padding: 0.75rem 1rem;
  border-radius: 8px; /* Vértices redondeados */
  transition: background-color 0.3s ease;
}

/* Efecto "over" */
.sidebar nav a:hover,
.sidebar nav a.router-link-exact-active {
  background-color: #4a5568; /* Rectángulo más claro */
}


/* --- Contenido Principal --- */
.main-content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

/* --- Barra de Navegación Superior --- */
.top-navbar {
  position: sticky;
  top: 0;
  width: 100%;
  background-color: white;
  padding: 0.75rem 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* border-bottom: 1px solid black; */
  display: flex;
  justify-content: flex-end;
  z-index: 10;
}

.auth-button {
  background-color: white;
  color: black;
  border: 1px solid black;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
}

/* --- Área de Contenido --- */
.content-area {
  flex-grow: 1;
  background-color: #fcfefe;  /* #f7fafc; */ /* Gris claro */
  padding: 1.5rem;
  overflow-y: auto;
}
</style>
