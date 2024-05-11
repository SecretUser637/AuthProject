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
app.use(VueAxios, axios)

app.use(router)
app.use(vuetify)

app.mount('#app')
