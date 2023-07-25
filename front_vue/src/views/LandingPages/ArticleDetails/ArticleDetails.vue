<template>
    <div>
      <h1>{{ article.title }}</h1>
      <p>{{ article.content }}</p>
  
      <!-- Add a link to trigger the download -->
      <a :href="downloadLink" download>
        Download Article as Word Document
      </a>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        article: {},
        downloadLink: '', // Variable to store the download link
      };
    },
    mounted() {
      this.fetchArticle();
      document.title = 'Written-Article-details';
    },
    methods: {
      fetchArticle() {
        const id = this.$route.params.id; // Access the article_id parameter directly
  
        axios
          .get(`/api/v1/article/${id}/`)
          .then((response) => {
            this.article = response.data;
            this.generateDownloadLink(); // Call the function to generate the download link
          })
          .catch((error) => {
            console.error('Error fetching article:', error);
          });
      },
      generateDownloadLink() {
        // Assuming you have an endpoint in your backend that generates and returns the download link
        // Replace 'your_backend_endpoint' with the actual endpoint URL
        axios.get('/api/v1/article/{article_id}/download/').then((response) => {
          this.downloadLink = response.data.downloadLink;
        });
      },
    },
  };
  </script>
  