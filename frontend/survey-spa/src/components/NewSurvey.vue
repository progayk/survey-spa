<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{ name }}</h2>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="tabs is-center is-fullwidth is-large">
          <ul>
            <li :class="{'is-active': step == 'name'}" @click="step = 'name'">
              <a>Name</a>
            </li>
            <li :class="{'is-active': step == 'questions'}" @click="step = 'questions'">
              <a>Questions</a>
            </li>
            <li :class="{'is-active': step == 'review'}" @click="step = 'review'">
              <a>Review</a>
            </li>
          </ul>
        </div>
        <div class="columns">
          <div class="column is-half is-offset-one-quarter">

            <div class="name" v-show="step == 'name'">
              <h2 class="is-large">Add Name</h2>
            </div>

            <div class="questions" v-show="step == 'questions'">
              <h2 class="is-large">Add Questions</h2>
            </div>

            <div class="review" v-show="step == 'review'">
              <h2 class="is-large">Review and Submit</h2>
            </div>

          </div>
        </div>
      </div>
    </section>
  </div>

</template>

<script>
export default {
  data () {
    return {
      step: 'name'
    }
  }
}
</script>

<style scoped>

</style>
