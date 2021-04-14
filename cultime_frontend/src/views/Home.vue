<template>
    <div>
      <div id="navigation">
        <a href="/" style="background-color: #201c1c; width:200px;height:auto;padding: 0px 20px;position:relative;top:10px; float:left; margin-top:20px; margin-left:25px;"><img style=" " src="https://i.ibb.co/7t9FYRv/Screenshot-2021-03-01-at-22-22-49.png" 
              alt="--Cultime--"  border="0"></a>
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login</router-link>
        <router-link to="/register">Create Account</router-link>
      </div>    

      <div class="homeMainDiv">
        <div class="homeVertDiv" style="height:6vw;">
          <div class="homeSubDiv" style="height:6vw;">
            <p style="color:#232323; font-size:2vw; font-weight: bold;">BECOME A MOVIE CRITIC</p>
          </div>
          <div class="homeSubDiv" style="height:6vw;">
            <p style="color:#232323; font-size:2vw; font-weight: bold;">CREATE YOUR WATCHLIST</p>
          </div>
          <div class="homeSubDiv" style="height:6vw;">
            <p style="color:#232323; font-size:2vw; font-weight: bold;">FIND PEOPLE WITH SIMILAR TASTE</p>
          </div>
        </div>
        <div class="homeVertDiv">
          <div class="homeSubDiv" v-for="review in reviews" :key="review.authorName" style="color:#262728 width:8vw;" >
            <div style="margin: 0px; padding:15px; text-align:left; display:flex; align-items:center;">
              <img :src="review.authorPicture" style="width:3.6vw; height:3.6vw; border-radius: 75px;"/>
              <p style="font-size: 1vw; color:white; margin-left: 10px;">{{review.authorName}} watched <b>{{review.movieName}}</b></p>
            </div>

            <div style="display:flex;">
              <div style="width:7vw;">
                <img style="border-radius:20px; width:4.5vw; height:6.5vw; " :src="review.moviePoster" >
              </div>

              <div style="width:4.5vw; height:6.5vw; ">
                <p style=" width:15vw; font-size: 0.7vw;">
                  {{review.reviewContent}}
                </p>

                <!-- <div v-for="n in review.rating" :key="n" style="display:inline-block; align:bottom ">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Plain_Yellow_Star.png" width="20vw;">
                </div> -->

                <div style="">
                  <p style="color:gray; font-size:1vw;">{{review.movieOverview}}</p>
                </div>
              </div>
            </div>
          </div>          
          <div class="homeSubDiv">
            <img style="border-radius:20px; width:4.5vw; height:6.5vw; margin: 2.8vw 1vw 1vw 1vw;" src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/cmru6N6Hnw2pJwuo1ctH1CxKqKZ.jpg" >
            <img style="border-radius:20px; width:4.5vw; height:6.5vw;  margin: 2.8vw 1vw 1vw 1vw;" src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dLlH4aNHdnmf62umnInL8xPlPzw.jpg" >
            <img style="border-radius:20px; width:4.5vw; height:6.5vw; margin: 2.8vw 1vw 1vw 1vw;" src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/gpYwKrP6s749b5Nzgm2174jKrpf.jpg" >
          </div>
          <div class="homeSubDiv">
            <div class="profilePictures">
            <img src="https://images.unsplash.com/photo-1582556362337-6a785ee99c63?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80" />
            <img src="https://i.pinimg.com/originals/73/16/f5/7316f550de9ca0045e3d8d98a5bb5e44.png" />
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/5f/Alberto_conversi_profile_pic.jpg" />
            </div>
          </div>
        </div>
      </div>

      <div style="width:%100">
        <VueSlickCarousel v-bind="settings" :arrows="true" :dots="true" style="margin: 100px 100px 100px 100px;">
          <div>
            <h1></h1>
            <img src="https://i.ibb.co/9wS5kvS/004.png">
          </div>
          <div>
            <h1></h1>
            <img src="https://i.ibb.co/dk2P7cV/003.png">
          </div>
          <div>
            <h1></h1>
            <img src="https://i.ibb.co/PMkGF6K/001.png">
          </div>
          <div>
            <h1></h1>
            <img src="https://i.ibb.co/wWtf2Vr/006.png">
          </div>                    
          <div>
            <h1></h1>
            <img src="https://i.ibb.co/ZVMXV9Z/005.png">
          </div>
        </VueSlickCarousel>
      </div>
    </div>
