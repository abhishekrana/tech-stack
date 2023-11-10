<script lang="ts">
import { type User } from '@/models/User'
import type { PropType } from 'vue'
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    users: {
      required: true,
      type: Array as PropType<User[]>,
    },
  },
  setup() {
    return {}
  },
})
</script>

<template>
  <table class="users-table">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Fullname</th>
        <th>Created At</th>
        <th>Updated At</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.name }}</td>
        <td>{{ user.fullname }}</td>
        <td>{{ user.created_at }}</td>
        <td>{{ user.updated_at }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
.users-table {
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  font-family: sans-serif;
  min-width: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.users-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
}

.users-table th,
.users-table td {
  padding: 12px 15px;
}

.users-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.users-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.users-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.users-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
}
</style>
