<template>
  <div class="ui segment">
  	<a :href="story.url">
    	<h5>{{ story.title }}</h5>
  	</a>
  </div>
</template>

<script>
export default {
  props: ['story'],
};
</script>