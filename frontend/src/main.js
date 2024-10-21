// frontend/src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Asegúrate de importar el router
import axios from 'axios';

/*
Vue.config.productionTip = false;

// Configuración de axios si es necesario
axios.defaults.baseURL = 'http://localhost:8000'; // Asegúrate de que la URL de tu API es correcta

new Vue({
  router, // Aquí se pasa el router a la instancia de Vue
render: h => h(App),
}).$mount('#app');
*/

const app = createApp(App);

app.use(router); // Asegúrate de usar el router aquí
app.config.globalProperties.$http = axios; // Si estás configurando Axios globalmente

app.mount('#app');