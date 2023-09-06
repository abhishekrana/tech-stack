<script lang="ts">
import { type Product } from '@/models/Product'
import type { PropType } from 'vue'
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    product: {
      required: true,
      type: Object as PropType<Product>,
    },
  },
  setup() {
    return {}
  },
})
</script>

<template>
  <div id="product">
    <div class="product-detail">{{ product.id }}</div>
    <div class="product-detail">{{ product.name }}</div>
    <div class="product-detail">{{ product.description }}</div>
    <div class="product-detail">{{ product.price }}</div>
  </div>
</template>

<style scoped>
#product {
  padding-top: 20px;
}

.product-detail {
  display: inline-block;
  padding: 4px;
  margin: 4px;
  border: 1px solid black;
  background-color: #eeeeee;
}
</style>
