<script lang="ts">
import type { Ref } from 'vue'
import { defineComponent, ref } from 'vue'

export default defineComponent({
  setup() {
    const newProductName: Ref<string> = ref('')
    const newProductDescription: Ref<string> = ref('')
    const newProductPrice: Ref<string> = ref('')

    const handleSubmit = () => {
      if (
        newProductName.value.length > 0 &&
        newProductDescription.value.length > 0 &&
        newProductPrice.value.length > 0
      ) {
        console.log(`Submitted ${newProductName.value} ${newProductDescription.value} ${newProductPrice.value}`)
        newProductName.value = ''
        newProductDescription.value = ''
        newProductPrice.value = ''
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
