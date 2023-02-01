import { createApp } from 'vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'jquery/dist/jquery.js'
import 'popper.js/dist/umd/popper.js'
import 'bootstrap/dist/js/bootstrap.js'
import 'animate.css';

import App from './App.vue'
import router from './router/index'
import store from './store/index'

const app = createApp(App)

app.use(router)
app.use(store)

app.mount('#app')
