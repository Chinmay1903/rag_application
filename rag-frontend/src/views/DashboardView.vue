<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col">
        <h1 class="text-center mb-4">Dashboard</h1>
        <div class="d-flex justify-content-end mb-4">
          <button @click="logout" class="btn btn-danger">Logout</button>
        </div>
        <div class="mb-4">
          <UploadDocument @documentUploaded="handleDocumentUploaded" />
        </div>
        <div v-if="docId" class="mt-4">
          <AskQuestion :docId="docId" />
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import { useRouter } from 'vue-router';
  import UploadDocument from '../components/UploadDocument.vue';
  import AskQuestion from '../components/AskQuestion.vue';
  
  export default {
    components: { UploadDocument, AskQuestion },
    data() {
      return {
        docId: null,
      };
    },
    setup() {
      const router = useRouter();
      return { router };
    },
    methods: {
      handleDocumentUploaded(docId) {
        this.docId = docId;
      },
      logout() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        this.$router.push('/login');
      },
    },
  };
  </script>
  