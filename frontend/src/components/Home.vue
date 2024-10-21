<!-- frontend/src/components/Home.vue -->
<template>
<div>
    <h1>Página de inicio</h1>
    <p>Bienvenido a la aplicación</p>
    <button @click="goToLogin">Iniciar Sesión</button>
</div>
</template>

<script>
export default {
name: 'HomePage',
methods: {
    goToLogin() {
    this.$router.push('/login');
    }
}
}
</script>

<style scoped>
button {
padding: 10px 20px;
background-color: #42b983;
color: white;
border: none;
cursor: pointer;
}
button:hover {
background-color: #38a169;
}

h1{
    color: black;
}
</style>