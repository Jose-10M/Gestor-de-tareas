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
import axios from 'axios';

export default {
data() {
return {
    email: ''
};
},
methods: {
resetPassword() {
    axios.post('http://localhost:8000/api/password-reset/', {
    email: this.email
    }).then(response => {
    alert(response.data.message);
    }).catch(error => {
    console.error("Error al restablecer la contraseña", error);
    });
}
}
};
</script>
