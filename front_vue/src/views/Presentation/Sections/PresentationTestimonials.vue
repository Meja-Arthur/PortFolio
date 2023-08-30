<script setup>
import DefaultReviewCard from "@/examples/cards/reviewCards/DefaultReviewCard.vue";
</script>


<template>
  <section class="py-7">
    <div class="container">
      <div class="row">
        <div class="col-lg-6 mx-auto text-center">
          <h2 class="mb-0">Trusted by over</h2>
          <h2 class="text-gradient text-success mb-3">
            1,000 000+ Article Clients
          </h2>
          <p class="lead">
            Another Paragraph of word's here 
          </p>
        </div>
      </div>


      <div class="row mt-6">
        <DefaultReviewCard
          name="Tonny Ochieng"
          date="1 day ago"
          review='"World need Here ."'
          :rating="7.0"
        />
        <DefaultReviewCard
          class="ms-md-auto"
          color="bg-gradient-success"
          name="Emmanuel Arthur"
          date="1 week ago"
          review='"World need Here  !!!"'
          :rating="5.0"
        />
        <DefaultReviewCard
          name="Yasmin Kazungu"
          date="3 weeks ago"
          review='"World need Here ."'
          :rating="5.0"
        />
      </div>

      <hr class="horizontal dark my-5" />
      <div class="row">
        <h7>Something should be here</h7>
      </div>

    </div>
  </section>
</template>
