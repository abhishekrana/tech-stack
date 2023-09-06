<script lang="ts">
import type { Product } from '@/models/Product'
import { useProductStore } from '@/stores/ProductStore'
import type { Ref } from 'vue'
import { defineComponent, ref } from 'vue'

export default defineComponent({
  setup() {
    const productStore = useProductStore()

    const newProductName: Ref<string> = ref('')
    const newProductDescription: Ref<string> = ref('')
    const newProductPrice: Ref<string> = ref('')

    const handleSubmit = () => {
      if (
        newProductName.value.length > 0 &&
        newProductDescription.value.length > 0 &&
        newProductPrice.value.length > 0
      ) {
        // TODO: Validate input.
        const product: Product = {
          id: '',
          name: newProductName.value,
          description: newProductDescription.value,
          price: Number(newProductPrice.value),
        }
        productStore.addProduct(product)
        newProductName.value = ''
        newProductDescription.value = ''
        newProductPrice.value = ''
        console.log(`Submitted ${product.name}, ${product.description}, ${product.price}`)
      }
    }
    return { handleSubmit, newProductName, newProductDescription, newProductPrice }
  },
})
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <input type="text" placeholder="Enter name" v-model="newProductName" />
    <input type="text" placeholder="Enter description" v-model="newProductDescription" />
    <input type="text" placeholder="Enter price" v-model="newProductPrice" />
    <button>Add</button>
    <!-- <button type="submit">Add</button> -->
  </form>
</template>

<style scoped></style>
