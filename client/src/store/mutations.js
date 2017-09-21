import Vue from 'vue';

export default {
  SET_ITEMS: (state, { items }) => {
    items.forEach((item) => {
      if (item) {
        Vue.set(state.items, item.id, item);
      }
    });
  },
};
