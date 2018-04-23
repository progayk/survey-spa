import Vue from 'vue'
import Vuex from 'vuex'

// imports of AJAX function go here
import { fetchSurveys, fetchSurvey, saveSurveyResponse, postNewSurvey, authenticate, register } from '@/api'
import { isValidJwt, EventBus } from '@/utils'

Vue.use(Vuex)

// The state object will serve as the single source of truth where all the important application-level
// data is contained within the store. This state object will contain survey data that can be accessed
// and watched for changes by any components interested in them such as the Home component
const state = {
  // single source of data
  surveys: [],
  currentSurvey: {},
  user: {},
  jwt: ''
}

// The actions object is where I will define what are known as action methods.
//  Action methods are referred to as being "dispatched" and they're used to
// handle asynchronous operations such as AJAX calls to an external service or API.
const actions = {
  // asynchronous operations
  loadSurveys (context) {
    return fetchSurveys()
      .then((response) => {
        context.commit('setSurveys', { surveys: response.data })
      })
  },
  loadSurvey (context, { id }) {
    return fetchSurvey(id)
      .then((response) => {
        context.commit('setSurvey', { survey: response.data })
      })
  },
  addSurveyResponse (context) {
    return saveSurveyResponse(context.state.currentSurvey)
  },
  login (context, userData) {
    context.commit('setUserData', { userData })
    return authenticate(userData)
      .then(response => context.commit('setJwtToken', { jwt: response.data }))
      .catch(error => {
        console.log('Error Authenticating: ', error)
        EventBus.$emit('failedAuthentication', error)
      })
  },
  register (context, userData) {
    context.commit('setUserData', { userData })
    return register(userData)
      .then(context.dispatch('login', userData))
      .catch(error => {
        console.log('Error Registering: ', error)
        EventBus.$emit('failedRegistering:', error)
      })
  },
  submitNewSurvey (context, survey) {
    return postNewSurvey(survey, context.state.jwt.token)
  }
}

// The mutations object provides methods which are referred to being "committed" and serve as the one
// and only way to change the state of the data in the state object. When a mutation is committed any
// components that are referencing the now reactive data in the state object are updated with the new
// values, causing the UI to update and re-render its elements.
const mutations = {
  // isolated data mutations
  setSurveys (state, payload) {
    state.surveys = payload.surveys
  },
  setSurvey (state, payload) {
    const nQuestions = payload.survey.questions.length
    for (let i = 0; i < nQuestions; i++) {
      payload.survey.questions[i].choice = null
    }
    state.currentSurvey = payload.survey
  },
  setChoice (state, payload) {
    const { questionId, choice } = payload
    const nQuestions = state.currentSurvey.questions.length
    for (let i = 0; i < nQuestions; i++) {
      if (state.currentSurvey.questions[i].id === questionId) {
        state.currentSurvey.questions[i].choice = choice
        break
      }
    }
  },
  setUserData (state, payload) {
    console.log('setUserData payload = ', payload)
    state.userData = payload.userData
  },
  setJwtToken (state, payload) {
    console.log('setJwtToken payload = ', payload)
    localStorage.token = payload.jwt.token
    state.jwt = payload.jwt
  }
}

// The getters object contains methods also, but in this case they serve to access the state data
// utilizing some logic to return information. Getters are useful for reducing code
// duplication and promote reusability across many components.
const getters = {
  // reusable data accessors
  isAuthenticated (state) {
    return isValidJwt(state.jwt.token)
  }
}

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})

export default store
