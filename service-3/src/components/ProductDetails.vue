<script lang="ts">
import { type Product } from '@/models/Product'
import type { PropType } from 'vue'
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    products: {
      required: true,
      type: Array as PropType<Product[]>,
    },
  },
  setup() {
    return {}
  },
})
</script>

<template>
  <table class="products-table">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Description</th>
        <th>Price</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="product in products" :key="product.id">
        <td>{{ product.id }}</td>
        <td>{{ product.name }}</td>
        <td>{{ product.description }}</td>
        <td>{{ product.price }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
.products-table {
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  font-family: sans-serif;
  min-width: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.products-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
}

.products-table th,
.products-table td {
  padding: 12px 15px;
}

.products-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.products-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.products-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.products-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
}
</style>
