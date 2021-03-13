<template>
  <div>
      <div id="navigation">
       <b-nav tabs>
          <img style="width:200px;height:auto;padding: 0px 20px;position:relative;top:10px; float:left; margin-top:20px; margin-left:25px;" src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
                alt="--Cultime--" border="0">
      <router-link to="/feed">Feed</router-link> |
      <router-link to="/watchlist">Watch List</router-link> |
      <router-link to="/following">Following</router-link> |
      <router-link to="/recommended">Recommended</router-link> |
      <router-link to="/profile">Profile</router-link>

        </b-nav>

    </div>  

    <h4>Register</h4>
      <form>
        <label for="first_name">First Name</label>
        <div>
          <input id="first_name" type="text" v-model="first_name" required autofocus>
        </div>

        <label for="last_name">Last Name</label>
        <div>
          <input id="last_name" type="text" v-model="last_name" required autofocus>
        </div>

        <label for="username">Username</label>
        <div>
          <input id="username" type="text" v-model="username" required autofocus>
        </div>

        <label for="email" >E-Mail Address</label>
        <div>
          <input id="email" type="email" v-model="email" required>
        </div>

        <label for="password">Password</label>
        <div>
          <input id="password" type="password" v-model="password" required>
        </div>

        <label for="password-confirm">Confirm Password</label>
        <div>
          <input id="password-confirm" type="password" v-model="password_confirmation" required>
        </div>

        <div>
          <button type="submit" @click="handleSubmit">
            Register
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
  name: 'Register',
  components: {},
  data() {
    return {
      // Registration data below
      first_name: "",
      last_name: "",
      password: "",
      password_confirmation: "",
      username: "",
      email: "",
    }
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault()
      if (this.password === this.password_confirmation && this.password.length > 0)
      {
        let url = "http://localhost:8000/register/"
        axios.post(url, {
          username: this.username,
          password: this.password,
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name
        })
        .then(response => {
          //localStorage.setItem('user',JSON.stringify(response.data.user))
          //localStorage.setItem('jwt',response.data.token)

          console.log("New user added")
          console.log(response.data)

          // if (localStorage.getItem('jwt') != null){
          //   this.$emit('loggedIn')
          //   if(this.$route.params.nextUrl != null){
          //     this.$router.push(this.$route.params.nextUrl)
          //   }
          //   else{
          //     this.$router.push('/')
          //   }
          // }
        })
        .catch(error => {
          console.error(error);
        });
      } 
      else {
        this.password = ""
        this.passwordConfirm = ""

        return alert("Passwords do not match")
      }
    }
  },
}
</script>
