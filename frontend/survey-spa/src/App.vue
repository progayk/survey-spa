<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <app-header></app-header>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/Header'
export default {
  name: 'App',
  components: {
    'app-header': Header
  }
}
</script>

<style lang="scss">
@import '~bulma/bulma'
</style>
