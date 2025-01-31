<template>
    <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title text-center">Login</h3>
            <form @submit.prevent="login">
              <div class="form-group">
                <label for="username">Username</label>
                <input
                  type="text"
                  id="username"
                  v-model="username"
                  class="form-control"
                  placeholder="Enter username"
                />
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input
                  type="password"
                  id="password"
                  v-model="password"
                  class="form-control"
                  placeholder="Enter password"
                />
              </div>
              <div class="form-group text-center">
                <button type="submit" class="btn btn-primary mt-3">Login</button>
                <button type="button" @click="goToRegister" class="btn btn-secondary mt-3 ml-2">Register</button>
              </div>
              <p class="text-danger text-center">{{ message }}</p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
  </template>
  
  <script>
  import api from '../api';
  import { useRouter } from 'vue-router';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        message: '',
      };
    },
    setup() {
      const router = useRouter();
      return { router };
    },
    methods: {
      async login() {
        try {
          const response = await api.post('login/', {
            username: this.username,
            password: this.password,
          });
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
          this.$router.push('/dashboard');
        } catch (error) {
          this.message = 'Login failed!';
        }
      },
      goToRegister() {
        this.$router.push('/register');
      },
    },
  };
  </script>
  