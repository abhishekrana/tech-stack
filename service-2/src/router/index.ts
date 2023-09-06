import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: ProductView,
    // },
    {
      path: '/products',
      name: 'products',
      // route level code-splitting
      // this generates a separate chunk (Product.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ProductView.vue'),
    },
    {
      path: '/users',
      name: 'users',
      component: () => import('../views/UserView.vue'),
    },
  ],
})

export default router
