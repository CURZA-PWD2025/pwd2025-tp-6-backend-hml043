<template>
  <main>
    <div class="titulo-contenedor">
      <h1>Categorias</h1>
      <img alt="Unco logo" class="logo" src="@/assets/ico_categoria.svg" width="35" height="35"/>
    </div>

    <CategoriaList />

  </main>
</template>

<script setup lang="ts">
import CategoriaList from '@/components/categoria/CategoriaList.vue';
</script>

<style scoped>
  /* --- Titulo e imagen --- */
.titulo-contenedor {
  display: flex;          /* Activa el modo Flexbox: los hijos se ponen en fila */
  align-items: center;    /* ALINEACIÓN VERTICAL: Centra los hijos verticalmente. Esta es la clave. */
  gap: 22px;              /* Espacio horizontal entre la imagen y el título. Más moderno que 'margin'. */
  /* margin-bottom: 2rem; */
}

.titulo-contenedor h1 {
  margin: 0;              /* Quitamos el margen por defecto del h1 para un mejor control */
  font-size: 36px;        /* Ajusta el tamaño de la fuente */
  color: #333;
}
</style>