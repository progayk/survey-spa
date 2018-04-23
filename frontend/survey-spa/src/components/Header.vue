<!--With the Login component coded up and its route defined I can provide access to it via a router-link component in the Header-->
<!--component within components/Header.vue. I conditionally show either the link to the NewSurvey component or the Login component-->
<!--by utilizing the isAuthenticated store getter once more within a computed property in the Header component referenced by-->
<!--v-if directives.-->
<template>
  <nav class="navbar is-light" role="navigation" aria-label="main navigation">
    <div class="navbar-menu">
      <div class="navbar-start">
        <router-link to="/" class="navbar-item">
          Home
        </router-link>
        <router-link v-if="isAuthenticated" to="/surveys" class="navbar-item">
          Create Survey
        </router-link>
        <router-link v-if="!isAuthenticated" to="/login" class="navbar-item">
          Login / Register
        </router-link>
      </div>
    </div>
  </nav>

</template>

<script>
export default {
  computed: {
    isAuthenticated () {
      return this.$store.getters.isAuthenticated
    }
  }
}
</script>

<style scoped>

</style>
