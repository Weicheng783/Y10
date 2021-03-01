<template>
    <div>
      <div id="navigation">
        <router-link to="/feed">Feed</router-link> |
        <router-link to="/watchlist">Watch List</router-link> |
        <router-link to="/following">Following</router-link> |
        <router-link to="/recommended">Recommended</router-link>
      </div>

      <p class="title is-2" style="color:white; margin: 60px;">Your private Cultime watchlist</p>

      <!-- Needs to be stylized and it is not working -->
      <autocomplete :search="search" style="max-width: 450px; margin: auto; padding-bottom: 60px;" defaultValue="Add new movies"></autocomplete>

      <div v-for="movie in watchList" :key="movie.movieTitle" class="movieBlock">
        <div style="display:flex; padding-left: 20px; padding-top: 20px;">
          <div>
            <img style="border-radius:20px;" v-bind:src=" 'https://' + movie.moviePoster">
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
          <button class="button" id="removeMovieButton">Remove Movie</button>
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
        ]
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
        let movies = [];
        for(let i=0;i<data.data.length;i++) {
          movies.push(data.data[i]['title'] + " (" + data.data[i]['release_date'] + ")");
        }
        return movies;
      })
    }
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

/* SEARCH BAR CSS */

.autocomplete-input {
  border: 1px solid #eee;
  border-radius: 8px;
  width: 100%;
  padding: 12px 12px 12px 48px;
  box-sizing: border-box;
  position: relative;
  font-size: 16px;
  line-height: 1.5;
  flex: 1;
  background-color: rgb(122, 117, 117);
  background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjNjY2IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGNpcmNsZSBjeD0iMTEiIGN5PSIxMSIgcj0iOCIvPjxwYXRoIGQ9Ik0yMSAyMWwtNC00Ii8+PC9zdmc+');
  background-repeat: no-repeat;
  background-position: 12px center;
}

.autocomplete-input:focus,
.autocomplete-input[aria-expanded="true"] {
  border-color: rgba(0, 0, 0, 0.12);
  background-color: rgba(126, 122, 122, 0.12);
  outline: none;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.16);
}

[data-position="below"] .autocomplete-input[aria-expanded="true"] {
  border-bottom-color: transparent;
  border-radius: 8px 8px 0 0;
  background-color: rgba(87, 87, 87, 0.12);
}

[data-position="above"] .autocomplete-input[aria-expanded="true"] {
  border-top-color: transparent;
  border-radius: 0 0 8px 8px;
  background-color: rgba(92, 89, 89, 0.12);
  z-index: 2;
}

/* Loading spinner */
.autocomplete[data-loading="true"]::after {
  content: "";
  border: 3px solid rgba(0, 0, 0, 0.12);
  border-right: 3px solid rgba(0, 0, 0, 0.48);
  border-radius: 100%;
  width: 20px;
  height: 20px;
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  animation: rotate 1s infinite linear;
  background-color: rgba(116, 112, 112, 0.12);
}

.autocomplete-result-list {
  margin: 0;
  border: 1px solid rgba(0, 0, 0, 0.12);
  padding: 0;
  box-sizing: border-box;
  max-height: 296px;
  overflow-y: auto;
  background: rgb(66, 66, 66);
  list-style: none;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.16);
}

[data-position="below"] .autocomplete-result-list {
  margin-top: -1px;
  border-top-color: transparent;
  border-radius: 0 0 8px 8px;
  padding-bottom: 8px;
}

[data-position="above"] .autocomplete-result-list {
  margin-bottom: -1px;
  border-bottom-color: transparent;
  border-radius: 8px 8px 0 0;
  padding-top: 8px;
}

/* Single result item */
.autocomplete-result {
  cursor: default;
  padding: 12px 12px 12px 48px;
  background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjY2NjIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGNpcmNsZSBjeD0iMTEiIGN5PSIxMSIgcj0iOCIvPjxwYXRoIGQ9Ik0yMSAyMWwtNC00Ii8+PC9zdmc+');
  background-repeat: no-repeat;
  background-position: 12px center;
}

.autocomplete-result:hover,
.autocomplete-result[aria-selected="true"] {
  background-color: rgba(99, 93, 93, 0.06);
}

@keyframes rotate {
  from {
    transform: translateY(-50%) rotate(0deg);
  }
  to {
    transform: translateY(-50%) rotate(359deg);
  }
}

</style>