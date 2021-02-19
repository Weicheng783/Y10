<template>
  <div>
    <div id="navigation">
      <router-link to="/feed">Feed</router-link> |
      <router-link to="/watchlist">Watch List</router-link> |
      <router-link to="/following">Following</router-link> |
      <router-link to="/recommended">Recommended</router-link>
    </div>
    <button @click="$emit('logOut')" >Logout</button>

    <div v-for="review in reviews" :key="review.authorName">
      <div>
        {{review.authorName}}
      </div>

      <div>
        <div>
          <img v-bind:src=" 'https://' + review.moviePoster" width="150px">
        </div>

        <div>
          <h1>
            {{review.movieName}}
          </h1>
          <p>
            {{review.reviewContent}}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

import axios from 'axios'

export default {
  name: 'Feed',
  data() {
    return {
        reviews: [
          {
            authorName: 'Rosabel Gladwyn',
            moviePoster: 'encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
            movieName: 'Bloodshot',
            reviewContent: 'Enjoyed the movie. Watched it with full attention!',
            rating: 5,
          },
        ],
    }
  },
  methods: {

  },
  mounted() {
    // call refresh token
    // if error call logout
    var objectToken = localStorage.getItem('jwt');
    var currentToken = JSON.parse( objectToken );
    console.log(currentToken);

    axios.post('http://localhost:8000/api/token/refresh/', {
      refresh: currentToken.refresh
    }).catch(function() {
      this.$emit('logOut');
    });
  }
}
</script>

<style scoped>

</style>