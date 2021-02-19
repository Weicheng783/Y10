<template>
    <div>
        <div id="navigation">
            <router-link to="/feed">Feed</router-link> |
            <router-link to="/watchlist">Watch List</router-link> |
            <router-link to="/following">Following</router-link> |
            <router-link to="/recommended">Recommended</router-link>
        </div>
        <p>Recommended people go here</p>
        <p v-for="person in persons" :key="person.first_name" >{{person.first_name}} {{person.last_name}}</p>
    </div>
</template>

<script>
export default {
  name: 'Recommended',
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
