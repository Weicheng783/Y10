<template>
    <div>
        <div v-show="showModal"> 
            <div class="modal is-active">
                <div class="modal-background">
 
                </div>
                <div class="modal-content">
                    <div class="box">
                        <p class="title is-4">ASDKAJSD</p>
                    </div>
                </div>
                <button class="modal-close" @click="showModal=false"></button> 
            </div>
        </div>
 
        <button type="button" class="btn btn-info" @click="showModal=true">Show modal</button>
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
        <p>The people you follow go here</p>
        <div v-for="person in persons" :key="person.name" class="FollowingBlock">
            <div style="display: flex; padding: 10px;">
                <img src="https://images.unsplash.com/photo-1586287011575-a23134f797f9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80" style="max-width: 150px; border-radius: 150px;"/>
                <div style="margin-left: 20px; margin-top: 20px;">
                    <p class="title is-2" style="color: white; margin-bottom: 0px;">{{person.firstName}} {{person.lastName}}</p>
                    <p style="color:gray; font-size:22px;">{{person.smallText}}</p>
                </div>
            </div>
            <div style="text-align:right; padding: 0px 20px 20px 0px;">
                <div v-show="showModal"> 
            <div class="modal is-active">
                <div class="modal-background">
                </div>
                <div class="modal-content">
                  
                  <div class="show-details">
                    <div style="item-align:bottom">
                        <div class="image">
                          <img src="https://images.unsplash.com/photo-1586287011575-a23134f797f9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80" style="border-radius: 150px;"/>
                        </div>
                          <div>
                            <p class="name" style="color: white; margin-bottom: 0px;">Matas Adamson</p>
                            <p class="bio" style="color:gray;">bio template, I love movies.</p>
                            <p class="title is-3" style="color: white; text-align:left;font-size:20px; padding-top: 50px;">Thier favourites</p>
            <div style="display:flex; justify-content:space-between;">
                <div style="display: flex; flex-direction: column; max-width: 30%; align-items:center;">
                    <img style="border-radius: 20px; margin-bottom: px;" src="https://www.themoviedb.org/t/p/w500/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg"/>

                </div>
                <div style="display: flex; flex-direction: column; max-width: 30%; align-items:center;">
                    <img style="border-radius: 20px; margin-bottom: px;" src="https://www.themoviedb.org/t/p/w500/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg"/>

                </div>
                <div style="display: flex; flex-direction: column; max-width: 30%; align-items:center;">
                    <img style="border-radius: 20px; margin-bottom: px;" src="https://www.themoviedb.org/t/p/w500/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg"/>

                </div>
            </div>
            <p class="title is-3" style="color: white; text-align:left; padding-top: 50px;font-size:20px;">Thier reviews</p>
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
                <button class="modal-close" @click="showModal=false"></button> 
            </div>
        </div>
        <button type="button" class="button profileButton" @click="showModal=true">Show Profile</button>
                <button class="button unfollowButton">Unfollow</button>
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
    }
  },
  methods: {
    updateFollowers() {
        var objectToken = localStorage.getItem('jwt');
        var currentToken = JSON.parse( objectToken );
        axios.get('http://localhost:8000/following/', {
            headers: {
                Authorization: "Bearer " + currentToken.access
            }
        }).then(
            data => {
                this.persons = [];
                for(let i=0;i<data.data.length;i++) {
                    this.persons.push({
                        firstName: data.data[i]['follower']['first_name'],
                        lastName: data.data[i]['follower']['last_name'],
                        id: data.data[i]['follower']['id'],
                    });
                }
            }
        );
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
            data => {
                this.persons = [];
                for(let i=0;i<data.data.length;i++) {
                    this.persons.push({
                        firstName: data.data[i]['follower']['first_name'],
                        lastName: data.data[i]['follower']['last_name'],
                        id: data.data[i]['follower']['id'],
                    });
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

.profileButton {
    background-color: #4b7bff;
    border-color: #4b7bff;
}

.profileButton:hover {
    background-color: #3863d8;
    border-color: #3863d8;
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
    font-family: Arial, Helvetica, sans-serif; 
    text-align:center;
    padding: 20px 0px 0px 0px;
}

.bio {
    font-family: Arial, Helvetica, sans-serif;
    text-align:center;
    font-size: small;
    font-size:12px;
    padding: 10px 0px 0px 0px;
}
</style>