# Pre-Commit Security Checklist

Run through this before every commit to `main`.

## README / Public Docs

- [ ] No internal directory contents described (docs/, references/, notes/)
- [ ] No file paths to secrets or tokens on disk
- [ ] No operational commands (gpg decrypt, ssh, etc.)
- [ ] No exact dependency versions (e.g., Astro 6.3.7 → Astro 6.x or Astro)
- [ ] No cloud project names, account IDs, or zone IDs
- [ ] No "competitive intel," "legal docs," or similar treasure-map language

## Code & Config

- [ ] No `.env`, `.env.local`, or secret files staged
- [ ] No API keys, tokens, or passwords in source
- [ ] `wrangler.toml`, `astro.config.mjs`, etc. contain no secrets

## Git Hygiene

- [ ] `git diff --cached` reviewed — know exactly what is going public
- [ ] No sensitive files added to `.gitignore` after they were already committed
- [ ] If deleting sensitive files, verify they are purged from history (BFG / filter-repo)

## Files That Should Never Be Public

| Category | Examples |
|----------|----------|
| Secrets | API tokens, private keys, passwords, session cookies |
| Legal | NUANS reports, incorporation certificates, contracts |
| Financial | Bank details, pricing sheets, supplier agreements |
| Operational | Server configs, internal IP addresses, VPN endpoints |
| Competitive | Ad strategy, objection guides, vendor pricing |

## One-Liner Self-Check

```bash
git diff --cached --name-only | xargs grep -HnE '(token|secret|password|key|gpg|decrypt|competitive|intel|legal|incorporation|\.secrets|cf-token|cloudflare)' 2>/dev/null
```

If this returns hits, stop and review.

---

*Last updated: 2026-06-03*
*Remedy for: README oversharing incident (commit 6a38b87)*
