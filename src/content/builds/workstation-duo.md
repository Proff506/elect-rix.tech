---
title: Workstation Duo
description: Two-machine lab — local LLM inference, distributed builds, GPU compute, and self-hosted services. No cloud dependency.
category: Lab Infrastructure
status: Active
stack: Pop!_OS · Linux Mint · Ollama · Docker · Cloudflare
slug: workstation-duo
date: 2025-03-01
updated: 2025-05-20
---

The Workstation Duo is a two-machine AI lab designed for local-first development. Every piece of infrastructure is self-hosted, private, and under your control.

## Primary Workstation — butters

- **CPU**: Intel Core i9-14900K (24 cores / 32 threads)
- **GPU**: NVIDIA GeForce RTX 5070 Ti (16GB GDDR7 VRAM)
- **RAM**: 32GB DDR5-6000
- **Storage**: 1.8TB NVMe Gen 4 SSD
- **OS**: Pop!_OS 22.04
- **Role**: Primary development, local LLM inference, web hosting

This machine runs Ollama with models like Qwen 3.5, Granite 4.1, Phi 4, Nemotron, and Llama 3.2. At 30-80 tok/s depending on model and quantization, it's fast enough for real interactive work. It handles all web development, builds, and the primary Telegram bot instance.

## Secondary Workstation — proff

- **CPU**: Intel Core i7 (8 cores / 16 threads)
- **GPU**: Dual AMD RX 9060 XT (32GB VRAM total)
- **RAM**: 32GB DDR4-3200
- **Storage**: 2TB SATA SSD
- **OS**: Linux Mint 21 (Cinnamon)
- **Role**: Distributed builds, GPU compute, media generation

This machine handles distributed compilation, ComfyUI for image generation, and GPU workloads that would tie up the primary workstation. With ROCm support, both AMD cards are usable for compute tasks.

## Software Stack

- **Ollama** — Local LLM inference server
- **Docker** — Containerized services and isolation
- **Cloudflare** — Edge DNS, Pages deployment, and Workers
- **Git** — Source control, no remote required
- **Bun** — JavaScript runtime for fast builds
- **Telegram** — Messaging interface for the AI agent

## Philosophy

Every prompt to a closed cloud service becomes training data. Every file you upload to a remote API is stored, analyzed, and potentially reproduced. For personal code, proprietary data, and sensitive projects — that's unacceptable.

The Workstation Duo proves you can run world-class AI locally for the cost of a gaming PC. No subscriptions, no data leakage, no terms-of-service changes mid-project. You own the hardware, you own the models, you own the output.