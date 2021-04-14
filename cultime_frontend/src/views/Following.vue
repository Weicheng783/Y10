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

        <div v-show="showModal"> 
        <div class="modal is-active">
            <div class="modal-background">
            </div>
            <div class="modal-content">
                <div class="show-details" >
                    <div style="item-align:bottom; width: 100%;">
                        <div class="image">
                            <img :src=chosenProfilePicture style="border-radius: 150px;"/>
                        </div>
                        <div>
                            <p class="name" style="color: white; margin-bottom: 0px;">{{chosenName}}</p>
                            <p class="bio" style="color:gray;">{{chosenBio}}</p>
                            <p class="title is-3" style="color: white; text-align:left;font-size:20px; padding-top: 50px;">Thier favourites</p>
                            <div style="display:flex; justify-content:space-evenly; align-items:center;">
                                <div v-for="fav in favourites" :key="fav.moviePoster" style="display: flex; flex-direction: column; max-width: 30%; align-items:center;">
                                    <img alt="Movie Poster" style="border-radius: 20px; margin-bottom: px;" v-bind:src=fav.moviePoster />
                                </div>
                            </div>
                            <p class="title is-3" style="color: white; text-align:left; padding-top: 50px;font-size:20px;">Their reviews</p>
                            <div v-for="review in reviews" :key="review.moviePoster" class="reviewBlock">
                                <div style="display: flex; align-items:center;">
                                    <img :src="review.moviePoster" style="margin: 15px 0px 15px 15px; max-width: 100px; border-radius:15px;"/>
                                    <div style="margin: 15px 0px 15px 15px;">
                                        <p class="title is-4" id="white-text" style="margin-bottom: 10px;">{{review.movieName}}</p>
                                        <p id="white-text" style="font-size: 18px; padding-bottom: 10px;">{{review.reviewContent}}</p>
                                            <div v-for="n in review.rating" :key="n" style="display:inline-block;">
                                                <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Plain_Yellow_Star.png" width="30px;">
                                            </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <button class="modal-close" @click="showModal=false;"></button> 
        </div>
        </div>

        <p class="title is-3" id="white-text" style="padding-bottom: 25px;">Your Cultime Squad!</p>

        <div v-for="person in persons" :key="person.name" class="FollowingBlock">
            <div style="display: flex; padding: 10px;">
                <img :src=person.portraitPath style="max-width: 150px; border-radius: 150px;"/>
                <div style="margin-left: 20px; margin-top: 20px;">
                    <p class="title is-2" style="color: white; margin-bottom: 0px;">{{person.name}}</p>
                    <p style="color:gray; font-size:22px;">{{person.smallText}}</p>
                </div>
            </div>
            <div style="text-align:right; padding: 0px 20px 20px 0px;">
                <button class="button blueButton" style="margin-right: 10px;" @click="showModal=true; fetchInfo(person.id)">View Profile</button>
                <button class="button unfollowButton" @click="unfollowUser(person.username)">Unfollow</button>
            </div>
        </div>
    </div>
</template>

<script>

//import modal from '@/components/modal.vue'
import axios from 'axios'

