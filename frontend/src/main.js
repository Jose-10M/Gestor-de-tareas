// frontend/src/main.js
// main.js
/*import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Asegúrate de importar el router
import axios from 'axios';



const app = createApp(App);

app.use(router); // Asegúrate de usar el router aquí
app.config.globalProperties.$http = axios; // Si estás configurando Axios globalmente

app.mount('#app');*/

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Asegúrate de importar el router
import axios from 'axios';

// Configuración de Axios para incluir el token en cada solicitud
axios.interceptors.request.use(config => {
    const token = localStorage.getItem('token'); // O donde estés guardando el token
    if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
}, error => {
    return Promise.reject(error);
});

const app = createApp(App);

app.use(router); // Asegúrate de usar el router aquí
app.config.globalProperties.$http = axios; // Si estás configurando Axios globalmente

app.mount('#app');
