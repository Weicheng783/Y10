<template>
  <div id="app">
    <router-view v-on:logOut="logOut" />
  </div>
</template>

<script>
export default {
  name: "app",
  methods: {
    logOut() {
      localStorage.removeItem('jwt');
      this.$router.push('/')
    }
  },
};

</script>

<style>
#app {
  color:white;
  margin: 0px;
  background-color: #201c1c;
  background-size: cover;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: #ffffff;
}
p, label{
  color: white;
}
</style>
