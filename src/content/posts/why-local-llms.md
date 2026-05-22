---
title: Why I Run Local LLMs — No Subscription, No Cloud
description: Cloud LLM subscriptions cost $20/month and send your data to third parties. A local setup costs nothing per token, works offline, and keeps your prompts private. Here's the math.
pubDate: 2025-05-20
tags: ['local-ai', 'ollama', 'privacy', 'workstation-duo']
slug: why-local-llms
category: 'Engineering'
---

I run most of my AI workloads locally via Ollama. Cloud APIs handle the occasional frontier task. The reasoning isn't just about cost — it's about owning your tools.

## The Cost Reality

Cloud LLM subscriptions run $240/year. For that you get a web interface, API access, and the guarantee that your prompts are training data for the next model release.

A local setup:

- **GPU**: RTX 5070 Ti — $749 MSRP; street prices vary significantly by region, tariffs, and retailer
- **Models**: Free, community-trained, or self-hosted
- **Privacy**: Your data never leaves the box

The GPU is a one-time purchase. Models are free. Over two years, you're ahead compared to a cloud subscription. Over three, dramatically so. And you can sell the GPU if you ever move on.

## Performance On Modern Hardware

Local models in 2026 are not slow. On the RTX 5070 Ti:

| Model | Size | Speed | Quality |
|-------|------|-------|---------|
| Qwen 3.5 | 14B Q4 | 60 tok/s | Excellent code |
| Granite 4.1 | 8B Q4 | 80 tok/s | Great reasoning |
| Phi 4 | 14B Q4 | 55 tok/s | Strong general |
| Nemotron | 12B Q4 | 50 tok/s | Good reasoning |

These speeds are interactive. You can have a real conversation, iterate on code, and get feedback in real time. No queue, no rate limits, no "high demand" warnings.

## What You Actually Lose

The cloud has two real advantages:

1. **Model access to the very latest** — frontier cloud models with the newest architectures are genuinely ahead of local models on some tasks.

2. **No maintenance** — You don't install drivers, update GPU toolkits, or debug VRAM allocation.

Both are real. Neither is worth $20/month for someone who can handle a Linux workstation.

## The Hybrid Approach

I use a hybrid setup. Local models handle 90% of tasks — coding, writing, research, small-scale analysis. Cloud APIs (via an aggregation router) handle the 10% that actually needs frontier model capability: complex architecture decisions, nuanced creative writing, or tasks where I need the absolute best reasoning.

An API router gives you access to dozens of frontier models with a single key. Pay per token, no subscription. Use the right model for the job.

## Privacy Isn't Paranoia

Cloud providers' terms of service change. Products get shut down. Data gets leaked. Even if you trust the company today, you don't know who owns it tomorrow.

Local models don't have terms of service. They don't get updated without your permission. They don't have a server room full of your prompts waiting for a subpoena.

## Setup Complexity Is a Myth

Installing Ollama on Linux is one command: `curl -fsSL https://ollama.com/install.sh | sh`. Running a model is `ollama run qwen3.5`. The entire setup from zero to chatting takes under 10 minutes on a workstation with modern GPU drivers.

If you can install a game on Steam, you can run local LLMs.

## Bottom Line

Local LLMs are fast enough, good enough, and cheap enough for serious work in 2026. The only reason to pay $20/month for a cloud subscription is if you can't or won't manage a local GPU. For technical people, that's not a real constraint.

Run local. Keep your data. Own your tools.
