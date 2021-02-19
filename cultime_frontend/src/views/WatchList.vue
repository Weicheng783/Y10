<template>
    <div>
        <div id="navigation">
          <router-link to="/feed">Feed</router-link> |
          <router-link to="/watchlist">Watch List</router-link> |
          <router-link to="/following">Following</router-link> |
          <router-link to="/recommended">Recommended</router-link>
      </div>
      <p>Watchlist</p>
    </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'WatchList',
  data() {
    return {
        movieTitle: "Parasite",
    }
  },
}
</script>
