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
          created_at: '',
          updated_at: '',
        }
        productStore.addProduct(product)
        newProductName.value = ''
        newProductDescription.value = ''
        newProductPrice.value = ''
        console.log(
          `Submitted ${product.name}, ${product.description}, ${product.price}, ${product.created_at}, ${product.updated_at}`,
        )
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
    <button class="submit-btn">Add</button>
    <!-- <button type="submit">Add</button> -->
  </form>
</template>

<style scoped>
form input {
  border: 1px solid #009879;
  padding: 2px 15px;
  margin: 0px 2px;
}

.submit-btn {
  background-color: #009879;
  border: none;
  color: white;
  padding: 2px 20px;
  text-decoration: none;
  margin: 0px 10px;
  cursor: pointer;
}
</style>
