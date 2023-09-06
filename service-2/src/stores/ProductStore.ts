import { defineStore } from 'pinia'
import { type Product } from '@/models/Product'
import { ref, computed } from 'vue'
import type { Ref, ComputedRef } from 'vue'

export const useProductStore = defineStore('productStore', () => {
  // Refs/State
  const products: Ref<Product[]> = ref([])
  let loading: boolean = false

  // ComputedProperties/Getters
  const favs: ComputedRef<Product[]> = computed((): Product[] => {
    return products.value.filter((product: Product): boolean => product.isFav)
  })

  const favsCount: ComputedRef<number> = computed((): number => {
    return products.value.reduce((p: number, c: Product): number => {
      return c.isFav ? p + 1 : p
    }, 0)
  })

  const totalCount: ComputedRef<number> = computed((): number => {
    return products.value.length
  })

  // Functions/Actions
  async function getProducts(): Promise<void> {
    loading = true
    const res: Response = await fetch('http://localhost:3000/products')
    const data = await res.json()
    products.value = data
    loading = false
  }

  async function addProduct(product: Product): Promise<void> {
    products.value.push(product)

    const res: Response = await fetch('http://localhost:3000/products', {
      method: 'POST',
      body: JSON.stringify(product),
      headers: { 'Content-Type': 'application/json' },
    })
    if (res.status != 201) {
      console.error(res)
    }
  }

  async function deleteProduct(id: number): Promise<void> {
    products.value = products.value.filter((t: Product): boolean => {
      return t.id !== id
    })

    const res: Response = await fetch('http://localhost:3000/products/' + id, {
      method: 'DELETE',
    })
    if (res.status != 200) {
      console.error(res)
    }
  }

  async function toggleFav(id: number): Promise<void> {
    const product: Product | undefined = products.value.find((t: Product): boolean => t.id === id)
    if (!product) {
      console.error(`Product with id=${id} does not exist`)
      return
    }

    product.isFav = !product.isFav

    const res: Response = await fetch('http://localhost:3000/products/' + id, {
      method: 'PATCH',
      body: JSON.stringify({ isFav: product.isFav }),
      headers: { 'Content-Type': 'application/json' },
    })
    if (res.status != 200) {
      console.error(res)
    }
  }

  return { products, loading, favs, favsCount, totalCount, getProducts, addProduct, deleteProduct, toggleFav }
})
