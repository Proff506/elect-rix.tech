---
title: Building This Site with Hermes Agent
description: From a blank Astro project to a deployed site in one session. Here's how an AI agent wrote the code, generated the content, and pushed to production.
pubDate: 2025-05-21
tags: ['astro', 'ai-workflow', 'hermes-agent', 'build-log']
slug: building-with-hermes
category: 'Engineering'
---

This site was built by an AI agent named Hermes. Not assisted by — built by. I gave the instructions, checked the output, and directed the vision. The agent handled every line of code, every deployment step, and every content file.

Here's how it worked.

## The Prompt

The starting prompt was simple:

> Design and build a professional landing page for elect-rix.tech. The site should represent a solo AI engineer with a two-workstation AI lab. Keep it clean, modern, and technically credible. Use Astro, Bun, and Tailwind. Include sections for services, builds, a blog, and about.

That's it. No wireframes, no mockups, no design system. Just the vision.

## What Happened Next

Hermes read the existing project structure (Astro + Tailwind was already set up from a previous session), then:

1. **Designed the information architecture** — Home, Builds, Blog, About, Workstation Duo
2. **Wrote the layout component** — Navigation, content area, footer with consistent styling
3. **Created all page components** — Hero section, services grid, builds showcase, blog listing
4. **Generated content** — Service descriptions, build case studies, about copy, blog posts
5. **Wrote the CSS** — Custom color tokens, typography, markdown content styles
6. **Built and deployed** — `bun run build` followed by a Cloudflare Pages push

Total wall-clock time: about 20 minutes.

## The Agent Architecture

Hermes is a Python-based agent with these tools:

- **File operations** — Read, write, patch, and search files
- **Shell execution** — Run commands, check outputs, handle errors
- **Web research** — Search, extract, and summarize web content
- **Git operations** — Commit, push, and manage branches
- **Deployment** — Cloudflare, AWS, and Docker interactions

The agent maintains context across multiple turns, tracks a todo list, and can handle long-running tasks. For this site build, it executed 15+ file writes, 5 shell commands, and maintained coherence across the entire session.

## What I Did

My role was director, not laborer:

- Defined the vision and constraints
- Reviewed the color scheme and approved the dark theme
- Asked for specific content (the Workstation Duo specs, the services list)
- Verified the build output and checked the deployed site
- Requested corrections ("the nav needs a Builds link", "add syntax highlighting to blog posts")

I never wrote a line of code or CSS. I never ran a build command. The agent did all of it.

## The Result

The site you're on right now. It's not a template. It's not a CMS. It's 100% custom code generated for this specific project, with content written by AI about AI. A recursive artifact.

## What Worked

- **One-shot architecture** — The first design pass was solid. Minor tweaks, no rewrites.
- **Content quality** — The generated copy is specific, technically accurate, and on-brand.
- **Tooling integration** — Astro + Bun + Tailwind was the right stack. Build times under 5 seconds.

## What Didn't

- **Images** — No local image generation in this session. The Duo could handle it (ComfyUI + Stable Diffusion), but it wasn't needed for a text-focused site.
- **SEO metadata** — Got added in a follow-up pass. Easy fix.

## What's Next

The site will grow with the lab. More builds, more blog posts, more experiments. Every addition will be agent-assisted. The pipeline is proven — local AI generates content, local tooling builds the site, and Cloudflare serves it to the world.

That's the vision: autonomous creation, owned end-to-end.