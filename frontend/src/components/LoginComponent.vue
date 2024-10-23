<template>
<div class="container d-flex justify-content-center align-items-center">
    <div class="form-container ">
        <h2 class="text-center mt-3">LOG IN</h2>
        <form @submit.prevent="login">
        <div class="form-group">
            <label for="username">Username:</label>
            <input v-model="username" type="text" placeholder="Usuario">
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input v-model="password" type="password" placeholder="Contraseña">
        </div>

        <div class="my-3 d-flex justify-content-center align-items-center" >
        <p id="error" v-if="error" style="color: red;">{{ error }}</p> <!-- Mostrar mensaje de error aquí -->
        </div>

        <div class="d-flex mt-3 justify-content-center align-items-center">
        <button type="submit" class="btn-lg">ENTRAR</button>
        </div>
        
        <div class="mt-4 d-flex justify-content-end">
            <p id="label-link">¿No tienes cuenta? <a class="fw-bolder" href="/register">Regístrarte</a></p>
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
    password: ''
};
},
methods: {
login() {
    axios.post('http://localhost:8000/api/login/', {
    username: this.username,
    password: this.password
    })
    .then(response => {
    // Guardar el token en localStorage
    localStorage.setItem('token', response.data.token);
    this.$router.push('/dashboard'); // Redirigir al dashboard
    })
    .catch(error => {
    console.error("Error al iniciar sesión", error.response.data);
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

#label-link{
    font-family: "Rajdhani";
    font-size: medium;
}

#error{
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