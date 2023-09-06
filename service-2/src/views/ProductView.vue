<script setup lang="ts">
import ProductDetails from '@/components/ProductDetails.vue'
import ProductForm from '@/components/ProductForm.vue'
import { useProductStore } from '@/stores/ProductStore'

const productStore = useProductStore()

productStore.getProducts()
</script>

<template>
  <h1>Products</h1>

  <!-- Create -->
  <ProductForm />

  <!-- List -->
  <ProductDetails :products="productStore.products" />
  <!-- <div v-for="product in productStore.products" :key="product.id">
    <ProductDetails :product="product" />
  </div> -->
</template>

<style scoped></style>
