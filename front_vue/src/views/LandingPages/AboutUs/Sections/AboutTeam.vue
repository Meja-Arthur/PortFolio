<script setup>
// example component
import HorizontalTeamCard from "@/examples/cards/teamCards/HorizontalTeamCard.vue";

// images
import emma from "@/assets/img/team-5.jpg";
import william from "@/assets/img/bruce-mars.jpg";
import ivana from "@/assets/img/ivana-squares.jpg";
import marquez from "@/assets/img/ivana-square.jpg";
</script>

<template>
  <section class="pb-5 position-relative bg-gradient-dark mx-n3">
    <div class="container">

      <div class="row">

        <div class="col-md-8 text-start mb-5 mt-5">
          <h3 class="text-white z-index-1 position-relative">The Executive Team</h3>
          <p class="text-white opacity-8 mb-0">
           SomeThing Should be Her 
          </p>
        </div>

      </div>

      <div class="row">

        <div class="col-lg-6 col-12">
          <HorizontalTeamCard class="mt-4" :image="emma"
            :profile="{ name: 'Nadine Anyango', link: 'javascript:;' }"
            :position="{ label: 'Chief Editor', color: 'success' }"
            description="SomeThing Should Be Here."
          />
        </div>

        <div class="col-lg-6 col-12">
          <HorizontalTeamCard class="mt-lg-4 mt-5" :image="william"
            :profile="{ name: 'Tony Ogembo', link: 'javascript:;' }"
            :position="{ label: 'Boss', color: 'success' }"
            description="Something Should Be Here ."
          />
        </div>

      </div>
      
      <div class="row mt-4">
        <div class="col-lg-6 col-12">
          <HorizontalTeamCard
            class="mt-4 z-index-2"
            :image="ivana"
            :profile="{ name: 'Meroka', link: 'javascript:;' }"
            :position="{ label: 'something here', color: 'success' }"
            description="Something Should Be Here."
          />
        </div>
        <div class="col-lg-6 col-12">
          <HorizontalTeamCard
            class="mt-lg-4 mt-5 z-index-2"
            :image="marquez"
            :profile="{ name: 'Herbert', link: 'javascript:;' }"
            :position="{ label: 'Something Here', color: 'success' }"
            description="Something Should Be Here."
          />
        </div>
      </div>
    </div>
  </section>
</template>
