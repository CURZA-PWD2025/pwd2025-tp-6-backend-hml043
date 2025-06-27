import { createRouter, createWebHistory } from 'vue-router'
//import AboutView          from '@/views/AboutView.vue'
import DashboardView      from '@/views/DashboardView.vue';
import ArticuloView       from '@/views/ArticuloView.vue';
import ProveedorView      from '@/views/ProveedorView.vue';
import MarcaView          from '@/views/MarcaView.vue';
import CategoriaView      from '@/views/CategoriaView.vue';
import UsuarioView        from '@/views/UsuarioView.vue';
import ConfiguracionView  from '@/views/ConfiguracionView.vue';
import NoEncontradoView   from '@/views/NoEncontradoView.vue';
/*
import articulo_routes    from './articulo_routes'
import marca_routes       from './marca_routes'
import categoria_routes   from './categoria_routes'
import proveedor_routes   from './proveedor_routes'
*/
const routes = [
    { path: '/',              name: 'home',         component: DashboardView },    
    { path: '/marcas',        name: 'marcas',       component: MarcaView },
    { path: '/categorias',    name: 'categorias',   component: CategoriaView },
    { path: '/articulos',     name: 'articulos',    component: ArticuloView },
    { path: '/proveedores',   name: 'proveedores',  component: ProveedorView },    
    { path: '/usuarios',      name: 'usuarios',     component: UsuarioView },
    { path: '/configuracion', name: 'configuracion',component: ConfiguracionView },
    { path: "/:catchAll(.*)", name: 'noencontrado', component: NoEncontradoView },

    { path: '/marcas/:id/edit',     name: 'marca_edit',       component: () => import('@/components/marca/MarcaForm.vue') },
    { path: '/marcas/create',       name: 'marca_create',     component: () => import('@/components/marca/MarcaForm.vue') },
    { path: '/categorias/:id/edit', name: 'categoria_edit',   component: () => import('@/components/categoria/CategoriaForm.vue') },
    { path: '/categorias/create',   name: 'categoria_create', component: () => import('@/components/categoria/CategoriaForm.vue') },
    { path: '/articulos/:id/edit',  name: 'articulo_edit',    component: () => import('@/components/articulo/ArticuloForm.vue') },
    { path: '/articulos/create',    name: 'articulo_create',  component: () => import('@/components/articulo/ArticuloForm.vue') },
    { path: '/proveedores/:id/edit',name: 'proveedor_edit',   component: () => import('@/components/proveedor/ProveedorForm.vue') },
    { path: '/proveedores/create',  name: 'proveedor_create', component: () => import('@/components/proveedor/ProveedorForm.vue') },
/*  
  ...marca_routes,
  ...categoria_routes,
  ...proveedor_routes,
  ...articulo_routes,  
*/
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

/*
router.beforeEach((to, from) => {
  console.log(to.name)
})
*/

export default router

