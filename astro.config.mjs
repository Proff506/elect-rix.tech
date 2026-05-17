// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://elect-rix.tech',
  output: 'static',
  vite: {
    plugins: [tailwindcss()]
  }
});