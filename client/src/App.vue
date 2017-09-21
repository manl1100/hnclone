<template>
  <div id="app">
    <div class='ui fluid container'>
      <div class='ui container'>
        <div class='ui inverted orange menu'>
          <a class='active item'>
            Hacker News Clone
          </a>
          <a class='item'>
            Show
          </a>
          <a class='item'>
            New
          </a>
        </div>
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  background-color: #F5F5F5;
  min-height: 100%;
}
</style>
