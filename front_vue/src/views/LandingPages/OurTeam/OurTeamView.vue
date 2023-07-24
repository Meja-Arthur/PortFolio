<script setup>
// example components
import DefaultNavbar from "../../../examples/navbars/NavbarDefault.vue";
import Header from "../../../examples/Header.vue";
import DefaultFooter from "../../../examples/footers/FooterDefault.vue";

// sections
import OurTeam from "./Sections/OurTeam.vue";


// image
import image from "@/assets/img/dg2.jpg";
</script>
<template>
  <DefaultNavbar transparent />

  <Header>
    <div
      class="page-header min-height-400"
      :style="{ backgroundImage: `url(${image})` }"
      loading="lazy"
    >
      <span class="mask bg-gradient-dark opacity-8"></span>
    </div>
  </Header>

  <div class="card card-body shadow-xl mx-3 mx-md-4 mt-n6">
    <OurTeam />
 
  </div>

  <DefaultFooter />
 
</template>