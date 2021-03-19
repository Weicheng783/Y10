<template>
    <div>
        <button>Trending now</button>
        <button>Personal Recommendations</button>

        <div v-for="movie in trendingMovies" :key="movie.movieId" class="movieBlock">
            <div style="display:flex; padding-left: 20px; padding-top: 20px;">
            <div>
                <img style="border-radius:20px; max-width:200px;" v-bind:src=" 'https://image.tmdb.org/t/p/w500/' + movie.moviePoster">
            </div>

            <div style="padding-left: 20px; padding-bottom: 20px;">
                <h1 style="color:white; margin:0px;" class="title is-3">
                {{movie.movieTitle}}
                </h1>
                <p style="max-width: 450px; color:gray;">
                {{movie.yearProduction}} ·
                {{movie.genres}}
                </p>
                <p style="margin-bottom: 20px; margin-top: 20px; max-width: 450px;">
                {{movie.shortSummary}}
                </p>

                <div v-for="n in movie.rating" :key="n" style="display:inline-block;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Plain_Yellow_Star.png" width="35px;">
                </div>
            </div>
            </div>

            <!-- <div style="text-align:right; padding: 0px 20px 20px 0px;">
            <button v-if="!movie.show" class="button" @click="movie.show=!movie.show">Share Review</button>
            <button v-else-if="movie.show" class="button" id="cancelReviewButton" @click="movie.show=!movie.show">Cancel Review</button>
            
            <button class="button" id="removeMovieButton" v-on:click="removeMovie(movie.indexId)">Remove Movie</button>
            </div>

            <div v-show="movie.show" style="padding-left: 20px;">
            <div>
                <p style="padding-bottom: 5px;">What are your thoughts on this movie</p>
                <textarea id="reviewcontent" v-model="newReviewContent" class="input" style="margin-bottom: 15px; min-height:100px; max-width:550px; border:none; color:white;"></textarea>
            </div>

            <p>Rate it on scale 1-5</p>
            <div>
                <div class="rate" style="display:inline-block;">
                <input type="radio" id="star5" v-model="newReviewRating" value="5" />
                <label for="star5" title="text">5 stars</label>
                <input type="radio" id="star4" v-model="newReviewRating" value="4" />
                <label for="star4" title="text">4 stars</label>
                <input type="radio" id="star3" v-model="newReviewRating" value="3" />
                <label for="star3" title="text">3 stars</label>
                <input type="radio" id="star2" v-model="newReviewRating" value="2" />
                <label for="star2" title="text">2 stars</label>
                <input type="radio" id="star1" v-model="newReviewRating" value="1" />
                <label for="star1" title="text">1 star</label>
                </div>
            </div> -->

            <!-- <div>
                <button @click="shareNewReview" class="button" style="margin-top: 10px; margin-bottom:15px;">Share Review</button>
            </div> -->
            <!-- </div> -->
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Trending',
    data() {
        return {
            trendingMovies: [
            {
                indexId: 0,
                movieId: 771,
                movieTitle: "Home Alone",
                rating: 5,
                yearProduction: 2000,
                shortSummary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                moviePoster: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
            },
            {
                indexId: 1,
                movieTitle: "Home Alone 3",
                rating: 4,
                yearProduction: 2002,
                shortSummary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                moviePoster: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
            },
            ],
            genres: [
                {
                id: 28,
                name: "Action"
                },
                {
                id: 12,
                name: "Adventure"
                },
                {
                id: 16,
                name: "Animation"
                },
                {
                id: 35,
                name: "Comedy"
                },
                {
                id: 80,
                name: "Crime"
                },
                {
                id: 99,
                name: "Documentary"
                },
                {
                id: 18,
                name: "Drama"
                },
                {
                id: 10751,
                name: "Family"
                },
                {
                id: 14,
                name: "Fantasy"
                },
                {
                id: 36,
                name: "History"
                },
                {
                id: 27,
                name: "Horror"
                },
                {
                id: 10402,
                name: "Music"
                },
                {
                id: 9648,
                name: "Mystery"
                },
                {
                id: 10749,
                name: "Romance"
                },
                {
                id: 878,
                name: "Science Fiction"
                },
                {
                id: 10770,
                name: "TV Movie"
                },
                {
                id: 53,
                name: "Thriller"
                },
                {
                id: 10752,
                name: "War"
                },
                {
                id: 37,
                name: "Western"
                }
            ]
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
        }).catch(data => {
            console.log(data);
        }).then(response => {
            let newToken = {
                refresh: currentToken.refresh,
                access: response.data.access,
            }
            localStorage.setItem('jwt', JSON.stringify(newToken));

            axios.get('http://localhost:8000/trending/').then(data => {
                console.log(data.data);
            });
        });

        axios.get('http://localhost:8000/trending/').then(data => {
            this.trendingMovies = [];
            for(let i=0;i<data.data.length;i++) {
                console.log(data.data[i]);
                let allGenres = "";

                for(let j=0;j<data.data[i]['genres'].length;j++) {
                    for(let k=0;k<this.genres.length;k++) {
                        if(this.genres[k].id == data.data[i]['genres'][j]) {
                            allGenres += this.genres[k].name;
                        }
                    }

                    if(j < data.data[i]['genres'].length - 1) {
                        allGenres += ", ";
                    }
                } 

                this.trendingMovies.push(
                    {
                        movieTitle: data.data[i]['title'],
                        moviePoster: data.data[i]['poster_path'],
                        shortSummary: data.data[i]['overview'],
                        yearProduction: data.data[i]['release_date'],
                        genres: allGenres,
                    }
                );
            }
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
  max-width: 700px;
  color:white;
}

#removeMovieButton {
  background-color: #FFA72B;
  border-color: #FFA72B;
  margin-left: 15px;
}

#removeMovieButton:hover {
  background-color: #c7801e;
  border-color: #c7801e;
}

#reviewcontent {
  border:none;
  background-color:#333333;
  outline: none;
}

#reviewcontent:focus {
  border:none;
  background-color:#383838;
  outline: none;
}

#cancelReviewButton {
    background-color: #FF5338;
    border-color: #FF5338;
}

#cancelReviewButton:hover {
    background-color: #cf3821;
    border-color: #cf3821;
}
</style>