import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/movies/MovieDetailView.vue'
import MovieListView from '@/views/movies/MovieListView.vue'
import RecommendedView from '@/views/movies/RecommendedView.vue'
import ReviewSearchView from '@/views/ReviewSearchView.vue'
import SignUpView from '@/views/user/SignUpView.vue'
import LogInView from '@/views/user/LogInView.vue'
import { useCounterStore } from '@/stores/userStore'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'home',
      component: HomeView
    },
    {
      path:'/movies',
      name:'movies',
      component: MovieListView
    },
    {
      path:'/:movieId',
      name:'movie-detail',
      component: MovieDetailView
    },
    {
      path:'/review-search',
      name:'review-search',
      component: ReviewSearchView
    },
    {
      path:'/recommended',
      name:'recommended',
      component: RecommendedView
    },
    // user 구현
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'ArticleView' && store.isLogin === false) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView'}
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인이 되어있습니다.')
    return { name: 'ArticleView'}
  }
})

export default router
