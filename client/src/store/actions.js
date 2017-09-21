const HACKER_NEWS_URL = 'http://localhost:8888/stories';

export default {

  FETCH_ITEMS: ({ commit }) => {
    fetch(HACKER_NEWS_URL, {
      method: 'GET',
    })
      .then(resp => resp.json())
      .then((data) => {
        commit({
          type: 'SET_ITEMS',
          items: data.stories,
        });
      });
  },
};
