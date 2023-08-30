<script setup>
import RotatingCard from "../../../examples/cards/rotatingCards/RotatingCard.vue";
import RotatingCardFront from "../../../examples/cards/rotatingCards/RotatingCardFront.vue";
import RotatingCardBack from "../../../examples/cards/rotatingCards/RotatingCardBack.vue";
import DefaultInfoCard from "../../../examples/cards/infoCards/DefaultInfoCard.vue";
</script>


<template>
  <section class="my-5 py-5">
    <div class="container">
      <div class="row align-items-center">

        <div class="col-lg-4 ms-auto me-auto p-lg-4 mt-lg-0 mt-4">

          <RotatingCard>
            <RotatingCardFront
              image="https://images.unsplash.com/photo-1569683795645-b62e50fbf103?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80"
              icon="touch_app"
              title="Some should be here<br/> Nadine"
              description="Capachino whatever."
            />

            <RotatingCardBack
              image="https://images.unsplash.com/photo-1498889444388-e67ea62c464b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1365&q=80"
              title="Rich Forever"
              description="And Also Here Nadine."
              :action="[
                {
                  route: './/sections/page-sections/hero-sections.html',
                  label: 'Start with Headers',
                },
              ]"
            />
          </RotatingCard>

        </div>


        <div class="col-lg-7 ms-auto">
          <h2>Why Choose Us?</h2>
          <div>
            <h4>Professional and Reliable</h4>
            <p>
              <ul>
                <li>Skilled copywriters and editors dedicated to crafting compelling content. </li>
                <li>Clear and open communication to understand your unique needs and goals. </li>
                <li>Swift response to your queries for a seamless collaboration experience.</li>
              </ul>
            </p>
          </div>

          <div>
            <h4>Extensive Portfolio</h4>
            <p>
              <ul>
                <li>Over 300,000 words written across diverse industries. </li>
                <li>Versatility and adaptability are showcased in our portfolio.  </li>
                <li>Experience in e-commerce, technology, healthcare, finance, and more.</li>
              </ul>
            </p>
          </div>

          <div>
            <h4>Experienced Team of Editors</h4>
            <p>
              <ul>
                <li>Meticulous review of every piece of content for quality assurance. </li>
                <li>Elimination of errors, refinement of clarity, and enhanced readability.  </li>
                <li>A commitment to excellence in every project we undertake.</li>
              </ul>
            </p>
          </div>


          <p></p>
          <p></p>
        </div>




      </div>
    </div>
  </section>
</template>
