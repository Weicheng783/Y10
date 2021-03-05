<template>
    <div>
        <div id="navigation">
            <router-link to="/feed">Feed</router-link> |
            <router-link to="/watchlist">Watch List</router-link> |
            <router-link to="/following">Following</router-link> |
            <router-link to="/recommended">Recommended</router-link>
        </div>
        <p>Recommended people go here</p>
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
                <button class="button followButton">Follow</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Recommended',
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

.followButton {
  background-color: #FFA72B;
  border-color: #FFA72B;
}

.followButton:hover {
  background-color: #c7801e;
  border-color: #c7801e;
}
</style>