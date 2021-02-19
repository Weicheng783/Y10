<template>
    <div>
      <div id="nav">
        <router-link to="/">Home</router-link> |
        <router-link to="/login">Login</router-link> |
        <router-link to="/register">Create Account</router-link>
      </div>
      <p>{{movieTitle}}</p>
    </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data() {
    return {
        movieTitle: "Parasite",
    }
  },
}
</script>
