<template>
<div>
    <h2>Iniciar sesión</h2>
    <form @submit.prevent="login">
    <input v-model="username" type="text" placeholder="Usuario">
    <input v-model="password" type="password" placeholder="Contraseña">
    <button type="submit">Entrar</button>
    <p v-if="error" style="color: red;">{{ error }}</p> <!-- Mostrar mensaje de error aquí -->
    </form>
</div>
</template>

<script>
export default {
    name: 'LoginPage',
data() {
    return {
    username: '',
    password: '',
    error: ''
    };
},
methods: {
    login() {
    // Enviar datos de login a la API
    this.$http.post('/api/login/', {
        username: this.username,
        password: this.password
    }).then(response => {
        localStorage.setItem('token', response.data.access)
        this.$router.push('/dashboard')
    }).catch(error => {
        // Manejar errores aquí
        if (error.response && error.response.data) {
          this.error = error.response.data.detail || 'Error al iniciar sesión'; // Mostrar el error específico
        } else {
          this.error = 'Error de conexión'; // Mostrar error de conexión
        }
    });
    }
}
}
</script>