<template>
    <div v-if="answer">
      <h3>Answer:</h3>
      <p><strong>Question:</strong> {{ answer.question }}</p>
      <p><strong>Answer:</strong> {{ answer.answer }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: "DisplayAnswer",
    props: {
      answer: Object,
    },
  };
  </script>
  