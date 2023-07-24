<script setup>
import CenteredBlogCard from "@/examples/cards/blogCards/CenteredBlogCard.vue";
import bg0 from "@/assets/img/quill-pen.jpg";
import TransparentBlogCard from "@/examples/cards/blogCards/TransparentBlogCard.vue";




</script>


<template>
  <section class="my-5 py-5">
    <div class="container">
      <div class="row align-items-center">

       <!--- <div class="col-lg-4 ms-auto me-auto p-lg-4 mt-lg-0 mt-4">

                <p>Welcome to the damned with wealth </p>

        </div>

        <div class="col-lg-6 ms-auto">
          <p>Hello You </p>

        </div>--> 
       <!--- <div class="col-lg-4 ms-auto mt-lg-0 mt-6">
          <div class="image-container">
            <img
              :src="bg0"
              alt="Image Description"
              class="image-style"
            />
            <p class="text-below-image">Your text goes here</p>
          </div>
        </div>-->
        <div class="col-lg-6 ms-auto mt-lg-0 mt-6">
          <h2>Better word here </h2>
          <p>
            With over five years of industry expertise, 
            we offer professional and reliable services while maintaining a friendly and approachable demeanor. 
            <br><br>
            At SCRIBENEST, our mission is to empower businesses and individuals through the expert use of words. 
            <br><br>
            It is not only about what you say; how you say it matters.
            <br>
            Well-crafted writing captivates audiences, drives meaningful engagement, 
            and leaves a lasting impression that will make your brand memorable. 
            <br><br>
          </p>
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6">
            <TransparentBlogCard 
                 :image="bg0" 
              />
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
