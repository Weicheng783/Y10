<template>
  <div>
    <div id="navigation" style="margin-bottom: 100px;">
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

    <div v-for="movie in reviewStack" :key="movie" class="reviewBlock">
      <p class="title is-5" id="white-text" style="padding: 10px 0px 10px 25px;">Review for {{movie}} added!</p>
    </div>

    <div class="reviewBlock" style="padding: 25px;">
      <p class="title is-3" style="color:white;">Share new review</p>

      <p class="title is-5" id="white-text" style="margin-bottom: 0px; padding-bottom: 10px; padding-top: 10px;">Select the movie</p>
      <autocomplete 
        @submit="updateCurrentReview" 
        :search="search" 
        style="max-width: 450px; padding-bottom: 30px;" 
      ></autocomplete>

      <div>
          <p id="white-text" class="title is-5" style="margin-bottom: 0px; padding-bottom: 10px;">What are your thoughts on this movie</p>
          <textarea id="reviewcontent" v-model="newReviewContent" class="input" style="margin-bottom: 15px; min-height:100px; max-width:550px; border:none; color:white;"></textarea>
      </div>

      <p id="white-text" class="title is-5" style="margin-bottom: 0px; padding-bottom: 5px; padding-top: 15px">Rate this movie</p>
      <div>
        <div class="rate" style="display: inline-block;">
          <input type="radio" id="star5" v-model="newReviewRating" name="rate" value="5" />
          <label for="star5" title="text">5 stars</label>
          <input type="radio" id="star4" v-model="newReviewRating" name="rate" value="4" />
          <label for="star4" title="text">4 stars</label>
          <input type="radio" id="star3" v-model="newReviewRating" name="rate" value="3" />
          <label for="star3" title="text">3 stars</label>
          <input type="radio" id="star2" v-model="newReviewRating" name="rate" value="2" />
          <label for="star2" title="text">2 stars</label>
          <input type="radio" id="star1" v-model="newReviewRating" name="rate" value="1" />
          <label for="star1" title="text">1 star</label>
        </div>
      </div>

      <div style="padding-top: 20px;">         
          <div style="display: flex; align-items: center; height: 30px;"> 
            <input type="radio" id="public" name="is_private" v-model="newIsPrivate" value="false" checked>
            <label for="public" style="padding-bottom: 0px; padding-left: 10px;">Share Publicly 📢</label>
          </div>
          <div style="display: flex; align-items: center; height: 30px;"> 
            <input type="radio" id="private" name="is_private" v-model="newIsPrivate" value="true">
            <label for="private" style="padding-bottom: 0px; padding-left: 10px;">Save Privately 🔒</label>
          </div>
      </div>

      <div>
          <button @click="shareNewReview" class="button" style="margin-top: 10px; margin-bottom:15px;">Share Review</button>
      </div>
    </div>

    <div v-for="review in reviews" :key="review.authorName" class="reviewBlock">
      <div style="margin: 0px; padding:15px; text-align:left; display:flex; align-items:center;">
        <img v-bind:src=review.profilePicture style="width:75px; height:75px; border-radius: 75px;"/>
        <p style="font-size: 20px; color:white; margin-left: 10px;">{{review.authorName}} watched <b>{{review.movieName}}</b></p>
      </div>

      <div style="display:flex; padding: 0px 0px 0px 15px;">
        <div>
          <img style="border-radius:20px; max-width: 200px;" v-bind:src=" 'https://' + review.moviePoster">
        </div>

        <div style="padding-left: 20px;">
          <p style="padding-bottom: 10px; max-width: 500px;">
            {{review.reviewContent}}
          </p>

          <div v-for="n in review.rating" :key="n" style="display:inline-block;">
              <img alt="Yellow star" src="https://upload.wikimedia.org/wikipedia/commons/4/44/Plain_Yellow_Star.png" width="35px;">
          </div>

          <div style="max-width:500px; padding-top:20px;">
            <p style="color:gray; font-size:15px;">{{review.movieOverview}}</p>
          </div>
        </div>
      </div>

      <div style="text-align:right; padding: 20px;">
        <button class="button" @click="addNewMovie(review.movieId)">Watch Later</button>
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
        nextMovieName: "",
        newReviewContent: "",
        newReviewRating: -1,
        newIsPrivate: false,
        reviewStack: [],
    }
  },
  methods: {
    addNewMovie(result) {
      var objectToken = localStorage.getItem('jwt');
      var currentToken = JSON.parse( objectToken );

      axios.post('http://localhost:8000/watchlist/',{movie_id: result}, {
          headers: {
              'authorization': 'Bearer ' + currentToken.access,
              'Accept' : 'application/json',
              'Content-Type': 'application/json'
          }
      }).then(() => {});
    },
    shareNewReview() {
      if(this.nextMovie == -1 || this.newReviewContent.length == 0 || this.newReviewRating == -1) {
        return;
      }
      this.newIsPrivate = Boolean(this.newIsPrivate);
      console.log("AA");
      var objectToken = localStorage.getItem('jwt');
      var currentToken = JSON.parse( objectToken );
      axios.post('http://localhost:8000/reviews/',{
          movie_id: this.nextMovie,
          content: this.newReviewContent,
          rating: this.newReviewRating,
          is_private: this.newIsPrivate,
        }, {
        headers: {
          'authorization': 'Bearer ' + currentToken.access,
          'Accept' : 'application/json',
          'Content-Type': 'application/json'
        }
      }).then(() => {this.reviewStack.push(this.nextMovieName);});
    },
    updateCurrentReview(result) {
      for(let i=0;i<this.movieSearchQueue.length;i++) {
        if(result == this.movieSearchQueue[i]['title']) {
          this.nextMovie = this.movieSearchQueue[i]['movieId'];
          this.nextMovieName = this.movieSearchQueue[i]['title'];
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
                movieId: (data.data[i]['movie__movie_id']),
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
    axios.post('http://localhost:8000/refresh/', {
            refresh: currentToken.refresh
        }, {
        headers: {
            'Accept' : 'application/json',
            'Content-Type': 'application/json',
        }
    }).catch(data => {
        console.log(data);
        this.$emit('logOut');
    }).then(response => {
      let newToken = {
          refresh: currentToken.refresh,
          access: response.data.access,
      }
      localStorage.setItem('jwt', JSON.stringify(newToken));

      objectToken = localStorage.getItem('jwt');
      currentToken = JSON.parse( objectToken );

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
                movieId: (data.data[i]['movie__movie_id']),
              }
            );
          }
          console.log(this.reviews);
        }
      );
    });
  }
}
</script>

<style scoped>
h1, div {
  color:white;
}

.reviewBlock {
  display:flex; 
  /* padding-left: 25px; */
  /* padding-top: 25px; */
  /* padding-bottom: 20px; */
  text-align:left;
  margin: auto;
  flex-direction: column;
  background-color:#262728;
  border-radius: 25px;
  margin-bottom: 30px;
  max-width: 800px;
  color:white;
}

#reviewcontent {
  background-color: #353535;
}

#reviewcontent:hover, #reviecontent:focus {
  background-color: #383838;
}

label:hover {
  color: #fdab01;
}

</style>