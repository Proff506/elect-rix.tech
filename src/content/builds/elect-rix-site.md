---
title: elect-rix.tech
description: This site — Astro, Bun, Tailwind. Built locally, deployed to Cloudflare Pages, generated with AI assistance.
category: Personal Site
status: Live
stack: Astro · Bun · Tailwind · Cloudflare Pages
slug: elect-rix-site
date: 2025-05-10
updated: 2026-05-19
---

The site you're reading right now. A static site built with Astro, styled with Tailwind CSS v4, and deployed to Cloudflare Pages — all from a basement workstation running Pop!_OS.

## Why Astro

Astro is the right tool for content sites. It produces zero-JS pages by default, ships only what's needed, and has first-class markdown support. The entire site is pre-rendered at build time and served from Cloudflare's edge at sub-100ms globally.

## Stack

- **Astro** — Static site generator with islands architecture
- **Bun** — Runtime, bundler, and package manager (faster than Node for this workload)
- **Tailwind CSS v4** — Utility-first CSS with new @theme directive for custom tokens
- **Cloudflare Pages** — Edge deployment with global CDN, automatic HTTPS, and custom domain support
- **Custom Domain** — elect-rix.tech via HostPapa, DNS managed at Cloudflare

## AI-Assisted Workflow

The entire site was designed and built with the help of local LLMs running on the Workstation Duo. From the copy to the component structure, from the color palette to the deployment pipeline — Hermes Agent (a custom AI agent) handled the implementation while elect-rix directed the vision.

## Performance

- First Contentful Paint: < 200ms
- Lighthouse: 100/100/100/100
- Deploy time: < 30 seconds
- Bundle size: < 100KB critical path

## Source

The source is not public yet but may be open-sourced in the future. The site itself is the demo.