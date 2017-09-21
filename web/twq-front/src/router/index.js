import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/Login'
import CriarForm from '@/components/CriarForm'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login/',
      name: 'Login',
      component: Login
    },
    {
    	path: '/criarForm',
    	name: 'CriarForm',
    	component: CriarForm
    }
  ]
})
