<script setup>
import ExampleCard from "../Components/ExampleCard.vue";
import MaterialBadge from "../../../components/MaterialBadge.vue";
import Fetching from "../../LandingPages/Articles/Sections/Fetching.vue";

// images

</script>
<template>
  <section class="py-5">

    <div class="container mt-2">

      <div class="row">

        <div class="col-md-9">
          <Fetching/>
        </div>

        <div class="col-md-3 mx-auto mt-md-0 mt-3">
          <div class="position-sticky" style="top: 100px !important">
            <h6 class="text-secondary font-weight-normal">
               Something nice should be here 
            </h6>
          </div>
        </div>


      </div>
    </div>
  </section>
</template>
