  <template>
    <div class='ui text container'>
      <div class='ui segments'>
        <story v-for="story in stories" v-bind:story="story" :key="story.id"></story>
      </div>
    </div>
  </template>


<script>
import Story from './Story';

export default {
  name: 'stories',
  components: {
    Story,
  },
  data() {
    return {
      stories: this.$store.getters.activeItems,
    };
  },
  beforeMount() {
    this.$store.dispatch('FETCH_ITEMS');
  },
};
</script>
