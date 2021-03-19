<template>
    <div>
        <div id="navigation">
            <router-link to="/feed">Feed</router-link> |
            <router-link to="/watchlist">Watch List</router-link> |
            <router-link to="/following">Following</router-link> |
            <router-link to="/recommended">Recommended</router-link>
        </div>

        <div class="change-details">
            <p class="title is-2" style="color: white; text-align:left;">Update Profile Settings</p>
            <p class="title is-3" style="color: white; text-align:left; padding-top: 25px;">Change your avatar</p>
            <div class="photo-upload">
                <div>
                <img :src="profilePicture" style="width:200px; height:200px; border-radius:100px;" alt="Profile Picture of User">  
                </div>
                <div style="display:flex; flex-direction:column; justify-content:center; padding: 0px 0px 0px 25px;">
                    <div style="padding-bottom: 20px;">
                        <input 
                            style="display:none;" 
                            type="file" 
                            @change="onFileSelected"
                            ref="fileInput"
                        >
                        <button 
                            class="button"
                            @click="$refs.fileInput.click()"
                        > 📂 Pick image</button>
                        <p v-show="selectedFile != null"> Picture selected </p>
                    </div>

                    <button class="button" @click="uploadPhoto">Upload new</button>  
                </div>       
            </div>

            <p class="title is-3" style="color: white; text-align:left; padding-top: 50px;">Profile details</p>
            <div class="update-details">
                <p id="white-text" class="title is-5" style="padding-top:5px; padding-bottom: 15px; margin-bottom:0px;">First Name</p>
                <input id="input-dark" style="max-width:550px;" class="input" v-model="newUserDetails.firstName"/>

                <p id="white-text" class="title is-5" style="padding-top: 25px; padding-bottom: 15px; margin-bottom:0px;">Last Name</p>
                <input id="input-dark" style="max-width:550px;" class="input" v-model="newUserDetails.lastName" />
            </div>

            <div class="confirm-changes" 
                v-show="(userDetails.firstName != newUserDetails.firstName) 
                || (userDetails.lastName != newUserDetails.lastName)"
            >
            <p class="title is-5" style="color: white; text-align:left; padding-top: 50px;">Please enter your username and password to confirm the changes</p>
            <div class="update-details">
                <p id="white-text" class="title is-5" style="padding-top:5px; padding-bottom: 15px; margin-bottom:0px;">Username</p>
                <input id="input-dark" style="max-width:550px;" class="input"/>

                <p id="white-text" class="title is-5" style="padding-top: 25px; padding-bottom: 15px; margin-bottom:0px;">Password</p>
                <input id="input-dark" style="max-width:550px;" class="input" type="password"/>
            </div>
            </div>

            <p class="title is-3" style="color: white; text-align:left; padding-top: 50px;">Your favourites</p>
            <div style="display:flex; justify-content:space-between;">
                <div style="display: flex; flex-direction: column; max-width: 30%; align-items:center;">
                    <img style="border-radius: 20px; margin-bottom: px;" src="https://www.themoviedb.org/t/p/w500/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg"/>
                    <button class="button" style="width: 90%;">Remove</button>
                </div>
                <div style="display: flex; flex-direction: column; max-width: 30%; align-items:center;">
                    <img style="border-radius: 20px; margin-bottom: px;" src="https://www.themoviedb.org/t/p/w500/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg"/>
                    <button class="button" style="width: 90%;">Remove</button>
                </div>
                <div style="display: flex; flex-direction: column; max-width: 30%; align-items:center;">
                    <img style="border-radius: 20px; margin-bottom: px;" src="https://www.themoviedb.org/t/p/w500/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg"/>
                    <button class="button" style="width: 90%;">Remove</button>
                </div>
            </div>

            <p class="title is-3" style="color: white; text-align:left; padding-top: 50px;">Your reviews</p>
            <div v-for="review in reviews" :key="review.moviePoster" class="reviewBlock">
                <div style="display: flex; align-items:center;">
                    <img :src="review.moviePoster" style="margin: 15px 0px 15px 15px; max-width: 100px; border-radius:15px;"/>
                    <div style="margin: 15px 0px 15px 15px;">
                        <p class="title is-4" id="white-text" style="margin-bottom: 10px;">{{review.movieName}}</p>
                        <p id="white-text" style="font-size: 18px; padding-bottom: 10px;">{{review.reviewContent}}</p>
                        <div v-for="n in review.rating" :key="n" style="display:inline-block;">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Plain_Yellow_Star.png" width="30px;">
                        </div>
                        <p v-show="review.isPrivate==true" style="color:gray;">🔒 Private Review</p>
                    </div>
                </div>

                <div style="text-align: right; padding: 0px 15px 15px 0px;">
                    <button class="button" id="remove-review-button" style="width: 125px; height: 35px;">Remove Review</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'Following',
  data() {
    return {
        selectedFile: null,
        profilePicture: "https://images.unsplash.com/photo-1552374196-c4e7ffc6e126?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80",
        userDetails: {
            firstName: "Andrej",
            lastName: "Velichkovski",
        },
        newUserDetails: {
            firstName: "Andrej",
            lastName: "Velichkovski",
        },
        reviews: [
          {
            moviePoster: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
            movieName: 'Bloodshot',
            reviewContent: 'Enjoyed the movie. Watched it with full attention!',
            rating: 5,
            isPrivate: true,
          },
          {
            moviePoster: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqWnWRWHFfmWcuTBva6CnPam3OWuNxBOI-oA&usqp=CAU',
            movieName: 'Home Alone',
            reviewContent: 'Enjoyed the movie. Watched it with full attention!',
            rating: 5,
            isPrivate: false,
          },
        ],
    }
  },
  methods: {
    onFileSelected(event) {
        this.selectedFile = event.target.files[0];
    },
    uploadPhoto() {
        const fd = new FormData();
        fd.append('profile_picture', this.selectedFile, this.selectedFile.name);

        var objectToken = localStorage.getItem('jwt');
        var currentToken = JSON.parse( objectToken );
        
        axios.post('http://localhost:8000/uploadphoto/', fd, {
            headers: {
                'authorization': 'Bearer ' + currentToken.access,
                'Accept' : 'application/json',
                'Content-Type': fd.Type,
            }
        }).then(() => {this.updateProfilePicture();});
    },
    updateProfilePicture() {
        var objectToken = localStorage.getItem('jwt');
        var currentToken = JSON.parse( objectToken );
        axios.get('http://localhost:8000/uploadphoto/', {
            headers: {
                Authorization: 'Bearer ' + currentToken.access,
            }
        }).then(data => {
            let currentPoster = data.data[0]['profile_picture'];
            if(currentPoster == null) {
              currentPoster = "https://images.unsplash.com/photo-1615105113716-63952cd0cba8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80";
            } 
            else {
              currentPoster = 'http://localhost:8000/' + currentPoster.substring(9, currentPoster.length);
            }
            this.profilePicture = currentPoster;
        });
    },
    updatePersonalReviews() {
        var objectToken = localStorage.getItem('jwt');
        var currentToken = JSON.parse( objectToken );
        axios.get('http://localhost:8000/personal_reviews/', {
            headers: {
                Authorization: 'Bearer ' + currentToken.access,
            }
        }).then(data => {
            console.log(data);
        });
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

        axios.get('http://localhost:8000/uploadphoto/', {
            headers: {
                Authorization: 'Bearer ' + currentToken.access,
            }
        }).then(data => {
            let currentPoster = data.data[0]['profile_picture'];
            if(currentPoster == null) {
              currentPoster = "https://images.unsplash.com/photo-1615105113716-63952cd0cba8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80";
            } 
            else {
              currentPoster = 'http://localhost:8000/' + currentPoster.substring(9, currentPoster.length);
            }
            this.profilePicture = currentPoster;
        });

        axios.get('http://localhost:8000/personal_reviews/', {
            headers: {
                Authorization: 'Bearer ' + currentToken.access,
            }
        }).then(data => {
            this.reviews = [];
            for(let i=0;i<data.data.length;i++) {
                this.reviews.push({
                    movieName: (data.data[i]['movie__movie_name']),
                    reviewContent: (data.data[i]['content']),
                    rating: (data.data[i]['rating']),
                    moviePoster: ('https://image.tmdb.org/t/p/w500' + data.data[i]['movie__poster_path']),
                    isPrivate: (data.data[i]['is_private']),
                }
                );
            }
        });
    });
}
}
</script>

<style>
p {
    color:white;
}

.photo-upload {
    display: flex;
    flex-direction: row;
    align-items:center;
    /* justify-content:center; */
}

.change-details {
    border-radius: 25px;
    max-width: 600px;
    background-color: #262728;
    margin: auto;
    padding: 25px;
    text-align:left;
}

#input-dark {
    background-color: #333333;
    border: none;
    color: white;
}

#input-dark:focus {
    background-color: #383838;
    outline:none;
    color: white;
}

.reviewBlock {
  /* display:flex;  */
  text-align:left;
  margin: auto;
  flex-direction: column;
  background-color:#242424;
  border-radius: 25px;
  margin-bottom: 30px;
  max-width: 800px;
  color:white;
}

#remove-review-button {
    background-color: rgb(131, 30, 30);
    color: white;
    border: none;
}

#remove-review-button:hover {
    background-color: rgb(94, 21, 21);
}

</style>
