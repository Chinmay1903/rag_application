<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h2 class="card-title text-center mb-4">Register</h2>
            <form @submit.prevent="register">
              <div class="form-group mb-3">
                <input v-model="username" type="text" class="form-control" placeholder="Username" />
              </div>
              <div class="form-group mb-3">
                <input v-model="email" type="email" class="form-control" placeholder="Email" />
              </div>
              <div class="form-group mb-3">
                <input v-model="password" type="password" class="form-control" placeholder="Password" />
              </div>
              <div class="form-group text-center">
                <button type="submit" class="btn btn-primary mt-3">Register</button>
                <button type="button" @click="goToLogin" class="btn btn-secondary mt-3 ml-2">Login</button>
              </div>
              <p v-if="message" class="text-danger text-center mt-3">{{ message }}</p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import { useRouter } from 'vue-router';
  import api from '../api';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        message: '',
      };
    },
    setup() {
      const router = useRouter();
      return { router };
    },
    methods: {
      async register() {
        try {
          const response = await api.post('register/', {
            username: this.username,
            email: this.email,
            password: this.password,
          });
          this.message = response.data.message;
          this.$router.push('/login');
        } catch (error) {
          this.message = 'Registration failed!';
        }
      },
      goToLogin() {
        this.$router.push('/login');
      },
    },
  };
  </script>
  