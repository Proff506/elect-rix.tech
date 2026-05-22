---
title: RixBot — Private AI Chatbot
description: A private, demo-ready AI chatbot with full R\u0026D knowledge base access. Runs locally with zero cloud dependency, or connects to a private Ollama endpoint for live inference.
category: AI Agent Platform
status: Live
stack: Astro · Browser JS · Ollama API · RAG
slug: rixbot
date: 2025-05-23
updated: 2025-05-23
---

RixBot is a private AI assistant embedded directly into elect-rix.tech. It provides instant answers about the entire project — builds, blog posts, hardware specs, and philosophy — without sending any data to third-party servers in demo mode.

## Architecture

**Frontend (Astro + Vanilla JS):**
- Built as a single Astro page (`src/pages/chatbot.astro`)
- Reactive chat UI with typing animations and suggested questions
- Fully self-contained — no React, no Vue, no external JS dependencies
- Inverted index keyword search for instant RAG-style retrieval
- Responsive dark-theme design matching the rest of the site

**Knowledge Base (Compiled at Build Time):**
- All `builds/` and `posts/` markdown content is read at build time
- Frontmatter and raw content injected into the page as structured JSON
- Simple keyword matching algorithm (TF proxy) ranks documents by relevance
- Zero runtime dependencies for the demo mode

**Live Mode (Optional):**
- Configurable Ollama-compatible endpoint via in-page settings panel
- Supports any OpenAI-compatible API (Ollama, vLLM, llama.cpp server)
- Built-in CORS warning and connection error handling
- Instant mode switch between demo and live without page reload

## How the RAG Works

The demo mode implements a minimal Retrieval-Augmented Generation pipeline:

1. **Build-time ingestion**: All `.md` files in `src/content/builds/` and `src/content/posts/` are parsed
2. **Inverted index**: At runtime, a simple inverted index maps keywords → document indices
3. **Query analysis**: User input is tokenized and matched against the index
4. **Document ranking**: Documents are scored by overlap count and top-k returned
5. **Response generation**: Pre-written knowledge snippets serve as deterministic "generations"

For topics outside the knowledge base, the bot returns a helpful fallback with suggested topics.

## Privacy Guarantees

- **Demo mode**: Zero network requests. Zero API keys. All data stays in the browser.
- **Live mode**: Only communicates with your configured private endpoint. No telemetry, no logging, no third parties.
- **No cookies, no analytics**: The chatbot doesn't set cookies or report usage.

## Use Cases

- **Portfolio visitors**: Instantly learn about elect-rix projects without reading every page
- **R\u0026D documentation**: Acts as an interactive index into months of build notes
- **Demo for clients**: Shows what a private AI assistant looks like without exposing internal infrastructure
- **Live deployment**: Flip a switch, point at an Ollama instance, and get real LLM responses grounded in project data

## Configuration

The settings panel (hidden by default) exposes:
- **Mode**: Demo vs. Live
- **Endpoint**: Ollama API URL (e.g. `http://localhost:11434/api/chat`)
- **Model**: Any model name installed on the endpoint (default: `qwen-hermes`)

## Roadmap

- Semantic search with local embeddings (transformers.js)
- Streaming response support for live mode
- Chat history persistence (localStorage)
- Multi-turn context in live mode
- Voice input via Web Speech API

## Why This Matters

Most "AI chatbots" on websites are thin wrappers around OpenAI or Anthropic APIs. Every visitor message becomes training data for a company that isn't yours. RixBot proves you can have a fast, useful, private assistant that runs entirely on your own terms — without leaking a single token to the cloud.