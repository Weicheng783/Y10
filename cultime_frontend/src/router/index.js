import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Feed from '../views/Feed.vue'
import WatchList from '../views/WatchList.vue'
import Following from '../views/Following.vue'
import Recommended from '../views/Recommended.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      guest: true
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: {
      guest: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      guest: true
    }
  },
  {
    path: '/feed',
    name: 'Feed',
    component: Feed,
    meta: {
      requiresAuth: true,
    }
  },
  {
    path: '/watchlist',
    name: 'WatchList',
    component: WatchList,
    meta: {
      requiresAuth: true,
    }
  },
  {
    path: '/following',
    name: 'Following',
    component: Following,
    meta: {
      requiresAuth: true,
    }
  },
  {
    path: '/recommended',
    name: 'Recommended',
    component: Recommended,
    meta: {
      requiresAuth: true,
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// Must be rewritten
router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('jwt') == null) {
      next({
        path: '/login',
        params: { nextUrl: to.fullPath }
      })
    }
    else {
      next()
    }
  } 
  else if(to.matched.some(record => record.meta.guest)) {
    if(localStorage.getItem('jwt') == null){
      next()
    }
    else{
      next({ name: 'Feed'})
    }
  }
  else {
    next()
  }
})

export default router
