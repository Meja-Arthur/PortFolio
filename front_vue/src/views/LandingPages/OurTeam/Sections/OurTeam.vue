<script setup>
// example component
import HorizontalTeamCard from "@/examples/cards/teamCards/HorizontalTeamCard.vue";

// images
import emma from "@/assets/img/team-5.jpg";
import william from "@/assets/img/bruce-mars.jpg";
import ivana from "@/assets/img/ivana-squares.jpg";
import marquez from "@/assets/img/ivana-square.jpg";
import axios from 'axios';
import { ref, onMounted } from 'vue';

// Other imports...

// Create a ref to hold the user data
const users = ref([]);

onMounted(async () => {
  // Fetch user data from the backend API
  try {
    const response = await axios.get('/api/users/user/'); // Replace with your actual API endpoint URL
    users.value = response.data;
  } catch (error) {
    console.error('Error fetching user data:', error);
  }
});

// Function to navigate to the user profile page
const navigateToUserProfile = (userId) => {
  router.push({ name: 'userprofile', params: { id: userId } });
};
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
          <RouterLink :to="{name:'profile1'}">
          <HorizontalTeamCard
            class="mt-4"
            :image="emma"
            :profile="{ name: 'Nadine Anyango', link: 'javascript:;' }"
            :position="{ label: 'Cheif Editor', color: 'success' }"
          />
        </RouterLink>
        </div>
        <div class="col-lg-6 col-12">
          <RouterLink :to="{name:'profile2'}">
          <HorizontalTeamCard
            class="mt-lg-4 mt-5"
            :image="william"
            :profile="{ name: 'Tony Ogembo', link: 'javascript:;' }"
            :position="{ label: 'C.E.O', color: 'success' }"

          />
        </RouterLink>
        </div>
      </div>

      <div class="row mt-4">
        <div class="col-lg-6 col-12">
          <RouterLink :to="{name:'profile3'}">
          <HorizontalTeamCard
            class="mt-4 z-index-2"
            :image="ivana"
            :profile="{ name: 'Patrick ALmeida', link: 'javascript:;' }"
            :position="{ label: 'Cheif Editor on Social Health articles ', color: 'success' }"
        
          />
        </RouterLink>
        </div>
        <div class="col-lg-6 col-12">
          <RouterLink :to="{name:'profile4'}">
          <HorizontalTeamCard
            class="mt-lg-4 mt-5 z-index-2"
            :image="marquez"
            :profile="{ name: 'Emmanuel Ogembo', link: 'javascript:;' }"
            :position="{ label: 'CHief Editor on Technology Articles', color: 'success' }"

          />
        </RouterLink>
        </div>
      </div>

    </div>
  </section>
</template>
