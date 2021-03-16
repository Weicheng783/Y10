<template>
    <div>
     <div id="navigation">
       <b-nav tabs>
         
          <a href="" style="background-color: #201c1c; width:200px;height:auto;padding: 0px 20px;position:relative;top:10px; float:left; margin-top:20px; margin-left:25px;"><img style=" " src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
                alt="--Cultime--"  border="0"></a>
                <!-- animation-name: logo; animation-duration:6s; -->
         
     
      <router-link to="/feed" >Feed</router-link> |
      <router-link to="/watchlist" >Watch List</router-link> |
      <router-link to="/following" >Following</router-link> |
      <router-link to="/recommended" >Recommended</router-link> |
      <router-link to="/profile" >Profile</router-link>
  
      <button @click="$emit('logOut')" id='logout_button' style='color:#fe5e73 ;background-color:#4267B2;'>Logout</button>
        </b-nav>

      </div>  

      <p class="title is-2" style="color:white; margin: 60px; font-family:'Times New Roman', Times, serif;">Your private <img style="width:200px;height:auto;padding: 0px ; animation-name: navi_enter; animation-duration:2s; " src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
                alt="Cultime" border="0"> watchlist</p>

      <!-- Needs to be stylized and it is not working -->
      <autocomplete @submit="addNewMovie" :search="search" style="max-width: 450px; margin: auto; padding-bottom: 60px;" defaultValue="Add new movies"></autocomplete>

      <div v-for="movie in watchList" :key="movie.movieTitle" class="movieBlock">
        <div style="display:flex; padding-left: 20px; padding-top: 20px;">
          <div>
            <img style="border-radius:20px; max-width:200px;" v-bind:src=" 'https://image.tmdb.org/t/p/w500/' + movie.moviePoster">
          </div>

          <div style="padding-left: 20px; padding-bottom: 20px;">
            <h1 style="color:white; margin:0px;" class="title is-3">
              {{movie.movieTitle}}
            </h1>
            <p style="max-width: 450px; color:gray;">
              {{movie.yearProduction}}
            </p>
            <p style="margin-bottom: 20px; margin-top: 20px; max-width: 450px;">
              {{movie.shortSummary}}
            </p>

            <div v-for="n in movie.rating" :key="n" style="display:inline-block;">
              <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Plain_Yellow_Star.png" width="35px;">
            </div>
          </div>
        </div>

        <div style="text-align:right; padding: 0px 20px 20px 0px;">
          <button class="button" id="removeMovieButton" v-on:click="removeMovie(movie.id)">Remove Movie</button>
        </div>
      </div>
    </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

import axios from 'axios'

export default {
  name: 'WatchList',
  data() {
    return {
        watchList: [
          {
            movieId: 771,
            movieTitle: "Home Alone",
            rating: 5,
            yearProduction: 2000,
            shortSummary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            moviePoster: 'encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
          },
          {
            movieTitle: "Home Alone 3",
            rating: 4,
            yearProduction: 2002,
            shortSummary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            moviePoster: 'encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
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
    updateWatchList() {
      console.log("CALLED");
      var objectToken = localStorage.getItem('jwt');
      var currentToken = JSON.parse( objectToken );
      axios.get('http://localhost:8000/watchlist/', {
          headers: {
            Authorization: "Bearer " + currentToken.access
          }
        }).then(
          data => {
            this.watchList = [];
            for(let i=0;i<data.data.length;i++) {
              this.watchList.push({
                id: data.data[i]['movie']['id'],
                movieTitle: data.data[i]['movie']['movie_name'],
                shortSummary: data.data[i]['movie']['overview'],
                yearProduction: data.data[i]['movie']['production_year'],
                moviePoster: data.data[i]['movie']['poster_path'],
                rating: data.data[i]['movie']['rating'],
              });
            }
            this.watchList = this.watchList.reverse();
          }
        );
    },
    addNewMovie(result) {
      for(let i=0;i<this.movieSearchQueue.length;i++) {
        if(result == this.movieSearchQueue[i]['title']) {
          var objectToken = localStorage.getItem('jwt');
          var currentToken = JSON.parse( objectToken );
          console.log(currentToken.access);

          axios.post('http://localhost:8000/watchlist/',{movie_id: this.movieSearchQueue[i]['movieId']}, {
              headers: {
                  'authorization': 'Bearer ' + currentToken.access,
                  'Accept' : 'application/json',
                  'Content-Type': 'application/json'
              }
          }).then(() => {this.updateWatchList();});
        }
      }
    },
    removeMovie(inputIdIn) {
      var objectToken = localStorage.getItem('jwt');
      var currentToken = JSON.parse( objectToken );
      console.log(inputIdIn);
      axios.post('http://localhost:8000/deletewatchlist/', {id: inputIdIn}, {
          headers: {
            'authorization': 'Bearer ' + currentToken.access,
            'Accept' : 'application/json',
            'Content-Type': 'application/json'
          }
        }
      ).then(()=>{this.updateWatchList();});
    }
  },
  mounted() {
      var objectToken = localStorage.getItem('jwt');
      var currentToken = JSON.parse( objectToken );
      axios.get('http://localhost:8000/watchlist/', {
          headers: {
            Authorization: "Bearer " + currentToken.access
          }
        }).then(
          data => {
            this.watchList = [];
            for(let i=0;i<data.data.length;i++) {
              this.watchList.push({
                id: data.data[i]['movie']['id'],
                movieTitle: data.data[i]['movie']['movie_name'],
                shortSummary: data.data[i]['movie']['overview'],
                yearProduction: data.data[i]['movie']['production_year'],
                moviePoster: data.data[i]['movie']['poster_path'],
                rating: data.data[i]['movie']['rating'],
              });
            }
            this.watchList = this.watchList.reverse();
          }
        );
    // call refresh token
    // if error call logout

    axios.post('http://localhost:8000/refresh/', {
      refresh: currentToken.refresh
    }).catch(function() {
      this.$emit('logOut');
    }).then(response => {
      localStorage.setItem('jwt', JSON.stringify(response.data));
    });

  }
}
</script>

<style>
h1, div, p {
  color:white;
}

@keyframes navi_enter {
  0%   { width:50%; height:auto;}

  100% {width:200px; height:auto;}
}

.movieBlock {
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


#removeMovieButton {
  background-color: #FFA72B;
  border-color: #FFA72B;
}

#removeMovieButton:hover {
  background-color: #c7801e;
  border-color: #c7801e;
}



/* SEARCH BAR CSS */


</style>