import { defineStore } from 'pinia'
import { type User } from '@/models/User'
import { ref, computed } from 'vue'
import type { Ref, ComputedRef } from 'vue'

export const useUserStore = defineStore('userStore', () => {
  // Consts
  const baseURL = '/api/users'

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

  async function addUser(user: User): Promise<void> {
    const res: Response = await fetch(baseURL + '/v1/users/', {
      method: 'POST',
      body: JSON.stringify([user]),
      headers: { 'Content-Type': 'application/json' },
    })
    if (res.status != 201) {
      console.error(res)
    }
    const data = await res.json()
    user.id = data.id
    user.created_at = data.created_at
    user.updated_at = data.updated_at
    users.value.push(user)
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
