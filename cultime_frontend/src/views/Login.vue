<template>
<body style="background-color:#201c1c;">
  <div id="login">
    <div id="navigation">
          <a href="/" style="background-color: #201c1c; width:200px;height:auto;padding: 0px 20px;position:relative;top:10px; float:left; margin-top:20px; margin-left:25px;"><img style=" " src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
              alt="--Cultime--"  border="0"></a>
          <router-link to="/">Home</router-link>
          <router-link to="/login">Login</router-link>
          <router-link to="/register">Create Account</router-link>
    </div>

    <br style="fill:white;">
      
    <div style="text-align:right;">
        <a><img style="width:600px;height:750px;padding: 25px 20px;border-radius:40px;" :src="randomMoviePoster" alt="Movie Poster" width="550"></a>
    </div>

    <div style="background-color:#262728;width:500px;position:relative;bottom:725px;left:100px;border-radius:25px;border:#1D1E1F; padding:30px;margin:0px;text-align:left">
      
      <form>
        <!-- <div>
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
        </div> -->
        <div>
          <p class="title is-5" style="color:white;padding:10px;margin:5px; text-align: center;">Login with your Cultime account</p>
        </div>

        <div>
          <p style="color:white;padding:25px 0px 10px 0px;">Username:</p>
          <input class="input" placeholder="Type your username..." id="input-dark" v-model="username" required autofoces>
        </div>

        <div>
          <p style="color:white;padding:25px 0px 10px 0px;" for="password" >Password:</p>
          <input class="input" type="password" placeholder="Type your password..." id="input-dark" v-model="password" required autofoces>
        </div>

        <div>
          <p style="color:white;text-align:center;">{{message}}</p>
          <button style="font-weight:bold;color: white;background-color:#036FC0;border:#036FC0;
          padding: 30px 200px;border-radius: 8px;margin:30px 0px;" class="ui button toggle" 
          :class="{active:isActive}" type="submit" 
          @click="handleSubmit">Login</button>
        </div>
        <router-link style="color:white;padding:0px;position:relative;left:125px;" to="/register">Create account instead?</router-link>
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
      message: "",
      randomMoviePoster: "",
    }
  },
  methods: { 
    handleSubmit(e){
      var self = this;
      e.preventDefault()
        if (this.password.length > 0) {
          axios.post('http://localhost:8000/login/', {
            username: this.username,
            password: this.password
          })
          .then(response => {
           // console.log(this.username, this.password)
            //console.log(response.data)
            //localStorage.setItem('user',JSON.stringify(response.data.user))
            localStorage.setItem('jwt', JSON.stringify(response.data))

            if (localStorage.getItem('jwt') != null){
              this.$emit('loggedIn')
              if(this.$route.params.nextUrl != null){
                this.$router.push(this.$route.params.nextUrl)
              }
              else {
                this.$router.push('feed');
              }
            }
          })
          .catch(function () {
            // console.log(error);
            // console.log(this);
            self.message = "Incorrect username or password!";
          });
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