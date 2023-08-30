<script setup>
import { onMounted, onUnmounted } from "vue";

//example components
import NavbarDefault from "../..//examples/navbars/NavbarDefault.vue";
import DefaultFooter from "../../examples/footers/FooterDefault.vue";
import Header from "../../examples/Header.vue";


//Vue Material Kit 2 components
import MaterialSocialButton from "@/components/MaterialSocialButton.vue";

// sections
import PresentationCounter from "./Sections/PresentationCounter.vue";
import PresentationPages from "./Sections/PresentationPages.vue";

import data from "./Sections/Data/designBlocksData";
import BuiltByDevelopers from "./Components/BuiltByDevelopers.vue";
import PresentationTestimonials from "./Sections/PresentationTestimonials.vue";
import PresentationInformation from "./Sections/PresentationInformation.vue";
import Intoduction from "./Sections/Intoduction.vue";
import Intro from "./Sections/Intro.vue";


//images
import vrBg from "@/assets/img/vr-bg.jpg";


//dep
import Typed from "typed.js";

//hooks
const body = document.getElementsByTagName("body")[0];
onMounted(() => {
  body.classList.add("presentation-page");
  body.classList.add("bg-gray-200");

  if (document.getElementById("typed")) {
    // eslint-disable-next-line no-unused-vars
    var typed = new Typed("#typed", {
      stringsElement: "#typed-strings",
      typeSpeed: 90,
      backSpeed: 90,
      backDelay: 200,
      startDelay: 500,
      loop: true,
    });
  }

});
onUnmounted(() => {
  body.classList.remove("presentation-page");
  body.classList.remove("bg-gray-200");
});
</script>

<template>

  <div class="container position-sticky z-index-sticky top-0">
    <div class="row">
      <div class="col-12">
        <NavbarDefault :sticky="true" />
      </div>
    </div>
  </div>

  <Header>
    <div
      class="page-header min-vh-75"
      :style="`background-image: url(${vrBg})`"
      loading="lazy"
    >
      <div class="container">

        <div class="row">

          <div class="col-lg-7 text-center mx-auto position-relative">
            <h1 class="text-white">
              Welcome to  <span class="text-white" id="typed"></span>
            </h1>

            <div id="typed-strings">
              <p> ScribeHaven </p>
            </div>


            <p class="lead text-white px-5 mt-3" :style="{ fontWeight: '500' }">
              
            </p>
          </div>

        </div>
        
      </div>
    </div>
  </Header>

  <div class="card card-body blur shadow-blur mx-3 mx-md-4 mt-n6">

    <PresentationCounter />
    <Intoduction/>
    <Intro/>
    <PresentationInformation />
    <PresentationPages />
    <BuiltByDevelopers />
    <PresentationTestimonials />

  </div>

  <DefaultFooter />

</template>
