<template>
    <div>
        <p>Recommended people go here</p>
        <p v-for="person in persons" :key="person.first_name" >{{person.first_name}} {{person.last_name}}</p>
    </div>
</template>

<script>
export default {
  name: 'Recommended',
  data() {
    return {
        persons: [
            {
                first_name: "A",
                last_name: "B",
            }
        ],
    }
  },
}
</script>
