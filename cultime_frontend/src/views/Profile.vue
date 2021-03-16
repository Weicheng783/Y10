<template>
    <div>
        <div id="navigation">
       <b-nav tabs>
          <a href="" style="background-color: #201c1c; width:200px;height:auto;padding: 0px 20px;position:relative;top:10px; float:left; margin-top:20px; margin-left:25px;"><img style=" " src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
                alt="--Cultime--"  border="0"></a>
      <router-link to="/feed">Feed</router-link> |
      <router-link to="/watchlist">Watch List</router-link> |
      <router-link to="/following">Following</router-link> |
      <router-link to="/recommended">Recommended</router-link> |
      <router-link to="/profile">Profile</router-link>
      <button @click="$emit('logOut')" id='logout_button' style='color:#fe5e73 ;background-color:#4267B2;'>Logout</button>
        </b-nav>

        </div>  
        <p>Profile Settings</p>

        <div class="avatar-change">
            <p>Change your avatar</p>
            <div>
                <img src="https://images.unsplash.com/photo-1552374196-c4e7ffc6e126?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80" style="width:100px; height:100px; border-radius:100px;">  
                <button class="button">Upload new</button>          
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Following',
  data() {
    return {
        persons: [
            {
                first_name: "A",
                last_name: "B",
            }
        ],
    }
  },
}
</script>

<style>
p {
    color:white;
}
</style>
