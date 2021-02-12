<template>
    <p>{{movieTitle}}</p>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'WatchList',
  data() {
    return {
        movieTitle: "Parasite",
    }
  },
}
</script>
