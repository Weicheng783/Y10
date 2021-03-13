<template>
  <div id="app">
    <router-view v-on:logOut="logOut" />
  </div>
</template>

<script>
export default {
  name: "app",
  methods: {
    logOut() {
      localStorage.removeItem('jwt');
      this.$router.push('/')
    }
  },
};

</script>

<style>
#app {
  color:white;
  margin: 0px;
  background-color: #201c1c;
  background-size: cover;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: #ffffff;
}
p, label{
  color: white;
}
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

#logout_button {
  font-weight: bold;
  display: inline-flex;
  /* float: right; */
  /* margin-right:10%; */

  margin-left:50px;

  appearance: button;

    border: none;
    background-color: #230a59;

    border-color: lawngreen;

    color: #007acc;
    padding: 20px 10px 10px 10px;
    /* margin: 30px 30px 20px 20px;  */
    margin-right:10px;
    margin-top:10px;
    /* padding-right: 10px; */
    text-align: center;
    text-decoration: none;
    display: inline-block;
    min-width: 20px;

    font-size: 20px;
    border-radius: 20px;
     
}


#logout_button :hover {
    background-color: #b0a8be;
    /* color: #1D1E1F; */
    color: #1a57b3;
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
