<script setup lang="ts">
import ProductDetails from '@/components/ProductDetails.vue'
import ProductForm from '@/components/ProductForm.vue'
import { useProductStore } from '@/stores/ProductStore'

const productStore = useProductStore()

productStore.getProducts()
</script>

<template>
  <h1>Products</h1>
  <ProductForm />
  <ProductDetails :products="productStore.products" />
</template>

<style scoped>
h1 {
  color: #009879;
}
</style>
