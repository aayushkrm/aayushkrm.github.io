---
layout: page
title: AlignSSL-SV
description: Neural networks for detecting genomic deletions from sequencing read alignments.
img: assets/img/projects/alignssl-sv.svg
importance: 1
category: research
tags: [Genomics, CNNs, Transformers, Self-supervised]
github: https://github.com/aayushkrm/AlignSSL-SV
---

## AlignSSL-SV — Detecting Mutations in Genomic Data

*AlignSSL-SV detects deletions, or losses of DNA segments, in sequencing data using neural networks. The model converts read alignments into tensors and predicts whether a deletion is present in a genomic region.*

Built with the research team at the **Big Mathematical Workshop 2026 (Great Math Track)**, Novosibirsk State University.

### Approach

- **Representation:** compared an image-free alignment-tensor representation with a DeepSV-style RGB-pileup baseline.
- **Architecture:** multi-scale CNNs followed by a transformer encoder and a calibrated deletion classifier.
- **Training:** masked alignment modeling for self-supervised pretraining, temperature scaling, and MC dropout for calibrated uncertainty.
- **Evaluation:** 1000 Genomes data with cross-population evaluation, label-efficiency sweeps, hard-negative controls, and varying amounts of labeled data.

### Status

Research code is under active development; a preprint is in preparation.

<p class="project-links">
  <a href="https://github.com/aayushkrm/AlignSSL-SV" target="_blank" rel="noopener">View on GitHub</a>
</p>
