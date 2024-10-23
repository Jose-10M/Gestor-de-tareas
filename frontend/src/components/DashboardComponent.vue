<template>
<div v-if="isLoggedIn">
    <h2>Bienvenido al Dashboard</h2>
</div>
<div v-else>
    <p>Debes iniciar sesión para ver esta página</p>
    <router-link to="/login">Iniciar Sesión</router-link>
</div>
</template>

<script>
import axios from 'axios';

export default {
data() {
return {
    data: null
};
},
created() {
this.fetchDashboardData();
},
methods: {
fetchDashboardData() {
    const token = localStorage.getItem('token'); // Obtener el token del localStorage

    axios.get('http://localhost:8000/api/dashboard/', {
    headers: {
        'Authorization': 'Token ' + token // Enviar el token en la cabecera
    }
    })
    .then(response => {
    this.data = response.data; // Guarda los datos en el estado
    })
    .catch(error => {
    console.error("Error al acceder al dashboard", error.response.data);
    });
}
}
};
</script>
