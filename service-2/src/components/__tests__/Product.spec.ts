import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import Product from '../Product.vue'

describe('Product', () => {
  it('renders properly', () => {
    const wrapper = mount(Product, { props: { msg: 'Hello Vitest' } })
    expect(wrapper.text()).toContain('Hello Vitest')
  })
})
