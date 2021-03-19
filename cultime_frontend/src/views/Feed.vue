<template>
  <div>
    <div id="navigation">
       <b-nav tabs>
          <a href="" style="background-color: #201c1c; width:200px;height:auto;padding: 0px 20px;position:relative;top:10px; float:left; margin-top:20px; margin-left:25px;"><img style=" " src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
                alt="--Cultime--"  border="0"></a>
      <router-link to="/feed">Feed</router-link> |
      <router-link to="/watchlist">Watch List</router-link> |
      <router-link to="/following">Following</router-link> |
      <router-link to="/recommended">Recommended</router-link> |
      <router-link to="/profile">Profile</router-link>
      <button @click="$emit('logOut')" id='logout_button' style='color:#fe5e73 ;background-color:#4267B2;'>Logout</button>
        </b-nav>

    </div>  
    

    <div class="reviewBlock">
      <p class="title is-3" style="color:white;">Share new review</p>

      <autocomplete @submit="updateCurrentReview" :search="search" style="max-width: 450px; margin: auto; padding-bottom: 60px;" defaultValue="Add new movies"></autocomplete>

      <p>What are your thoughts on this movie</p>
      <input v-model="newReviewContent" class="input" style="max-width:300px;"/>

      <p>Rate it on scale 1-5</p>
      <input v-model="newReviewRating" class="input" style="max-width:300px;" type="number" />

      <button @click="shareNewReview" class="button">Share Review</button>
    </div>

    <div v-for="review in reviews" :key="review.authorName" class="reviewBlock">
      <div style="margin: 0px; padding:15px; text-align:left; display:flex; align-items:center;">
        <img v-bind:src=review.profilePicture style="width:75px; border-radius: 75px;"/>
        <p style="font-size: 20px; color:white; margin-left: 10px;">{{review.authorName}} watched <b>{{review.movieName}}</b></p>
      </div>

      <div style="display:flex; padding: 0px 0px 0px 15px;">
        <div>
          <img style="border-radius:20px;" v-bind:src=" 'https://' + review.moviePoster" width="150px">
        </div>

        <div style="padding-left: 20px;">
          <p style="padding-bottom: 10px;">
            {{review.reviewContent}}
          </p>

          <div v-for="n in review.rating" :key="n" style="display:inline-block;">
              <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Plain_Yellow_Star.png" width="35px;">
          </div>

          <div style="max-width:500px; padding-top:20px;">
            <p style="color:gray; font-size:15px;">{{review.movieOverview}}</p>
          </div>
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
        nextMovie: -1,
        newReviewContent: "",
        newReviewRating: -1,
    }
  },
  methods: {
    shareNewReview() {
      if(this.nextMovie == -1 || this.newReviewContent.length == 0 || this.newReviewRating == -1) {
        return;
      }
      var objectToken = localStorage.getItem('jwt');
      var currentToken = JSON.parse( objectToken );
      axios.post('http://localhost:8000/reviews/',{
          movie_id: this.nextMovie,
          content: this.newReviewContent,
          rating: this.newReviewRating
        }, {
        headers: {
          'authorization': 'Bearer ' + currentToken.access,
          'Accept' : 'application/json',
          'Content-Type': 'application/json'
        }
      }).then(() => {console.log("A")});
    },
    updateCurrentReview(result) {
      for(let i=0;i<this.movieSearchQueue.length;i++) {
        if(result == this.movieSearchQueue[i]['title']) {
          this.nextMovie = this.movieSearchQueue[i]['movieId'];
          console.log(this.nextMovie);
          break;
        }
      }
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
          this.movieSearchQueue.push({
            movieId: data.data[i]['id'],
            title: data.data[i]['title'] + " (" + data.data[i]['release_date'] + ")",
          });
          movies.push(data.data[i]['title'] + " (" + data.data[i]['release_date'] + ")");
        }
        return movies;
      })
    },
    updateReviews() {
      var objectToken = localStorage.getItem('jwt');
      var currentToken = JSON.parse( objectToken );
      axios.get('http://localhost:8000/reviews/', {
        headers: {
          Authorization: "Bearer " + currentToken.access
        }
      }).then(data => {
          this.reviews = [];
          for(let i=0;i<data.data.length;i++) {
            let currentPoster = data.data[i]['author__additionaluser__profile_picture'];
            if(currentPoster == null) {
              currentPoster = "https://images.unsplash.com/photo-1615105113716-63952cd0cba8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80";
            } 
            else {
              currentPoster = 'http://localhost:8000/' + currentPoster.substring(9, currentPoster.length);
            }

            this.reviews.push(
              {
                authorName: (data.data[i]['author__first_name'] + ' ' + data.data[i]['author__last_name']),
                movieName: (data.data[i]['movie__movie_name']),
                reviewContent: (data.data[i]['content']),
                rating: (data.data[i]['rating']),
                moviePoster: ('image.tmdb.org/t/p/w500' + data.data[i]['movie__poster_path']),
                movieOverview: (data.data[i]['movie__overview']),
                profilePicture: currentPoster,
              }
            );
          }
        }
      );
    }
  },
  mounted() {
    // call refresh token
    // if error call logout
    var objectToken = localStorage.getItem('jwt');
    var currentToken = JSON.parse( objectToken );

    axios.get('http://localhost:8000/reviews/', {
        headers: {
          Authorization: "Bearer " + currentToken.access
        }
      }).then(data => {
          this.reviews = [];
          for(let i=0;i<data.data.length;i++) {
            let currentPoster = data.data[i]['author__additionaluser__profile_picture'];
            if(currentPoster == null) {
              currentPoster = "https://images.unsplash.com/photo-1615105113716-63952cd0cba8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80";
            } 
            else {
              currentPoster = 'http://localhost:8000/' + currentPoster.substring(9, currentPoster.length);
            }

            this.reviews.push(
              {
                authorName: (data.data[i]['author__first_name'] + ' ' + data.data[i]['author__last_name']),
                movieName: (data.data[i]['movie__movie_name']),
                reviewContent: (data.data[i]['content']),
                rating: (data.data[i]['rating']),
                moviePoster: ('image.tmdb.org/t/p/w500' + data.data[i]['movie__poster_path']),
                movieOverview: (data.data[i]['movie__overview']),
                profilePicture: currentPoster,
              }
            );
          }
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



#logout_button {
  font-weight: bold;
  display: inline-flex;
  /* float: right; */
  /* margin-right:10%; */

  margin-left:50px;

  appearance: button;

    border: none;
    background-color: #230a59;
    border-color: lawngreen;

    color: #007acc;
    padding: 20px 10px 10px 10px;
    /* margin: 30px 30px 20px 20px;  */
    margin-right:10px;
    margin-top:10px;
    /* padding-right: 10px; */
    text-align: center;
    text-decoration: none;
    display: inline-block;
    min-width: 20px;

    font-size: 20px;
    border-radius: 20px;
     
}


#logout_button :hover {
    background-color: #b0a8be;
    /* color: #1D1E1F; */
    color: #1a57b3;
}

/* #logout_button router-link-exact-active {
  background-color: #FFAB00;
  color: #1D1E1F;
} */
</style>