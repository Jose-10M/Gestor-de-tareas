<template>
<div>
    <h2>Recuperar contraseña</h2>
    <form @submit.prevent="resetPassword">
    <input v-model="email" type="email" placeholder="Correo">
    <button type="submit">Enviar</button>
    </form>
</div>
</template>

<script>
export default {
    name: 'PasswordResetComponent',
data() {
    return {
    email: ''
    }
},
methods: {
    resetPassword() {
    this.$http.post('/api/password-reset/', {
        email: this.email
    }).then(() => {
        alert("Correo de recuperación enviado")
    }).catch(() => {
        alert("Error al enviar el correo")
    })
    }
}
}
</script>
