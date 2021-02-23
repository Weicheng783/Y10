<template>
    <div>
        <div id="navigation">
            <router-link to="/feed">Feed</router-link> |
            <router-link to="/watchlist">Watch List</router-link> |
            <router-link to="/following">Following</router-link> |
            <router-link to="/recommended">Recommended</router-link>
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
