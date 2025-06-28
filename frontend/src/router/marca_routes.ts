//import MarcaForm from '@/components/marca/MarcaForm.vue';

const marca_routes = [
  {
    path: '/marcas',
    name: 'marca_view',
    component: () => import('@/views/MarcaView.vue'),
    children: [      
      {
        path: ':id/edit',
        name: 'marca_edit',
        component: () => import('@/components/marca/MarcaForm.vue'),
      },
      {
        path: 'create',
        name: 'marca_create',
        component: () => import('@/components/marca/MarcaForm.vue'),
      },
      /*
      {
        path: '/list',
        name: 'marca_list',
        component: () => import('@/components/marca/MarcaList.vue'),
      },
      {
        path: ':id/show',
        name: 'marca_show',
        component: () => import('@/components/marca/MarcaShow.vue'),
      },
      */
    ]
  }
]

export default marca_routes
