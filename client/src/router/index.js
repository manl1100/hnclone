import Vue from 'vue';
import Router from 'vue-router';
import Stories from '@/components/Stories';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Stories',
      component: Stories,
    },
  ],
});
