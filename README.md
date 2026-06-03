# elect-rix.tech

Brand tagline: Protect your data. Even when the lights go out.

## Stack

- Astro, Tailwind CSS V4, Bun
- Cloudflare Pages
- Wrangler CLI for deployment

## Project Layout

| Directory | Purpose |
|-----------|---------|
| `src/pages/` | Site routes |
| `src/components/` | Reusable UI components |
| `src/content/` | Blog posts |
| `public/` | Static assets (favicon, OG images) |
| `dist/` | Production build output (git-ignored) |
| `scripts/` | Deployment + build automation |

## Commands

| Command | Action |
|---------|--------|
| `bun install` | Dependencies |
| `bun dev` | Local dev at localhost:4321 |
| `bun build` | Static build → `./dist/` |
| `bun preview` | Preview before deploy |
| `wrangler pages deploy dist` | Deploy to production |

## Deployment

- Static output only (`output: 'static'`)
- Sitemap auto-generated via `@astrojs/sitemap`
- Custom 404 at `src/pages/404.astro`
- OG image: `public/og-default.png`

## Security

API tokens and secrets are managed locally per environment and are never committed to version control.

## About

elect-rix.tech — Astro blog on Cloudflare Pages
