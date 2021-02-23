<template>
  <div>
    <div id="navigation">
      <router-link to="/feed">Feed</router-link> |
      <router-link to="/watchlist">Watch List</router-link> |
      <router-link to="/following">Following</router-link> |
      <router-link to="/recommended">Recommended</router-link> |
      <router-link to="/profile">Profile</router-link>
    </div>
    <button @click="$emit('logOut')" >Logout</button>

    <div v-for="review in reviews" :key="review.authorName" class="reviewBlock">
      <div class="title is-4" style="margin: 30px 0px 30px 20px; text-align:left;">
        {{review.authorName}}
      </div>

      <div style="display:flex; padding-left: 20px;">
        <div>
          <img style="border-radius:20px;" v-bind:src=" 'https://' + review.moviePoster" width="150px">
        </div>

        <div>
          <h1 style="padding-left: 20px;" class="title is-3">
            {{review.movieName}}
          </h1>
          <p style="padding-left: 20px; padding-bottom: 20px;">
            {{review.reviewContent}}
          </p>
        </div>
      </div>

      <div style="text-align:right; padding: 20px;">
        <button class="button">Watch Later</button>
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
          {
            authorName: 'Weicheng Ao',
            moviePoster: 'encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
            movieName: 'Home Alone',
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
h1, div {
  color:white;
}

.reviewBlock {
  /* display:flex;  */
  text-align:left;
  margin: auto;
  flex-direction: column;
  background-color:#262728;
  border-radius: 25px;
  margin-bottom: 30px;
  max-width: 800px;
  color:white;
}
</style>