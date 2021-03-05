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

    <div class="reviewBlock">
      <p>Share new review</p>

      <autocomplete :search="search" style="max-width: 450px; margin: auto; padding-bottom: 60px;" defaultValue="Add new movies"></autocomplete>

      <p>What are your thoughts on this movie</p>
      <input class="input" style="max-width:300px;"/>

      <p>Rate it on scale 1-5</p>
      <input class="input" style="max-width:300px;" type="number" />
    </div>

    <div v-for="review in reviews" :key="review.authorName" class="reviewBlock">
      <div style="margin: 0px; padding:15px; text-align:left; display:flex; align-items:center;">
        <img v-bind:src=review.authorPicture style="width:75px; border-radius: 75px;"/>
        <p style="font-size: 20px; color:white; margin-left: 10px;">{{review.authorName}} watched <b>{{review.movieName}}</b></p>
      </div>

      <div style="display:flex; padding: 0px 0px 0px 15px;">
        <div>
          <img style="border-radius:20px;" v-bind:src=" 'https://' + review.moviePoster" width="150px">
        </div>

        <div>
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
            authorPicture: "https://images.unsplash.com/photo-1582556362337-6a785ee99c63?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80",
            moviePoster: 'encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
            movieName: 'Bloodshot',
            reviewContent: 'Enjoyed the movie. Watched it with full attention!',
            rating: 5,
          },
          {
            authorName: 'Weicheng Ao',
            authorPicture: "https://images.unsplash.com/photo-1586287011575-a23134f797f9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80",
            moviePoster: 'encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
            movieName: 'Home Alone',
            reviewContent: 'Enjoyed the movie. Watched it with full attention!',
            rating: 5,
          },
        ],
        movieSearchQueue: [

        ],
    }
  },
  methods: {
    search(input) {
      if(!(typeof input === 'string' || input instanceof String)) {return [];}
      if(input.length < 3) {return [];}
      return axios.post('http://localhost:8000/searchmovie/', {
        title: input
      }
      ).then( data => {
        this.movieSearchQueue = [];
        let movies = []
        for(let i=0;i<data.data.length;i++) {
          this.movieSearchQueue.push({movieId: data.data[i]['id'],title: data.data[i]['title'] + " (" + data.data[i]['release_date'] + ")"});
          movies.push(data.data[i]['title'] + " (" + data.data[i]['release_date'] + ")");
        }
        return movies;
      })
    },
  },
  mounted() {
    // call refresh token
    // if error call logout
    var objectToken = localStorage.getItem('jwt');
    var currentToken = JSON.parse( objectToken );
    console.log(currentToken);

    // axios.post('http://localhost:8000/api/token/refresh/', {
    //   refresh: currentToken.refresh
    // }).catch(function() {
    //   this.$emit('logOut');
    // });
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