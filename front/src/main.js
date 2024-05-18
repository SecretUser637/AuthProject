import './assets/main.css'

import { createApp } from 'vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import App from './App.vue'
import router from './router'

const vuetify = createVuetify({
  components,
  directives,
})
const app = createApp(App)


import axios from 'axios'
import VueAxios from 'vue-axios'

axios.defaults.headers.common['Authorization'] = "Bearer " + localStorage.getItem('JWT_token') ?? ''

app.use(VueAxios, axios)

import ToastPlugin from 'vue-toast-notification';
// Import one of the available themes
import 'vue-toast-notification/dist/theme-default.css';

app.use(ToastPlugin);
app.use(router)
app.use(vuetify)

app.mount('#app')
