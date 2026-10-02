// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  vite: {
    build: {
      // Never inline scripts into HTML, so the CSP can be script-src 'self'
      assetsInlineLimit: 0,
    },
  },
});
