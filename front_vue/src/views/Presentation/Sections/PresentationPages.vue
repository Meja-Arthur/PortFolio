<script setup>
import ExampleCard from "../Components/ExampleCard.vue";
import MaterialBadge from "../../../components/MaterialBadge.vue";
import Fetching from "../../LandingPages/Articles/Sections/Fetching.vue";

// images
import imgSigninCover from "@/assets/img/signin-cover.png";
</script>
<template>
  <section class="py-5">

    <div class="container">
      <div class="row">
        <div class="row text-center my-sm-5 mt-3">

          <div class="col-lg-6 mx-auto">
            <h4 class="">With our published Article all round the Globe</h4>

          </div>

        </div>
      </div>
    </div>

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
