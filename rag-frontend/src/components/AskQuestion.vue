<template>
  <div v-if="docId">
    <h2>Ask a Question</h2>
    <form @submit.prevent="askQuestion">
      <input v-model="question" type="text" placeholder="Enter your question" />
      <button type="submit">Ask</button>
    </form>
    <p v-if="answer">Answer: {{ answer }}</p>
  </div>
</template>

<script>
import api from '../api';

export default {
  props: ['docId'],
  data() {
    return {
      question: '',
      answer: '',
    };
  },
  methods: {
    async askQuestion() {
      try {
        const response = await api.post(`ask/${this.docId}/`, { question: this.question }, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        });
        this.answer = response.data.answer;
      } catch (error) {
        this.answer = 'Failed to retrieve answer!';
      }
    },
  },
};
</script>
