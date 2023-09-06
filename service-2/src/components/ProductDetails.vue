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
    // product: {
    //   required: true,
    //   type: Object as PropType<Product>,
    // },
  },
  setup() {
    return {}
  },
})
</script>

<template>
  <!-- <div id="product">
    <div class="product-detail">{{ product.id }}</div>
    <div class="product-detail">{{ product.name }}</div>
    <div class="product-detail">{{ product.description }}</div>
    <div class="product-detail">{{ product.price }}</div>
  </div> -->

  <table class="styled-table">
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
/* #product {
  padding-top: 20px;
}

.product-detail {
  display: inline-block;
  padding: 4px;
  margin: 4px;
  border: 1px solid black;
  background-color: #eeeeee;
} */

.styled-table {
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  font-family: sans-serif;
  min-width: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.styled-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
}

.styled-table th,
.styled-table td {
  padding: 12px 15px;
}

.styled-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.styled-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
}
</style>
