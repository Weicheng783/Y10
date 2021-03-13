<template>
    <div>
       <div id="navigation">

        <b-nav tabs>
            <img style="width:200px;height:auto;padding: 0px 20px;position:relative;top:10px; float:left; margin-top:20px; margin-left:25px;" src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
                alt="Screenshot-2021-03-01-at-22-22-49" border="0">
            <router-link to="/" >Home</router-link>
            <router-link to="/login" >Login</router-link> 
            <router-link to="/register" >Create Account</router-link>
        </b-nav>

      </div>
 
        <p>The people you follow go here</p>
        <div v-for="person in persons" :key="person.name" class="FollowingBlock">
            <div style="display: flex; padding: 10px;">
                <img v-bind:src=person.portraitPath style="max-width: 150px; border-radius: 150px;"/>
                <div style="margin-left: 20px; margin-top: 20px;">
                    <p class="title is-2" style="color: white; margin-bottom: 0px;">{{person.name}}</p>
                    <p style="color:gray; font-size:22px;">{{person.smallText}}</p>
                </div>
            </div>
            <div style="text-align:right; padding: 0px 20px 20px 0px;">
                <button class="button blueButton" style="margin-right: 10px;">View Profile</button>
                <button class="button unfollowButton">Unfollow</button>
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
                name: "Harry Johnson",
                portraitPath: "https://images.unsplash.com/photo-1586287011575-a23134f797f9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80",
                smallText: "You both like comedy movies!",
            },
            {
                name: "Oliver Smith",
                portraitPath: "https://images.unsplash.com/photo-1582556362337-6a785ee99c63?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80",
                smallText: "Watched 15 similar movies!",
            }
        ],
    }
  },
}
</script>

<style scoped>
.FollowingBlock {
    text-align:left;
    margin: auto;
    flex-direction: column;
    background-color:#262728;
    border-radius: 25px;
    margin-bottom: 30px;
    max-width: 800px;
    color:white;
}
.blueButton {
    background-color: rgb(59, 167, 238);
    border-color: rgb(59, 167, 238);
}

.blueButton:hover {
    background-color: rgb(43, 137, 199);
    border-color: rgb(43, 137, 199);
}

.unfollowButton {
    background-color: #FF5338;
    border-color: #FF5338;
}

.unfollowButton:hover {
    background-color: #cf3821;
    border-color: #cf3821;
}
</style>