</template>

<script>

import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  name: 'Home',
  components: { VueSlickCarousel },
  data () {
    return {
      settings:
      {
        "dots": true,
        "focusOnSelect": true,
        "infinite": true,
        "speed": 500,
        "autoplay": true,
        "autoplaySpeed": 5000,
        "slidesToShow": 3,
        "slidesToScroll": 1,
        "touchThreshold": 5,
      },
      reviews:null
    }
  },
  methods: {
  },
  created () {
    let self = this;

    this.reviewsArr = [
      {
        authorName: 'Emre Inal',
        authorPicture: "https://images.unsplash.com/photo-1582556362337-6a785ee99c63?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80",
        moviePoster: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/cmru6N6Hnw2pJwuo1ctH1CxKqKZ.jpg',
        movieName: 'Paper Lives',
        reviewContent: 'Enjoyed the movie. Watched it with full attention!',
        rating: 3,
      },
      {
        authorName: 'Weicheng Ao',
        authorPicture: "https://images.unsplash.com/photo-1586287011575-a23134f797f9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80",
        moviePoster: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dLlH4aNHdnmf62umnInL8xPlPzw.jpg',
        movieName: 'Home Alone',
        reviewContent: 'Enjoyed the movie. Watched it with full attention!',
        rating: 2,
      },
      {
        authorName: 'Andrej Velichkovski',
        authorPicture: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Alberto_conversi_profile_pic.jpg",
        moviePoster: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/gpYwKrP6s749b5Nzgm2174jKrpf.jpg',
        movieName: 'Home Alone',
        reviewContent: "I like a good hacker movie. This starts brilliantly - but goes nowhere and flounders around like a, er, flounder in a floundering thing. As others have said, it's not so much about hacking as about scamming.",
        rating: 1,
      },
      {
        authorName: 'Awais Ahmed',
        authorPicture: "https://i.pinimg.com/originals/73/16/f5/7316f550de9ca0045e3d8d98a5bb5e44.png",
        moviePoster: "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg",
        movieName: 'Wonder Woman 1984',
        reviewContent: "Wonder Woman 1984 is the right film to end 2020 and to start 2021. It reminds us of what’s truly important in this world, and that we must have faith in ourselves and in one another to do what’s right because if we don’t do it, nobody will.",
        rating: 4,
      },
    ]
    self.reviews = [self.reviewsArr[Math.floor(Math.random()*self.reviewsArr.length)]];
  
    setInterval(function(){ 
        self.reviews = [self.reviewsArr[Math.floor(Math.random()*self.reviewsArr.length)]];
    }, 3000);

  }
}
</script>

<style>
.nav{
  height: 120px;
  display: flex;
  justify-content: center;
  margin-top: 25px;
}
.logo
{
  width: 165.2px;
  height: 44.1px;
  margin: 10px 60px 10px 25px;
}

.homeMainDiv{
  width: 84%;
  height: 24vw;
  background: rgb(42, 42, 42);
  margin: 0% 8% 0% 8%;
  border-radius: 12.5px;
}
.homeVertDiv{
  width: 96%;
  height: 13vw;
  background: transparent;
  margin: 2% 2% 2% 2%;
  display: flex;
}
.homeSubDiv{
  width: 40%;
  height: 96%;
  background: rgb(112, 112, 112);
  margin: 2% 2% 2% 2%;
  border-radius: 15px;
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
.changerDiv
{
  width: 600px;
  height: 800px;
  justify-content: center;
}
.changerImg
{
  width: 800px;
  height: 900px;
}

.rLink
{
  resize: none;
  width: 200px;
  height: 50px;
  background-color: #7a7871;
  border: none;
  font-weight: bold;
  color: #232323;
  text-decoration: center;
  display: inline-block;
  font-size: 21px;
  font-family: Arial;
  padding: 10px 10px 10px 10px;
  margin: 4px 40px;
  cursor: pointer;
  border-radius: 12.5px;
}
.rLink:hover 
{
    background-color: #664914
}
.rLink:active 
{
    background-color: #d19627;
}
.selected
{
  background-color: #d19627;
}
.profilePictures > * {
  border-radius: 75px; 
  width:4vw; 
  height:4vw; 
  margin: 4.0vw 1vw 1vw 1vw;
}
</style>