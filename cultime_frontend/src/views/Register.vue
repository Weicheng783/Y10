<template>
<body style="background-color:#201c1c;">
  <div>
    <div id="navigation">
        <a href="/" style="background-color: #201c1c; width:200px;height:auto;padding: 0px 20px;position:relative;top:10px; float:left; margin-top:20px; margin-left:25px;"><img style=" " src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
              alt="--Cultime--"  border="0"></a>
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login</router-link>
        <router-link to="/register">Create Account</router-link>
    </div>
    
    <div style="text-align:right;">
        <a style="padding:0px;margin:0px;"><img style="width:600px;height:750px;padding: 25px 20px;border-radius:40px;" :src="randomMoviePoster" alt="Movie Poster" width="550"></a>
    </div>

    <div style="background-color:#262728;width:500px;position:relative;bottom:725px;left:100px;border-radius:25px;border:#1D1E1F; padding:30px;margin:0px;text-align:left">
      <form>
        <p class="title is-5" style="color:white;padding:10px;margin:5px; text-align: center;">Create your Cultime account</p>

        <p style="text-align:left; color:white;padding:25px 0px 10px 0px;">First Name</p>
        <input class="input" placeholder="Type your first name..." id="input-dark" v-model="first_name" required autofoces>
        
        <p style="text-align:left; color:white;padding:25px 0px 10px 0px;">Last Name</p>
        <input class="input" placeholder="Type your last name..." id="input-dark" v-model="last_name" required autofoces>

        <p style="text-align:left; color:white;padding:25px 0px 10px 0px;">Username</p>
        <input class="input" placeholder="Type your username..." id="input-dark" v-model="username" required autofoces>

        <p style="text-align:left; color:white;padding:25px 0px 10px 0px;">E-Mail Address</p>
        <input class="input" placeholder="Type your email..." id="input-dark" v-model="email" required autofoces>

        <p style="text-align:left; color:white;padding:25px 0px 10px 0px;">Password</p>
        <input class="input" type="password"  placeholder="Type your password..." id="input-dark" v-model="password" required autofoces>

        <p style="text-align:left; color:white;padding:25px 0px 10px 0px;">Consfirm Password</p>
        <input class="input" type="password" placeholder="Confirm your password..." id="input-dark" v-model="password_confirmation" required autofoces>

        <div>
          <button class="button-register" style="margin-top: 50px; width: 100%;" type="submit" @click="handleSubmit">
            Register
          </button>
        </div>

        <p style="text-align:center; margin-top: 15px;">{{message}}</p>
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
      message: "",
      randomMoviePoster: "",
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
        .then(() => {
          var self = this;
          // localStorage.setItem('user',JSON.stringify(response.data.user))
          // localStorage.setItem('jwt',response.data.token)

          // console.log("New user added")
          // console.log(response.data)

          // if (localStorage.getItem('jwt') != null){
          //   this.$emit('loggedIn')
          //   if(this.$route.params.nextUrl != null){
          //     this.$router.push(this.$route.params.nextUrl)
          //   }
          //   else{
          //     this.$router.push('/')
          //   }
          // }
          self.message = "Your account has been created! Login to continue!";
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
  mounted() {
    axios.get('http://localhost:8000/trending/').then(data => {
      let trendingMovies = [];
      for(let i=0;i<data.data.length;i++) {
        trendingMovies.push({
          movieId: data.data[i]['id'],
          movieTitle: data.data[i]['title'],
          moviePoster: data.data[i]['poster_path'],
          shortSummary: data.data[i]['overview'],
          yearProduction: data.data[i]['release_date'],
        });
      }

    
      this.randomMoviePoster = "https://image.tmdb.org/t/p/original/" + trendingMovies[
        Math.floor(Math.random() * trendingMovies.length)
      ].moviePoster;
    });
  }
}
</script>

<style>
.button-register{
  font-weight:bold;
  color: white;
  background-color:#036FC0;
  border:#036FC0;
  padding: 15px 150px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 20px;
}

.button-register:hover{
  background-color: #065591;
}

#input-dark {
  background-color: #333333;
  border: none;
  color: white;
  width: 100%;
  padding-left: 10px;
}

#input-dark:focus {
  background-color: #383838;
  outline:none;
  color: white;
}

</style>