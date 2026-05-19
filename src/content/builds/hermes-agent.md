---
title: Hermes Agent Bot
description: Autonomous AI assistant deployed on Telegram. Manages coding tasks, research, and DevOps — 24/7 from local infrastructure.
category: AI Agent Platform
status: Running
stack: Python · Telethon · Ollama · Docker
slug: hermes-agent
date: 2025-04-15
updated: 2025-05-20
---

Hermes is an autonomous AI agent that lives on Telegram and manages real tasks. It's not a chatbot — it's an operator that reads messages, executes commands, writes code, deploys applications, and reports back. All running on the Workstation Duo with zero cloud AI dependency.

## What It Does

- **Code Generation** — Writes, reviews, and refactors code in Python, TypeScript, Go, and Rust
- **DevOps Orchestration** — Deploys to Cloudflare, manages DNS, runs CI/CD pipelines
- **Research & Summarization** — Reads documentation, summarizes papers, searches the web via multiple providers
- **File Operations** — Reads, writes, patches, and manages files across the workstation
- **Process Management** — Runs shell commands, monitors logs, and reports on system health
- **Long-Running Tasks** — Handles multi-step workflows that can take minutes or hours

## Architecture

The bot is built on a modular agent framework:

- **Telegram Interface** — Telethon-based, handles inline commands, file uploads, and threaded conversations
- **Core Agent** — State machine with tool use, context management, and error recovery
- **Tool Registry** — Extensible tools for file ops, shell, web search, git, deployment, and more
- **Model Router** — Switches between local models (Qwen, Granite, Phi) and cloud APIs based on task complexity
- **Memory Layer** — SQLite-backed conversation history and project state

## Local-First Design

Hermes defaults to local Ollama models. For tasks that need heavier reasoning (like code review or complex architecture decisions), it can route to cloud APIs — but only when explicitly needed. Everything else runs on the local GPU at 40-60 tok/s.

The bot communicates with the secondary workstation for compute-heavy tasks and can delegate work across both machines in the Duo.