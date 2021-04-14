<template>
    <div>
      <div id="navigation">
        <a href="/feed" style="background-color: #201c1c; width:200px;height:auto;padding: 0px 20px;position:relative;top:10px; float:left; margin-top:20px; margin-left:25px;"><img style=" " src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
                alt="--Cultime--"  border="0"></a>
        <router-link to="/feed">Feed</router-link>
        <router-link to="/watchlist">Watch List</router-link>
        <router-link to="/following">Following</router-link>
        <router-link to="/recommended">Recommended</router-link>
        <router-link to="/profile">Profile</router-link>
        <router-link to="/trending">Trending</router-link>
        <button @click="$emit('logOut')" id='logout_button' style='color:#fe5e73 ;background-color:#4267B2;'>Logout</button>
      </div>

      <p class="title is-2" style="color:white; margin: 60px;">Your private Cultime watchlist</p>

      <autocomplete @submit="addNewMovie" :search="search" style="max-width: 450px; margin: auto; padding-bottom: 60px;"></autocomplete>

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
          <button class="button" id="removeMovieButton" @click="removeMovie(movie.id)">Remove Movie</button>
        </div>

        <div v-show="movie.show" style="padding-left: 20px; display: flex; flex-direction: column;">
          <div>
              <p id="white-text" class="title is-5" style="margin-bottom: 0px; padding-bottom: 10px;">What are your thoughts on this movie</p>
              <textarea id="reviewcontent" v-model="movie.newReviewContent" class="input" style="margin-bottom: 15px; min-height:100px; max-width:550px; border:none; color:white;"></textarea>
          </div>

          <p id="white-text" class="title is-5" style="margin-bottom: 0px; padding-bottom: 5px; padding-top: 15px">Rate this movie</p>
          <form>
            <div class="rate" style="display: inline-block;">
              <input style="visibility: hidden;" type="radio" :id="`star5-rating-${movie.id}`" v-model="movie.newReviewRating" :name="`rating-${movie.id}`"    value="5" />
              <label :for="`star5-rating-${movie.id}`" title="text">5 stars</label>
              <input style="visibility: hidden;" type="radio" :id="`star4-rating-${movie.id}`" v-model="movie.newReviewRating" :name="`rating-${movie.id}`"  value="4" />
              <label :for="`star4-rating-${movie.id}`" title="text">4 stars</label>
              <input style="visibility: hidden;" type="radio" :id="`star3-rating-${movie.id}`" v-model="movie.newReviewRating" :name="`rating-${movie.id}`"  value="3" />
              <label :for="`star3-rating-${movie.id}`" title="text">3 stars</label>
              <input style="visibility: hidden;" type="radio" :id="`star2-rating-${movie.id}`" v-model="movie.newReviewRating" :name="`rating-${movie.id}`"  value="2" />
              <label :for="`star2-rating-${movie.id}`" title="text">2 stars</label>
              <input style="visibility: hidden;" type="radio" :id="`star1-rating-${movie.id}`" v-model="movie.newReviewRating" :name="`rating-${movie.id}`" value="1" />
              <label :for="`star1-rating-${movie.id}`" title="text">1 star</label>
            </div>
          </form>

          <form>
            <div style="padding-top: 20px;">         
                <div style="display: flex; align-items: center; height: 30px;"> 
                  <input type="radio" id="public" name="is_private" v-model="movie.newIsPrivate" value="false" checked>
                  <label for="public" style="padding-bottom: 0px; padding-left: 10px;">Share Publicly 📢</label>
                </div>
                <div style="display: flex; align-items: center; height: 30px;"> 
                  <input type="radio" id="private" name="is_private" v-model="movie.newIsPrivate" value="true">
                  <label for="private" style="padding-bottom: 0px; padding-left: 10px;">Save Privately 🔒</label>
                </div>
            </div>
          </form>

          <div>
            <button @click="shareNewReview" class="button" style="margin-top: 10px; margin-bottom:15px;">Share Review</button>
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
        newReviewRating: 0,
        newReviewContent: null,
    }
  },
  methods: {
    shareNewReview(){
      console.log("TO DO");
    },
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
                newReviewRating: 0,
                newIsPrivate: false,
                newReviewContent: "",
                show: false,
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
    axios.post('http://localhost:8000/refresh/', {
            refresh: currentToken.refresh
        }, {
        headers: {
            'Accept' : 'application/json',
            'Content-Type': 'application/json',
        }
    }).catch(() => {
        this.$emit('logOut');
    }).then(response => {
      let newToken = {
          refresh: currentToken.refresh,
          access: response.data.access,
      }
      localStorage.setItem('jwt', JSON.stringify(newToken));

      objectToken = localStorage.getItem('jwt');
      currentToken = JSON.parse( objectToken );
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
                newReviewRating: 0,
                newIsPrivate: false,
                newReviewContent: "",
                show: false,
              });
            }
            this.watchList = this.watchList.reverse();
          }
        );
    });
  }
}
</script>

<style>
h1, div, p {
  color:white;
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

/* MOVIE STAR RATING */

*{
    margin: 0;
    padding: 0;
}
.rate {
    float: left;
    height: 46px;
    padding: 0px;
}
.rate:not(:checked) > input {
    position:absolute;
    top:-9999px;
}
.rate:not(:checked) > label {
    float:right;
    width:1em;
    overflow:hidden;
    white-space:nowrap;
    cursor:pointer;
    font-size:30px;
    color:#ccc;
}
.rate:not(:checked) > label:before {
    content: '★ ';
}
.rate > input:checked ~ label {
    color: #ffc700;    
}
.rate:not(:checked) > label:hover,
.rate:not(:checked) > label:hover ~ label {
    color: #deb217;  
}
.rate > input:checked + label:hover,
.rate > input:checked + label:hover ~ label,
.rate > input:checked ~ label:hover,
.rate > input:checked ~ label:hover ~ label,
.rate > label:hover ~ input:checked ~ label {
    color: #c59b08;
}

</style>