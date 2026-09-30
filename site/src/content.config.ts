import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';

const laws = defineCollection({
  loader: glob({ pattern: '*.yaml', base: '../data/laws' }),
});

export const collections = { laws };

