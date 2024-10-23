<template>
<div class="container d-flex justify-content-center align-items-center">
    <div class="form-container">
        <h2 class="d-flex justify-content-center align-items-center">SING UP</h2>
        <form @submit.prevent="register">
        <div class="form-group">
            <label for="username">Username:</label>
            <input v-model="username" type="text" placeholder="Usuario">
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input v-model="email" type="email" placeholder="Correo">
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input v-model="password" type="password" placeholder="Contraseña">
        </div>
        <div class="d-flex mt-4 justify-content-center align-items-center">
        <button type="submit">REGISTRAR</button>
        </div>
        </form>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
data() {
return {
    username: '',
    email: '',
    password: '',
    first_name: '',
    last_name: ''
};
},
methods: {
register() {
    axios.post('http://localhost:8000/api/register/', {
    username: this.username,
    email: this.email,
    password: this.password,
    first_name: this.first_name,
    last_name: this.last_name
    }).then(response => {
    alert(response.data.message);
    this.$router.push('/login');
    }).catch(error => {
    console.error("Error al registrar", error);
    });
}
}
};
</script>

<style scoped>
.container{
    height: 100vh; 
}

.form-container {
    width: 100%;
    max-width: 400px;
    margin: 50px auto;
    padding: 30px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form-container h2 {
    color: #6a1b9a; /* Color morado */
    font-family: "Bowlby One";

}

.form-container p{
    font-family: "Bowlby One";
    color: black;
}

.form-group input {
    width: 100%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
    font-family: 'Times New Roman', Times, serif; /* Fuente Times New Roman */
}

.form-group label {
    display: block;
    color: #6a1b9a; /* Color morado */
    margin-bottom: 8px;
}

.form-group input:focus {
    outline-color: #6a1b9a; /* Morado al hacer foco en el input */
}

button:hover {
    background-color: #4e148c; /* Morado más oscuro */
}

button {
    width: 40%;
    padding: 12px;
    background-color: #6a1b9a; /* Morado */
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-family: 'Times New Roman', Times, serif;
}

.form-group input, label, button, a{
    font-family: "Rajdhani";
    font-weight: bolder
}

@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Bowlby+One&display=swap');
</style>