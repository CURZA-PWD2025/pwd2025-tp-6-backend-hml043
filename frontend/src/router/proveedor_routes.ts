const proveedor_routes = [
  {
    path: '/proveedores',
    name: 'proveedor_view',
    component: () => import('@/views/ProveedorView.vue'),
    children: [
      {
        path: '',
        name: 'proveedor_list',
        component: () => import('@/components/proveedor/ProveedorList.vue'),
      },
      {
        path: ':id/update',
        name: 'proveedor_update',
        component: () => import('@/components/proveedor/ProveedorUpdate.vue'),
      },
      {
        path: '',
        name: 'proveedor_create',
        component: () => import('@/components/proveedor/ProveedorCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'proveedor_show',
        component: () => import('@/components/proveedor/ProveedorShow.vue'),
      },

    ]
  }
]
export default proveedor_routes
