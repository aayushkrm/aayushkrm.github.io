---
layout: page
title: Efficient Neural HFT
description: Quantized deep ensemble for market state forecasting on constrained hardware.
img: assets/img/projects/efficient-neural-hft.svg
importance: 3
category: research
tags: [Time Series, INT8, PyTorch, MLOps]
github: https://github.com/aayushkrm/efficient-neural-hft
demo: https://huggingface.co/spaces/aayushkrm/hft-quant-lab
---

## Efficient Neural HFT — Market State Forecasting

*High-frequency trading market-state forecasting under extreme deployment constraints: a 10-model ensemble running on a single CPU core with a memory limit under 20 MB.*

### Highlights

- **Architecture:** a Hive Mind ensemble of deep residual GRUs and LSTMs with Mish activations and Squeeze-and-Excitation blocks.
- **Model compression:** a custom dynamic INT8 quantization pipeline in PyTorch that reduced memory usage by **75%**.
- **Robustness:** automated artifact serialization and custom Huber and Pinball financial losses.
- **Result:** Top 30 of the Wunder Fund RNN Challenge global ranking.

<p class="project-links">
  <a href="https://github.com/aayushkrm/efficient-neural-hft" target="_blank" rel="noopener">View on GitHub</a>
  ·
  <a href="https://huggingface.co/spaces/aayushkrm/hft-quant-lab" target="_blank" rel="noopener">View demo</a>
</p>
