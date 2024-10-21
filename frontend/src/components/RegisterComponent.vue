<template>
<div>
    <h2>Registrarse</h2>
    <form @submit.prevent="register">
    <input v-model="username" type="text" placeholder="Usuario">
    <input v-model="email" type="email" placeholder="Correo">
    <input v-model="password" type="password" placeholder="Contraseña">
    <button type="submit">Registrar</button>
    </form>
</div>
</template>

<script>
export default {
    name: 'RegisterComponent',
data() {
    return {
    username: '',
    email: '',
    password: ''
    }
},
methods: {
    register() {
    this.$http.post('/api/register/', {
        username: this.username,
        email: this.email,
        password: this.password
    }).then(() => {
        alert("Registro exitoso")
    }).catch(() => {
        alert("Error al registrarse")
    })
    }
}
}
</script>
