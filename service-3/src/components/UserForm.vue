<script lang="ts">
import type { User } from '@/models/User'
import { useUserStore } from '@/stores/UserStore'
import type { Ref } from 'vue'
import { defineComponent, ref } from 'vue'

export default defineComponent({
  setup() {
    const userStore = useUserStore()

    const newUserName: Ref<string> = ref('')
    const newUserFullname: Ref<string> = ref('')

    const handleSubmit = () => {
      if (newUserName.value.length > 0 && newUserFullname.value.length > 0) {
        // TODO: Validate input.
        const user: User = {
          id: '',
          name: newUserName.value,
          fullname: newUserFullname.value,
          created_at: '',
          updated_at: '',
        }
        userStore.addUser(user)
        newUserName.value = ''
        newUserFullname.value = ''
        console.log(`Submitted ${user.name}, ${user.fullname}, ${user.created_at}, ${user.updated_at}`)
      }
    }
    return { handleSubmit, newUserName, newUserFullname }
  },
})
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <input type="text" placeholder="Enter name" v-model="newUserName" />
    <input type="text" placeholder="Enter fullname" v-model="newUserFullname" />
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
