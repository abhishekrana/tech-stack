<script setup lang="ts">
import UserDetails from '@/components/UserDetails.vue'
import UserForm from '@/components/UserForm.vue'
import { useUserStore } from '@/stores/UserStore'

const userStore = useUserStore()

userStore.getUsers()
</script>

<template>
  <h1>Users</h1>
  <UserForm />
  <UserDetails :users="userStore.users" />
</template>

<style scoped>
h1 {
  color: #009879;
}
</style>
