<template>
<body style="background-color:#201c1c;">
  <div id="login">
    <div id="nav">
      <b-nav tabs>
        <a href="https://ibb.co/d4hyWLB"><img style="width:160px;height:30px;padding: 0px 20px;position:relative;top:10px;" src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
        alt="Screenshot-2021-03-01-at-22-22-49" border="0"></a>
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/register">Create Account</router-link>
      </b-nav>
      <br style="fill:white;">
          <div style="text-align:right;">
        <a style="padding:0px;margin:0px;" href="https://ibb.co/VH2nb2P"><img style="width:600px;height:750px;padding: 25px 20px;border-radius:40px;" src="https://i.ibb.co/wJMG8Mx/Screenshot-2021-03-01-at-10-00-45.png" 
        alt="Screenshot-2021-03-01-at-10-00-45" width="550"></a>
      </div>
    </div>
    <div style="background-color:#262728;width:500px;position:relative;bottom:725px;left:100px;border-radius:25px;border:#1D1E1F;
    padding:30px;margin:0px;text-align:left">
    <form>
      <div>
        <button style="font-weight:bold;color: white;background-color:#DC4437;border:#DC4437;
        padding: 30px 152px;border-radius:8px;margin:30px 0px;" class="ui button toggle" 
        :class="{active:isActive}" type="submit" 
        @click="isActive = !isActive, handleSubmit">Login with Google</button>
      </div>
      <div>
        <button style="font-weight:bold;color: white;background-color:#4267B2;border:#4267B2;
        padding: 30px 142px;border-radius:8px;margin:0px 0px;" class="ui button toggle" 
        :class="{active:isActive}" type="submit" 
        @click="isActive = !isActive, handleSubmit">Login with Facebook</button>
      </div>
      <div>
        <P style="color:white;padding:10px;margin:5px;"> ─────── Login with your account ───────</p>
      </div>
      <p style="color:white;padding:10px;" for="username" >Username:</p>
      <div>
        <input placeholder="Type your username..." style="color:white;background-color:#262728;border:#black;
        padding:15px 145px;border-radius:8px;text-align:left;" id="username" type="text" v-model="username" required autofocus>
      </div>
      <div>
        <p style="color:white;padding:10px;" for="password" >Password:</p>
        <div>
          <input placeholder="Type your password..." style="color:white;background-color:#262728;border:#black;
        padding:15px 145px;border-radius:8px;" id="password" type="password" v-model="password" required>
        </div>
      </div>
      <div>
        <button style="font-weight:bold;color: white;background-color:#036FC0;border:#036FC0;
        padding: 30px 200px;border-radius: 8px;margin:30px 0px;" class="ui button toggle" 
        :class="{active:isActive}" type="submit" 
        @click="isActive = !isActive, handleSubmit">Login</button>
      </div>
      <b-nav tabs>
        <router-link style="color:white;padding:0px;position:relative;left:125px;" to="/register">Create account instead?</router-link>
      </b-nav>
  </form>
  </div>
  </div>
</body>
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
      isActive: false,
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

<style>

input { 
    text-align:left; 
}
</style>