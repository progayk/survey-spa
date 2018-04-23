import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Survey from '@/components/Survey'
import NewSurvey from '@/components/NewSurvey'
import Login from '@/components/Login'
import store from '@/store'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }, {
      // :id is for Dynamic Segment
      path: '/surveys/:id',
      name: 'Survey',
      component: Survey
    }, {
      path: '/surveys',
      name: 'NewSurvey',
      component: NewSurvey,
      // ts worth mentioning here that I am utilizing vue-router's route guard beforeEnter
      // to check to see if the current user is authenticated via the isAuthenticated getter
      // from the store. If isAuthenticated returns false then I redirect the application to
      // the login page.
      beforeEnter (to, from, next) {
        if (!store.getters.isAuthenticated) {
          next('/login')
        } else {
          next()
        }
      }
    }, {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