export default {
  name: 'Following',
  data() {
    return {
        persons: [
            {
                name: "Radu Johnson",
                portraitPath: "",
                smallText: "You both like comedy movies!",
            },
            {
                name: "Oliver Smith",
                portraitPath: "https://images.unsplash.com/photo-1582556362337-6a785ee99c63?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80",
                smallText: "Watched 15 similar movies!",
            }
        ],
        showModal: false,
            favourites: [
                {
                    moviePoster: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
                }
            ],
            reviews: [
                {
                    moviePoster: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
                    movieName: 'Bloodshot',
                    reviewContent: 'Enjoyed the movie. Watched it with full attention!',
                    rating: 5,
                },
                {
                    moviePoster: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
                    movieName: 'Home Alone',
                    reviewContent: 'Enjoyed the movie. Watched it with full attention!',
                    rating: 5,
                },
            ],
            chosenName: "",
            chosenBio: "",
            chosenProfilePicture: "",
    }
  },
  methods: {
    fetchInfo(id) {
        var objectToken = localStorage.getItem('jwt');
        var currentToken = JSON.parse( objectToken );
        axios.post('http://localhost:8000/profile_info/',{id: id}, {
            headers: {
                Authorization: "Bearer " + currentToken.access,
                'Accept' : 'application/json',
                'Content-Type': 'application/json',
            },
        }).then(response => {
            console.log(response.data);
            this.favourites = [];
            for(let i=0;i<response.data['favourites'].length;i++) {
                this.favourites.push({
                    moviePoster: "https://image.tmdb.org/t/p/w500/" + response.data['favourites'][i]['movie__poster_path'],
                });
            }

            this.reviews = [];
            for(let i=0;i<response.data['reviews'].length;i++) {
                this.reviews.push({
                    moviePoster: "https://image.tmdb.org/t/p/w500/" + response.data['reviews'][i]['movie__poster_path'],
                    movieName: response.data['reviews'][i]['movie__movie_name'],
                    reviewContent: response.data['reviews'][i]['content'],
                    rating: response.data['reviews'][i]['rating'],
                })
            }

            this.chosenName = response.data['info'][0]['user__first_name'] + " " + response.data['info'][0]['user__last_name'];
            this.chosenBio = response.data['info'][0]['user_bio'];
            let currentPicture = response.data['info'][0]['profile_picture']
            this.chosenProfilePicture = 'http://localhost:8000/' + currentPicture.substring(9, currentPicture.length);
        });
    },
    updateFollowers() {
        var objectToken = localStorage.getItem('jwt');
        var currentToken = JSON.parse( objectToken );
        axios.get('http://localhost:8000/following/', {
            headers: {
                Authorization: "Bearer " + currentToken.access
            }
        }).then(
            response => {
                console.log(response.data);
                this.persons = [];
                for(let i=0;i<response.data.length;i++) {

                    let currPortraitPath = "static/profile_pictures/default.png"
                    let currentPoster = response.data[i]['follower__additionaluser__profile_picture'];
                    if(currentPoster != null) {
                        currPortraitPath = currentPoster.substring(9, currentPoster.length);
                    }

                    this.persons.push({
                        id: response.data[i]['follower__id'],
                        name: response.data[i]['follower__first_name'] + " " + response.data[i]['follower__last_name'],
                        portraitPath: "http://localhost:8000/" + currPortraitPath,
                        username: response.data[i]['follower__username'],
                    })
                }
            }
        );
    },
    unfollowUser(username) {
        var objectToken = localStorage.getItem('jwt');
        var currentToken = JSON.parse( objectToken );
        console.log(username);
        axios.post('http://localhost:8000/unfollow/',{username: username}, {
            headers: {
                Authorization: "Bearer " + currentToken.access,
                'Accept' : 'application/json',
                'Content-Type': 'application/json',
            },
        }).then(() => {this.updateFollowers();})
    },
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
        this.$emit('logOut');
    }).then(response => {
        let newToken = {
            refresh: currentToken.refresh,
            access: response.data.access,
        }
        localStorage.setItem('jwt', JSON.stringify(newToken));

        objectToken = localStorage.getItem('jwt');
        currentToken = JSON.parse( objectToken );

        axios.get('http://localhost:8000/following/', {
            headers: {
            Authorization: "Bearer " + currentToken.access
            }
        }).then(
            response => {
                this.persons = [];
                for(let i=0;i<response.data.length;i++) {
                    let currPortraitPath = "static/profile_pictures/default.png"
                    let currentPoster = response.data[i]['follower__additionaluser__profile_picture'];
                    console.log(response.data[i]);
                    if(currentPoster != null) {
                        currPortraitPath = currentPoster.substring(9, currentPoster.length);
                    }

                    this.persons.push({
                        id: response.data[i]['follower__id'],
                        name: response.data[i]['follower__first_name'] + " " + response.data[i]['follower__last_name'],
                        portraitPath: "http://localhost:8000/" + currPortraitPath,
                        username: response.data[i]['follower__username'],
                    })
                }
            }
        );
    });
  }
}
</script>

<style scoped>
.FollowingBlock {
    text-align:left;
    margin: auto;
    flex-direction: column;
    background-color:#262728;
    border-radius: 25px;
    margin-bottom: 30px;
    max-width: 800px;
    color:white;
}
.blueButton {
    background-color: rgb(59, 167, 238);
    border-color: rgb(59, 167, 238);
}

.blueButton:hover {
    background-color: rgb(43, 137, 199);
    border-color: rgb(43, 137, 199);
}

.unfollowButton {
    background-color: #FF5338;
    border-color: #FF5338;
}

.unfollowButton:hover {
    background-color: #cf3821;
    border-color: #cf3821;
}
.show-details {
    border-radius: 25px;
    width: 600px;
    height: auto;
    background-color: #262728;
    margin: auto;
    padding: 25px;
    text-align:left;
    display: flex;
}

.image {
      display: block;
      margin-left: auto;
      margin-right: auto;
      width: 50%;
      padding: 0px;
      width:150px;
      height:150px;
      flex-basis: 70%;
      order: 2;
}

.name {
    /* font-family: Arial, Helvetica, sans-serif;  */
    text-align:center;
    font-size: 21px;
    padding: 20px 0px 0px 0px;
}

.bio {
    /* font-family: Arial, Helvetica, sans-serif; */
    text-align:center;
    /* font-size: small; */
    font-size:15px;
    padding: 10px 0px 0px 0px;
}
</style>