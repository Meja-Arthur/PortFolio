<script setup>
import CenteredBlogCard from "@/examples/cards/blogCards/CenteredBlogCard.vue";
import bg0 from "@/assets/img/pen.jpg";
import TransparentBlogCard from "@/examples/cards/blogCards/TransparentBlogCard.vue";




</script>


<template>
  <section class="my-5 py-5">
    <div class="container">
      <div class="row align-items-center">

        
          <div class="col-lg-4 ms-auto mt-lg-0 mt-6">
            <TransparentBlogCard 
                 :image="bg0" 
            />
          </div>
        


        <div class="col-lg-6 ms-auto">
          <h2>Better word here </h2>
          <p>

            What we say and how we say it can bring audiences closer to your brand, 
            and explain complex concepts. 
            <br><br>
            Most importantly, optimized content will allow your audience to get answers to their problems easily. 
            <br>
            And what is a product or service if not a solution to a problem?
            <br>
            SCRIBENEST brings all these points together to create a single solution: efficient content writing and editing services.
          
          </p>
        </div>

      </div>
    </div>
  </section>
</template>
<style>
/* Inside your component's style section or in a separate CSS file */
.image-container {
  display: inline-block;
  text-align: center; /* To center the text below the image */
  border: none; /* Remove the visible border */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add a shadow border */
  padding: 10px; /* Add some padding around the content within the container */
}

.image-style {
  width: 400px;
  height: auto;
  margin-left: -20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* You can remove this if you want only the container to have a shadow border */
}

.text-below-image {
  margin-top: 10px; /* Add some spacing between the image and the text */
}

</style>
