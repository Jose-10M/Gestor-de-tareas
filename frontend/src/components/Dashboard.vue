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
export default {
    name: 'DashboardComponent',
computed: {
    isLoggedIn() {
    return !!localStorage.getItem('token')
    }
}
}
</script>
