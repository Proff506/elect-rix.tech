#!/usr/bin/env python3
"""
elect-rix Hardware Intelligence Feed
Tracks efficiency-optimized compute devices for local inference deployment.
Runs weekly via cron, saves findings to reports/.
"""

import json
import os
from datetime import datetime

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "notes", "hardware-intel")
os.makedirs(REPORTS_DIR, exist_ok=True)

# Search queries targeting efficiency-optimized inference hardware
QUERIES = [
    # Small form factor / edge inference
    "NVIDIA Jetson Orin Nano Super edge inference 2025 2026",
    "Intel NUC NPU AI inference mini PC 2026",
    "Qualcomm Snapdragon X Elite AI inference benchmarks",
    "Hailo-8 Hailo-15 edge AI accelerator device 2026",
    "AMD Ryzen AI NPU small form factor inference",

    # SBCs and micro devices
    "Raspberry Pi AI Kit Hailo inference benchmarks",
    "Orange Pi 5 Pro RK3588 inference performance",
    "NVIDIA Jetson Thor next generation edge",

    # Apple Silicon (efficiency king)
    "Apple M4 Ultra local LLM inference benchmarks",
    "Apple M5 neural engine specifications leak",

    # Efficiency-focused GPUs
    "RTX 5070 Ti efficiency inference benchmarks",
    "NVIDIA GTX 1650 budget inference local AI",
    "AMD RDNA4 efficiency inference ROCm",

    # Mini/cloud alternative devices
    "Mac Studio M4 inference server local AI",
    "Tinybox AMD MI250 inference performance review",
    "Intel Arc Battlemage inference benchmarks efficiency",

    # Emerging / niche
    "Tenstorrent Grayskull RISC-V AI accelerator 2026",
    "Cerebras WSE-3 inference availability",
    "Groq LPU inference device consumer availability 2026",
    "microBT Whatsminer AI inference repurpose",

    # Market signals
    "edge AI inference device market 2026 2027 forecast",
    "local AI hardware consumer market growth",
    "SBC AI accelerator HAT 2026",
]

def build_report():
    """Build the search query list and metadata for the cron agent to execute."""
    report = {
        "generated_at": datetime.now().isoformat(),
        "purpose": "Track efficiency-optimized hardware for elect-rix local inference deployment. Focus: devices that can run 7B-13B models locally at usable speeds for consumer/smb deployment.",
        "product_roadmap_context": "elect-rix special environments need hardware targets. Version 2.5 deployment requires knowing what consumers will own or can afford to buy.",
        "queries": QUERIES,
        "key_metrics_to_track": [
            "TOPS/W (efficiency, not raw perf)",
            "7B model inference tokens/sec on device",
            "Device cost (consumer price point)",
            "Power draw under load (watts)",
            "RAM/VRAM available for model loading",
            "Local availability (can a consumer buy this today?)",
        ],
        "filter_criteria": {
            "must_have": "Can run a 7B parameter model at >= 10 tokens/sec locally",
            "sweet_spot": "Under $500, under 50W, fits on a desk",
            "enterprise_tier": "Under $2000, runs 13B+ models, suitable for SMB deployment",
            "ignore": "Data center GPUs, cloud-only solutions, vaporware with no ship date",
        },
        "output_path": os.path.join(REPORTS_DIR, f"hw-intel-{datetime.now().strftime('%Y-%m-%d')}.md"),
    }
    return report

if __name__ == "__main__":
    report = build_report()
    outpath = os.path.join(REPORTS_DIR, f"queue-{datetime.now().strftime('%Y-%m-%d')}.json")
    with open(outpath, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Hardware intel queue written to {outpath}")
    print(f"Report will be saved to: {report['output_path']}")