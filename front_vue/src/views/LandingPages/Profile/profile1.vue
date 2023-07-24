<script setup>
// example components
import DefaultNavbar from "../../../examples/navbars/NavbarDefault.vue";
import Header from "../../../examples/Header.vue";

// sections
import Footer from "./Sections/ProfileFooter.vue";
import Profile from "./Sections/Profile.vue";
import Posts from "./Sections/ProfilePosts.vue";
import Contact from "./Sections/ProfileContact.vue";

// image
import image from "@/assets/img/city-profile.jpg";
import { onMounted } from "vue";
//Vue Material Kit 2 components
import MaterialButton from "@/components/MaterialButton.vue";
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialTextArea from "@/components/MaterialTextArea.vue";

// image
import bgContact from "@/assets/img/examples/blog2.jpg";

// tooltip
import setTooltip from "@/assets/js/tooltip";

// store
import { useAppStore } from "@/stores";
const store = useAppStore();

onMounted(() => {
  setTooltip(store.bootstrap);
});
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
  <div class="card card-body blur shadow-blur mx-3 mx-md-4 mt-n6 mb-4">

    <section class="py-sm-7 py-5 position-relative">
    <div class="container">
      <div class="row">
        <div class="col-12 mx-auto">
          <div class="mt-n8 mt-md-n9 text-center">
            <div class="blur-shadow-avatar">
              <MaterialAvatar
                size="xxl"
                class="shadow-xl position-relative z-index-2"
                :image="profilePic"
                alt="Avatar"
              />
            </div>
          </div>

          <div class="row py-7">

            <div class="col-lg-7 col-md-7 z-index-2 position-relative px-md-2 px-sm-5 mx-auto">
              
              <div  class="d-flex justify-content-between align-items-center mb-2">
                <h3 class="mb-0">Nadine Anyango</h3>
                <div class="d-block">
                  <MaterialButton  class="text-nowrap mb-0" variant="outline" color="success" size="sm">Follow</MaterialButton>
                </div>
              </div>

              <div class="row mb-4">

                <div class="col-auto"><span class="h6 me-1">323</span><span>Posts</span></div>
                  
                <div class="col-auto"><span class="h6 me-1">3.5k</span><span>Followers</span></div>

                <div class="col-auto"><span class="h6 me-1">260</span><span>Following</span></div>
                  
              </div>

              <strong>About</strong>
              <p class="text-lg mb-0">
                Something should be written down here as well about your Info
              </p>
            </div>
          </div>

        </div>
      </div>
    </div>
    </section>


    <Posts />
  </div>


  <section class="py-lg-5">
    <div class="container">
      <div class="row">
        <div class="col">
          <div class="card box-shadow-xl overflow-hidden mb-5">
            <div class="row">
              <div
                class="col-lg-5 position-relative bg-cover px-0"
                :style="{ backgroundImage: `url(${bgContact})` }"
                loading="lazy"
              >
                <div
                  class="z-index-2 text-center d-flex h-100 w-100 d-flex m-auto justify-content-center"
                >
                  <div class="mask bg-gradient-dark opacity-8"></div>
                  <div
                    class="p-5 ps-sm-8 position-relative text-start my-auto z-index-2"
                  >
                    <h3 class="text-white">Contact Information</h3>
                    <p class="text-white opacity-8 mb-4">
                      Fill up the form and our Team will get back to you within
                      24 hours.
                    </p>
                    <div class="d-flex p-2 text-white">
                      <div>
                        <i class="fas fa-phone text-sm"></i>
                      </div>
                      <div class="ps-3">
                        <span class="text-sm opacity-8">(+254) 772 100 200</span>
                      </div>
                    </div>
                    <div class="d-flex p-2 text-white">
                      <div>
                        <i class="fas fa-envelope text-sm"></i>
                      </div>
                      <div class="ps-3">
                        <span class="text-sm opacity-8"
                          >Arthurogembo@gmail.com</span
                        >
                      </div>
                    </div>
                    <div class="d-flex p-2 text-white">
                      <div>
                        <i class="fas fa-map-marker-alt text-sm"></i>
                      </div>
                      <div class="ps-3">
                        <span class="text-sm opacity-8"
                          >Dyonisie Wolf Bucharest, RO 010458</span
                        >
                      </div>
                    </div>
                    <div class="mt-4">
                      <MaterialButton
                        color="none"
                        size="lg"
                        class="btn-icon-only btn-link text-white mb-0"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        data-original-title="Log in with Facebook"
                      >
                        <i class="fab fa-facebook"></i>
                      </MaterialButton>
                      <MaterialButton
                        color="none"
                        size="lg"
                        class="btn-icon-only btn-link text-white mb-0"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        data-original-title="Log in with Twitter"
                      >
                        <i class="fab fa-twitter"></i>
                      </MaterialButton>
                      <MaterialButton
                        color="none"
                        size="lg"
                        class="btn-icon-only btn-link text-white mb-0"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        data-original-title="Log in with Dribbble"
                      >
                        <i class="fab fa-dribbble"></i>
                      </MaterialButton>
                      <MaterialButton
                        color="none"
                        size="lg"
                        class="btn-icon-only btn-link text-white mb-0"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        data-original-title="Log in with Instagram"
                      >
                        <i class="fab fa-instagram"></i>
                      </MaterialButton>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-7">
                <p>Something should be here for example the profession of this guy in the company </p>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </section>


  <Footer />
</template>