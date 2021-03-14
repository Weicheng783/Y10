

<template>
    <div id='color'>
      
      <div id="navigation">

      <b-nav tabs>
      <img @click="changeColor" style="width:180px;height:30px;padding: 0px 20px;position:relative;top:10px;" src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
        alt="--Cultime--" border="0">
     
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/register">Create Account</router-link>
      </b-nav>
  
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
        // movieTitle: "Parasite",
        
    }
  },
 


  methods: {
    

  }
}
</script>

<style>

#nav {
  font-weight: bold;
  appearance: button;

    border: none;
    background-color: #676172;

    /* color: #ceaf41; */
    padding: 20px 10px 10px 10px;
    /* margin: 30px 30px 20px 20px;  */
    margin-right:10px;
    margin-top:10px;
    /* padding-right: 10px; */
    text-align: center;
    text-decoration: none;
    display: flex;
    min-width: 20px;

    font-size: 20px;
    border-radius: 12px;

    
  }

#nav :hover {
      background-color: #b0a8be;
    /* color: #1D1E1F; */
    color: #131a05;
}

#nav .router-link-exact-active {
  /* background-color: #FFAB00; */
  color: #b0a8be;
  background-color: #37225a;
}


</style>

