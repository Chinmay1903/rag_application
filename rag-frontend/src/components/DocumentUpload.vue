<template>
    <div>
      <h3>Upload Document</h3>
      <input type="file" @change="handleFileChange" />
      <button @click="handleUpload">Upload</button>
    </div>
  </template>
  
  <script>
  import api from "../api";
  
  export default {
    name: "DocumentUpload",
    props: {
      onUpload: Function,
    },
    data() {
      return {
        file: null,
      };
    },
    methods: {
      handleFileChange(event) {
        this.file = event.target.files[0];
      },
      async handleUpload() {
        if (!this.file) {
          alert("Please select a file");
          return;
        }
        const formData = new FormData();
        formData.append("file", this.file);
  
        try {
          const response = await api.post("/upload/", formData, {
            headers: { "Content-Type": "multipart/form-data" },
          });
          alert("Document uploaded successfully!");
          this.onUpload(response.data); // Notify parent component
        } catch (error) {
          console.error("Error uploading document:", error);
          alert("Failed to upload document.");
        }
      },
    },
  };
  </script>
  