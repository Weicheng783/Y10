<template>
    <div>
        <p>The people you follow go here</p>
        <p v-for="person in persons" :key="person.first_name" >{{person.first_name}} {{person.last_name}}</p>
    </div>
</template>

<script>
export default {
  name: 'Following',
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
