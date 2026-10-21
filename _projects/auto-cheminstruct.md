---
layout: page
title: Auto-ChemInstruct
description: Physics-verified chemical dataset generator built from four autonomous agents.
img: assets/img/projects/auto-cheminstruct.svg
importance: 2
category: research
tags: [Multi-agent, LLM, Cheminformatics, RLHF/DPO]
github: https://github.com/aayushkrm/auto-cheminstruct
---

## Auto-ChemInstruct — Physics-Verified Chemical Dataset Generator

*An autonomous four-agent pipeline that generates physically verified chemical datasets for RLHF/DPO without human annotators. Manuscript in preparation for NeurIPS Datasets & Benchmarks.*

### Pipeline

- **Hypothesis agent** generates candidate reactions.
- **Verification agent** uses RDKit and xTB as physical oracles.
- **Reflection agent** builds causal chain-of-thought traces, explaining failures such as steric hindrance and high energy barriers.
- **Compilation agent** creates preference pairs for DPO and RLHF.

### Highlights

- Failed reactions are **retained**, producing negative examples that standard datasets often lack and reducing positive-label bias.
- **GigaChain** handles literature processing, embeddings for SMILES and IUPAC, and calls to PubChem and Materials Project.
- The **MAP-Elites** evolutionary loop from GigaEvo optimizes agent prompts through LangGraph mutations.
- Orchestrated through **Maestro** with a virtual research team of a GI agent, analyst, and literature reviewer, keeping dataset generation reproducible and auditable.

<p class="project-links">
  <a href="https://github.com/aayushkrm/auto-cheminstruct" target="_blank" rel="noopener">View on GitHub</a>
</p>
