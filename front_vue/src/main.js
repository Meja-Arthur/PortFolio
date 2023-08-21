

import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8200'

// Nucleo Icons
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";
import materialKit from "./material-kit";


const app = createApp(App);
app.use(createPinia());
app.use(router, axios)
app.use(materialKit);
app.mount("#app");
