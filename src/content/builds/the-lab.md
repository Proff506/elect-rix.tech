---
title: The Lab
description: Dedicated infrastructure for local AI inference, distributed compute, and self-hosted services that don't phone home. Capability over specs.
category: Lab Infrastructure
status: Active
stack: Pop!_OS · Ollama · Docker · Cloudflare
slug: the-lab
date: 2025-03-01
updated: 2026-05-24
---

The Lab is dedicated AI infrastructure designed for local-first development and deployment. Every service is self-hosted, private, and under direct control.

## Capabilities

- **Local Inference** — Multiple concurrent LLMs across dedicated GPU hardware. No API keys, no telemetry, no per-token billing. Inference stays on-prem by architecture.
- **Distributed Compute** — Multi-machine workload distribution for batch inference, model testing, and reproducible benchmarking. No cloud instances.
- **Self-Hosted Services** — Containerized infrastructure: CI runners, AI agents, deployments all under one roof. No vendor lock-in, no surprise terms-of-service changes.
- **Offline-First Operations** — Designed to keep working when connectivity drops. Local models, local storage, local decision-making.

## Software Stack

- **Ollama** — Local LLM inference server
- **Docker** — Containerized services and isolation
- **Cloudflare** — Edge DNS, Pages deployment, and Workers
- **Bun** — JavaScript runtime for fast builds
- **Git** — Source control across distributed machines

## Philosophy

Every prompt sent to a closed cloud service becomes training data. Every file uploaded to a remote API is stored, analyzed, and potentially reproduced. For client work, proprietary code, and regulated data, that's unacceptable.

The Lab proves you can run capable AI locally without subscriptions, without data leakage, and without terms-of-service changes mid-project. If cloud is used, it's chosen consciously — not by default.
