<template>
  <div>
    <h1>{{ article.title }}</h1>

    <!-- Add a link to trigger the download -->
    <a :href="downloadLink" download target="_blank" v-if="downloadLink">
      Download Article as Word Document
    </a>
    <button @click="downloadDocument" v-else>
      Generate Download Link
    </button>
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
      const articleId = this.$route.params.id; // Access the article_id parameter directly
      axios
        .get(`/api/v1/article/${articleId}/`)
        .then((response) => {
          this.article = response.data;
        })
        .catch((error) => {
          console.error('Error fetching article:', error);
        });
    },
    downloadDocument() {
      // Remove HTML tags from the content using a regular expression
      const plainTextContent = this.article.content.replace(/<[^>]+>/g, '');

      // Make a GET request to the correct endpoint to generate the Word document
      axios
        .get(`/api/v1/article/${this.article.id}/download/?content=${encodeURIComponent(plainTextContent)}`, {
          responseType: 'blob', // Set the responseType to 'blob' to receive the file as a Blob
        })
        .then((response) => {
          const blob = new Blob([response.data], {
            type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
          });
          this.downloadLink = URL.createObjectURL(blob);
        })
        .catch((error) => {
          console.error('Error fetching download link:', error);
        });
    },
  },
};
</script>
