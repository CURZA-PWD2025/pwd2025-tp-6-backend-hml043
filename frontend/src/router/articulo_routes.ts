const articulo_routes = [
  {
    path: '/articulos',
    name: 'articulo_view',
    component: () => import('@/views/ArticuloView.vue'),
    children: [
      {
        path: '',
        name: 'articulo_list',
        component: () => import('@/components/articulo/ArticuloList.vue'),
      },
      {
        path: ':id/update',
        name: 'articulo_update',
        component: () => import('@/components/articulo/ArticuloUpdate.vue'),
      },
      {
        path: '',
        name: 'articulo_create',
        component: () => import('@/components/articulo/ArticuloCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'articulo_show',
        component: () => import('@/components/articulo/ArticuloShow.vue'),
      },

    ]
  }
]
export default articulo_routes
