<template>
    <div>
      <h3>Ask a Question</h3>
      <input
        type="text"
        v-model="question"
        placeholder="Enter your question"
      />
      <button @click="handleAskQuestion">Ask</button>
    </div>
  </template>
  
  <script>
  import api from "../api";
  
  export default {
    name: "QuestionForm",
    props: {
      docId: Number,
      onAnswerReceived: Function,
    },
    data() {
      return {
        question: "",
      };
    },
    methods: {
      async handleAskQuestion() {
        if (!this.question) {
          alert("Please enter a question");
          return;
        }
        try {
          const response = await api.post(`/ask/${this.docId}/`, {
            question: this.question,
          });
          this.onAnswerReceived(response.data);
        } catch (error) {
          console.error("Error asking question:", error);
          alert("Failed to get an answer.");
        }
      },
    },
  };
  </script>
  