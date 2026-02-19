---
layout: page
title: Efficient Neural HFT
description: Market State Forecasting
img:
importance: 2
category: research
github: https://github.com/aayushkrm/efficient-neural-hft
---

## Efficient Neural HFT (Market State Forecasting)

**GitHub:** [aayushkrm/efficient-neural-hft](https://github.com/aayushkrm/efficient-neural-hft)  
**Demo:** [Hugging Face Space](https://huggingface.co/spaces/aayushkrm/hft-quant-lab)

### Key Achievements

- **Architecture:** Architected a "Hive Mind" Ensemble consisting of Deep Residual GRUs and LSTMs, optimized with Mish activations and Squeeze-and-Excitation blocks to maximize predictive power in financial time-series forecasting.
- **Model Compression:** Engineered a custom INT8 Dynamic Quantization pipeline in PyTorch to meet extreme deployment constraints of <20MB storage and single-core CPU execution.
- **Memory Efficiency:** Reduced model memory footprint by 75%, allowing a sophisticated 10-model ensemble to operate within a strictly limited resource budget.
- **MLOps:** Implemented automated MLOps workflows, including artifact serialization and custom financial loss functions (Huber, Pinball) to improve model robustness.
- **Production:** Developed a production-grade inference pipeline specifically designed for high-frequency trading (HFT) latency and performance standards.

### Technologies Used

`PyTorch` `TensorFlow` `Python` `INT8 Quantization` `MLOps` `Financial ML`

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  <div>
    <a href="https://github.com/aayushkrm/efficient-neural-hft" target="_blank" class="btn btn-sm z-depth-0" role="button">
      <i class="fab fa-github gh-icon"></i> View on GitHub
    </a>
    <a href="https://huggingface.co/spaces/aayushkrm/hft-quant-lab" target="_blank" class="btn btn-sm z-depth-0" role="button">
      <i class="fas fa-rocket"></i> View Demo
    </a>
  </div>
</div>
