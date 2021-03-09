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
            <router-link to="/feed">Feed</router-link> |
            <router-link to="/watchlist">Watch List</router-link> |
            <router-link to="/following">Following</router-link> |
            <router-link to="/recommended">Recommended</router-link>
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
                <button class="button blueButton" style="margin-right: 10px;">View Profile</button>
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
</style>