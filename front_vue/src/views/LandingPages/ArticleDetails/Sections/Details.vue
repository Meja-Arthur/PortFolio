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


        <div class="article-paper">
          <div class="paper-section">  

            <div class="title">
                <h3>{{ article.title }}</h3>
            </div>

            <p>{{ article.description }}</p>

            <div v-if="article.author_name">
              written by: <h6>{{ article.author_name }}</h6>
            </div>
            <div v-else>
              <p>Author information missing</p>
            </div>
          </div>
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
    watch: {
  article: {
    handler(newValue) {
      console.log('Article Data:', newValue);
      console.log('Author Data:', newValue.author);
    },
    deep: true
  }
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

.button:hover {
    color: white;
}


.title{

    text-align: center;
    font-size: medium;
}
.article-paper {
  background-color: #f7f7f7;
  padding: 20px;
  margin: auto;
  max-width: 800px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.paper-section {
  margin-bottom: 20px;
  padding: 20px;
  background-color: white;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.button {
  background-color: #4CAF50;
  border: none;
  border-radius: 10px;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.button:hover {
  color: white;
}

.title {
  text-align: center;
  font-size: medium;
  margin-top: 20px;
}

</style>