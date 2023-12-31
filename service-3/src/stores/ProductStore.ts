import { defineStore } from 'pinia'
import { type Product } from '@/models/Product'
import { ref, computed } from 'vue'
import type { Ref, ComputedRef } from 'vue'

export const useProductStore = defineStore('productStore', () => {
  // Consts
  const baseURL = '/api/products'

  // Refs/State
  const products: Ref<Product[]> = ref([])
  let loading: boolean = false

  // ComputedProperties/Getters
  const length: ComputedRef<number> = computed((): number => {
    return products.value.length
  })

  // Functions/Actions
  async function getProducts(): Promise<void> {
    loading = true
    const res: Response = await fetch(baseURL + '/v1/products/')
    const data = await res.json()
    products.value = data
    loading = false
  }

  async function addProduct(product: Product): Promise<void> {
    const res: Response = await fetch(baseURL + '/v1/products/', {
      method: 'POST',
      body: JSON.stringify([product]),
      headers: { 'Content-Type': 'application/json' },
    })
    if (res.status != 201) {
      console.error(res)
    }
    const data = await res.json()
    product.id = data.id
    product.created_at = data.created_at
    product.updated_at = data.updated_at
    products.value.push(product)
  }

  async function deleteProduct(id: string): Promise<void> {
    products.value = products.value.filter((t: Product): boolean => {
      return t.id !== id
    })
    const res: Response = await fetch(baseURL + '/v1/products/' + id + '/', {
      method: 'DELETE',
    })
    if (res.status != 200) {
      console.error(res)
    }
  }

  return { products, loading, length, getProducts, addProduct, deleteProduct }
})
