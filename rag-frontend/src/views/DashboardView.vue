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
// import api from '../api';

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
  // created() {
  //   this.checkAccessToken();
  // },
  methods: {
    handleDocumentUploaded(docId) {
      this.docId = docId;
    },
    // async checkAccessToken() {
    //   const accessToken = localStorage.getItem('access_token');
    //   const refreshToken = localStorage.getItem('refresh_token');

    //   if (!accessToken) {
    //     this.refreshAccessToken(refreshToken);
    //   } else {
    //     try {
    //       await api.get('/some-protected-endpoint', {
    //         headers: { Authorization: `Bearer ${accessToken}` },
    //       });
    //     } catch (error) {
    //       if (error.response && error.response.status === 401) {
    //         this.refreshAccessToken(refreshToken);
    //       } else {
    //         this.logout();
    //       }
    //     }
    //   }
    // },
    // async refreshAccessToken(refreshToken) {
    //   try {
    //     const response = await api.post('/refresh/', { refresh: refreshToken });
    //     localStorage.setItem('access_token', response.data.access);
    //   } catch (error) {
    //     this.logout();
    //   }
    // },
    logout() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      this.$router.push('/login');
    },
  },
};
</script>
  