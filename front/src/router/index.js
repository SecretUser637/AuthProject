import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/registration',
      name: 'reg',
      component: RegisterView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    }
  ]
})
router.beforeEach(async (to, from, next) => {
  let isAuth = false;
  if (localStorage.getItem('JWT_token')) {
    console.log(localStorage.getItem('exp'))
    console.log(new Date().getTime() / 1000)
    if ((localStorage.getItem('exp') - (new Date().getTime() / 1000)) >= 0) {
      isAuth = true
    }
  }
  console.log(isAuth)
  if (to.name == 'home' && !isAuth) {
    next({ name: 'login' })
  }
  else {
    next()
  }
})
export default router
