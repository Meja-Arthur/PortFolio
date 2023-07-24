<script setup>
import DefaultCounterCard from "../../../examples/cards/counterCards/DefaultCounterCard.vue";
</script>

<template>
  <section class="pt-3 pb-4" id="count-stats">
    <div class="container">
      <div class="row">
        <div class="col-lg-9 z-index-2 border-radius-xl mx-auto py-3">
          <div class="row">

            <div class="col-md-4 position-relative">

              <DefaultCounterCard
                color="success"
                title="Coded Elements"
                description="Here To Nadine"
                :count="70"
                suffix="+"
                :duration="3000"
                divider="vertical"
              />

            </div>

            <div class="col-md-4 position-relative">

              <DefaultCounterCard
                color="success"
                title="Design Blocks"
                description=" Another Something Here To "
                :count="15"
                suffix="+"
                :duration="3000"
                divider="vertical"
              />

            </div>

            <div class="col-md-4">

              <DefaultCounterCard
                color="success"
                title="Pages"
                description="SomeThing Should be Here Nadine"
                :count="4"
                :duration="3000"
              />

            </div>


          </div>
        </div>
      </div>
    </div>
  </section>
</template>
