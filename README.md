# elect-rix.tech — Technical Operations

Brand tagline: *Protect your data. Even when the lights go out.*

## Stack
- Astro 6.3.7, Tailwind CSS V4, Bun
- Cloudflare Pages (`elect-rix.pages.dev` → `elect-rix.tech` + `www.elect-rix.tech`)
- Wrangler CLI for deployment

## Project Layout
```
src/pages/          Site routes (Astro .astro + .md)
src/components/     Reusable UI components
src/content/        Blog posts (future CMS integration point)
public/             Static assets (favicon, OG images)
dist/               Production build output (git-ignored)
docs/               GPG-encrypted legal docs, incorporation guides, competitive intel
references/         Marketing collateral source: ad strategy, objection guides
scripts/            Deployment + build automation
```

## Commands
| Command | Action |
|---------|--------|
| `bun install` | Dependencies |
| `bun dev` | Local dev at `localhost:4321` |
| `bun build` | Static build → `./dist/` |
| `bun preview` | Preview before deploy |
| `wrangler pages deploy dist --project-name=elect-rix` | Deploy to production |

## Deployment
- Static output only (`output: 'static'`)
- Sitemap auto-generated via `@astrojs/sitemap`
- Custom 404 at `src/pages/404.astro`
- OG image: `public/og-default.png`

## Secrets
Cloudflare API token lives at `~/.secrets/cf-token.txt` (600). Never commit tokens.

## Docs Index (encrypted)
All sensitive documents in `docs/` are GPG-encrypted. Decrypt with:
```bash
gpg --decrypt docs/FILENAME.md.gpg
```

## Next Technical Work
- [ ] Build deploy pipeline script (`scripts/deploy.sh`) with dry-run + local backup
- [ ] Add `public/.well-known/security.txt` 
- [ ] Implement `/blog` content collection for MDX posts
- [ ] Integrate web analytics (privacy-preserving, e.g. Plausible self-hosted)