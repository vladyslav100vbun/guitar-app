import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'


const app = createApp(App)

app.config.globalProperties.$isAuth = localStorage.getItem('access_token');

app.use(router)

app.mount('#app')
