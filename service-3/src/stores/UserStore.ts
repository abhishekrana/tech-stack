import { defineStore } from 'pinia'
import { type User } from '@/models/User'
import { ref, computed } from 'vue'
import type { Ref, ComputedRef } from 'vue'

export const useUserStore = defineStore('userStore', () => {
  // Consts
  const baseURL = '/api/users'
  // const baseURL = 'http://localhost:3000'

  // Refs/State
  const users: Ref<User[]> = ref([])
  let loading: boolean = false

  // ComputedProperties/Getters
  const length: ComputedRef<number> = computed((): number => {
    return users.value.length
  })

  // Functions/Actions
  async function getUsers(): Promise<void> {
    loading = true
    const res: Response = await fetch(baseURL + '/v1/users/')
    const data = await res.json()
    users.value = data
    loading = false
  }

  async function addUser(product: User): Promise<void> {
    const res: Response = await fetch(baseURL + '/v1/users/', {
      method: 'POST',
      body: JSON.stringify(product),
      headers: { 'Content-Type': 'application/json' },
    })
    if (res.status != 201) {
      console.error(res)
    }
    const data = await res.json()
    product.id = data.id
    users.value.push(product)
  }

  async function deleteUser(id: string): Promise<void> {
    users.value = users.value.filter((t: User): boolean => {
      return t.id !== id
    })
    const res: Response = await fetch(baseURL + '/v1/users/' + id + '/', {
      method: 'DELETE',
    })
    if (res.status != 200) {
      console.error(res)
    }
  }

  return { users, loading, length, getUsers, addUser, deleteUser }
})
