<template>
  <div class="login">
    <form>
      <label for="username" >Username</label>
      <div>
        <input id="username" type="text" v-model="username" required autofocus>
      </div>
      <div>
        <label for="password" >Password</label>
        <div>
          <input id="password" type="password" v-model="password" required>
        </div>
      </div>
      <div>
        <button type="submit" @click="handleSubmit">
          Login
        </button>
      </div>
  </form>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

import axios from 'axios'

export default {
  name: 'Login',
  data() {
    return {
      username: "",
      password: "",
    }
  },
  methods: { 
    handleSubmit(e){
      e.preventDefault()
        if (this.password.length > 0) {
          axios.post('http://localhost:8000/login/', {
            username: this.username,
            password: this.password
          })
          .then(response => {
            console.log(this.username, this.password)
            console.log(response.data)
            //localStorage.setItem('user',JSON.stringify(response.data.user))
            localStorage.setItem('jwt', JSON.stringify(response.data))

            if (localStorage.getItem('jwt') != null){
              this.$emit('loggedIn')
              if(this.$route.params.nextUrl != null){
                this.$router.push(this.$route.params.nextUrl)
              }
              else {
                this.$router.push('feed')
              }
            }
          })
          .catch(function (error) {
            console.error(error.response);
          });
      }
    }
  }
}
</script>
