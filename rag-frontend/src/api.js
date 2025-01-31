// src/api.js
import axios from 'axios';
import router from './router';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/', // Replace with your Django API base URL
});

// Add a response interceptor
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      // Redirect to login page on 401 Unauthorized
      router.push('/login');
    }
    return Promise.reject(error);
  }
);

export default api;
