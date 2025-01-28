<template>
  <div id="app">
    <h1>Async QA System</h1>
    <DocumentUpload @onUpload="handleDocumentUpload" />
    <QuestionForm
      v-if="docId"
      :docId="docId"
      @onAnswerReceived="handleAnswerReceived"
    />
    <DisplayAnswer :answer="answer" />
  </div>
</template>

<script>
import DocumentUpload from "./components/DocumentUpload.vue";
import QuestionForm from "./components/QuestionForm.vue";
import DisplayAnswer from "./components/DisplayAnswer.vue";

export default {
  name: "App",
  components: {
    DocumentUpload,
    QuestionForm,
    DisplayAnswer,
  },
  data() {
    return {
      docId: null,
      answer: null,
    };
  },
  methods: {
    handleDocumentUpload(data) {
      this.docId = data.document_id; // Replace with the key returned from your backend
      this.answer = null; // Clear previous answer
    },
    handleAnswerReceived(data) {
      this.answer = data;
    },
  },
};
</script>
