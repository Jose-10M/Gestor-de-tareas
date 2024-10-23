// frontend/src/router.js
import { createRouter, createWebHistory } from 'vue-router';
/*import Vue from 'vue';
import Router from 'vue-router';*/
import HomePage from './components/Home.vue';
import LoginPage from './components/LoginComponent.vue';
import RegisterComponent from './components/RegisterComponent.vue';
import PasswordResetComponent from './components/PasswordResetComponent.vue';
import DashboardComponent from './components/DashboardComponent.vue';


/*
const routes = [
    { path: '/', component: HomePage },
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterComponent},
    { path: '/password-reset', component: PasswordResetComponent },
    { path: '/dashboard', component: DashboardComponent }
];*/


const routes = [
    { path: '/', component: HomePage },
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterComponent },
    { path: '/password-reset', component: PasswordResetComponent },
    { path: '/dashboard', component: DashboardComponent, meta: { requiresAuth: true } } // Ruta protegida
];


const router = createRouter({
history: createWebHistory(),
routes
});

// frontend/src/router.js

// Agregar esto al final del archivo router.js
router.beforeEach((to, from, next) => {
const isAuthenticated = !!localStorage.getItem('token'); // Comprobar si hay token de JWT en el localStorage
if (to.matched.some(record => record.meta.requiresAuth)) {
    // Si la ruta requiere autenticación y el usuario no está autenticado
    if (!isAuthenticated) {
    next({ name: 'login' });
    } else {
    next();
    }
} else {
    next(); // Si no requiere autenticación, continuar normalmente
}
});

export default router; // Asegúrate de exportar el router