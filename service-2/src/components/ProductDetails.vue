<script lang="ts">
import { type Product } from '@/models/Product'
import type { PropType } from 'vue'
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    product: {
      // required: true,
      required: false,
      type: Object as PropType<Product>,
    },
  },
  setup() {
    return {}
  },
})
</script>

<template>
  <div>
    <Product />
  </div>
</template>

<style scoped></style>
