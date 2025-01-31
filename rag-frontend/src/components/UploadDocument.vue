<template>
    <div>
      <h2>Upload Document</h2>
      <form @submit.prevent="uploadDocument">
        <input type="file" @change="handleFileUpload" />
        <button type="submit">Upload</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import api from '../api';
  
  export default {
    data() {
      return {
        file: null,
        message: '',
      };
    },
    methods: {
      handleFileUpload(event) {
        this.file = event.target.files[0];
      },
      async uploadDocument() {
        const formData = new FormData();
        formData.append('file', this.file);
  
        try {
          const response = await api.post('upload/', formData, {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('access_token')}`,
              'Content-Type': 'multipart/form-data',
            },
          });
          this.message = 'Document uploaded successfully!';
          this.$emit('documentUploaded', response.data.document_id);
        } catch (error) {
          this.message = 'Document upload failed!';
        }
      },
    },
  };
  </script>
  