<template>
  <div>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/register">Create Account</router-link>
    </div>

      <form class="form">

        <h3 style="color:white;  margin:5px;">───────Create Account───────</h3>

        <div class="field">
         <label for="first_name">First Name</label>
         <div class="control">
           <input style="width: 100%" placeholder="First Name" id="first_name" type="text" v-model="first_name" required autofocus>
         </div>
        </div>

        <div class="field">
          <label for="last_name">Last Name</label>
          <div>
            <input style="width: 100%" placeholder="Last Name" id="last_name" type="text" v-model="last_name" required autofocus>
          </div>
        </div>

        <div class="field">
          <label for="username">Username</label>
          <div>
            <input style="width: 100%" placeholder="Username" id="username" type="text" v-model="username" required autofocus>
          </div>
        </div>

        <div class="field">
          <label for="email" >E-Mail Address</label>
          <div>
            <input style="width: 100%" placeholder="E-Mail" id="email" type="email" v-model="email" required>
          </div>
        </div>

        <div class="field">
          <label for="password">Password</label>
          <div>
            <input style="width: 100%" placeholder="Password" id="password" type="password" v-model="password" required>
          </div>
        </div>

        <div class="field">
          <label for="password-confirm">Confirm Password</label>
          <div>
            <input style="width: 100%" placeholder="Password" id="password-confirm" type="password" v-model="password_confirmation" required>
          </div>
        </div>

        <div>
          <button style="margin-top: 20px;" type="submit" @click="handleSubmit">
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
        let url = "http://localhost:8000/authentication/register/"
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

<style>
    
    input{
      border: #black;
      border-radius: 8px;
      background-color:#262728;
      text-align:center;
      padding:15px 145px;
      
    }

    label{
      float: left;
      padding-bottom: 5px;
      color:white;
      
      font-weight: bold;
    }

    button{
      font-weight:bold;
      color: white;
      background-color:#036FC0;
      border:#036FC0;
      padding: 15px 150px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 20px;
      

    }

    button:hover{
      background-color: #065591;
    }

    


    .form{
      float: left;
      border: 5px solid #262728;
      border-radius: 20px;
      background-color: #262728;
      margin-left: 200px;
      padding: 20px 20px 20px 20px;
      

    }
</style>
