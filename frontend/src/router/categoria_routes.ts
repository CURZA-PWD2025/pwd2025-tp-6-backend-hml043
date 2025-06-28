const categoria_routes = [
  {
    path: '/categorias',
    name: 'categoria_view',
    component: () => import('@/views/CategoriaView.vue'),
    children: [
      {
        path: '',
        name: 'categoria_list',
        component: () => import('@/components/categoria/CategoriaList.vue'),
      },
      {
        path: ':id/update',
        name: 'categoria_update',
        component: () => import('@/components/categoria/CategoriaUpdate.vue'),
      },
      {
        path: '',
        name: 'categoria_create',
        component: () => import('@/components/categoria/CategoriaCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'categoria_show',
        component: () => import('@/components/categoria/CategoriaShow.vue'),
      },

    ]
  }
]

export default categoria_routes
