<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/users" class="nav-item">Users</RouterLink>
        <RouterLink to="/products" class="nav-item">Products</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
nav {
  width: 100%;
  font-size: 20px;
  text-align: center;
}

.nav-item {
  padding: 10px;
}
</style>
