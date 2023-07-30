<template>
  
    <div>
        <div>

            <a :href="downloadLink" download target="_blank" v-if="downloadLink">
            Download Article as Word Document
            </a>

            <button class="button" @click="downloadDocument" v-else>
                
                <i class="fas fa-download"></i><br>
                Generate Download Docx
            </button>

        </div>

        <div class="title">
            <h3>{{ article.title }}</h3>
        </div>

  
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
        const plainTextContent = this.article.content.replace(/<[^>]+>/g, '');// removing  the HTML tags 
  
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


<style>
.button {
  background-color: #4CAF50; /* Green */
  border: none;
  border-radius: 10px;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  transition-duration: 0.4s;
}


.title{

    text-align: center;
    font-size: medium;
}

</style>