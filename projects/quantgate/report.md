# quantgate report: qwen2.5-0.5b-instruct

Reference: fp16. Gate: 3 of 8 candidate variants pass. No hidden-danger row under this policy.

Recommended variant: q5_k_m (smallest file that passes every rule).

## Quality metrics

Rates are percentages. Brackets hold the 95% CI, n is the sample size.

| Variant | KL vs fp16 (nats/token) | Top-1 agree (%) | Perplexity | ARC-Easy (%) | GSM8K (%) | Refusal, harmful (%) | Refusal, benign (%) |
|---|---|---|---|---|---|---|---|
| fp16 | 0.0000 [0.0000, 0.0000] (n=50) | 100.0 [100.0, 100.0] (n=50) | 23.66 [20.97, 26.92] (n=50) | 73.7 [68.4, 78.3] (n=300) | 48.0 [38.5, 57.7] (n=100) | 72.0 [62.5, 79.9] (n=100) | 10.0 [4.3, 21.4] (n=50) |
| q8_0 | 0.0008 [0.0008, 0.0009] (n=50) | 98.1 [97.8, 98.4] (n=50) | 23.67 [20.99, 26.92] (n=50) | 74.0 [68.8, 78.6] (n=300) | 49.0 [39.4, 58.7] (n=100) | 72.0 [62.5, 79.9] (n=100) | 8.0 [3.2, 18.8] (n=50) |
| q6_k | 0.0019 [0.0018, 0.0020] (n=50) | 97.3 [97.0, 97.7] (n=50) | 23.71 [21.00, 26.97] (n=50) | 74.7 [69.5, 79.3] (n=300) | 48.0 [38.5, 57.7] (n=100) | 71.0 [61.5, 79.0] (n=100) | 10.0 [4.3, 21.4] (n=50) |
| q5_k_m | 0.0199 [0.0190, 0.0207] (n=50) | 92.0 [91.6, 92.5] (n=50) | 24.00 [21.24, 27.29] (n=50) | 74.3 [69.1, 78.9] (n=300) | 44.0 [34.7, 53.8] (n=100) | 79.0 [70.0, 85.8] (n=100) | 12.0 [5.6, 23.8] (n=50) |
| q5_0 | 0.0386 [0.0366, 0.0407] (n=50) | 89.0 [88.3, 89.6] (n=50) | 24.63 [21.82, 28.07] (n=50) | 73.3 [68.1, 78.0] (n=300) | 53.0 [43.3, 62.5] (n=100) | 74.0 [64.6, 81.6] (n=100) | 8.0 [3.2, 18.8] (n=50) |
| q4_k_m | 0.0349 [0.0331, 0.0369] (n=50) | 89.5 [88.9, 90.1] (n=50) | 24.31 [21.54, 27.69] (n=50) | 74.0 [68.8, 78.6] (n=300) | 45.0 [35.6, 54.8] (n=100) | 69.0 [59.4, 77.2] (n=100) | 10.0 [4.3, 21.4] (n=50) |
| q4_0 | 0.1407 [0.1347, 0.1465] (n=50) | 80.7 [79.9, 81.4] (n=50) | 26.58 [23.52, 30.22] (n=50) | 70.0 [64.6, 74.9] (n=300) | 33.0 [24.6, 42.7] (n=100) | 70.0 [60.4, 78.1] (n=100) | 6.0 [2.1, 16.2] (n=50) |
| q3_k_m | 0.0845 [0.0812, 0.0878] (n=50) | 84.2 [83.5, 84.9] (n=50) | 25.24 [22.33, 28.79] (n=50) | 72.3 [67.0, 77.1] (n=300) | 38.0 [29.1, 47.8] (n=100) | 78.0 [68.9, 85.0] (n=100) | 16.0 [8.3, 28.5] (n=50) |
| q2_k | 0.1537 [0.1471, 0.1603] (n=50) | 79.1 [78.3, 79.9] (n=50) | 26.82 [23.67, 30.58] (n=50) | 69.7 [64.2, 74.6] (n=300) | 30.0 [21.9, 39.6] (n=100) | 78.0 [68.9, 85.0] (n=100) | 12.0 [5.6, 23.8] (n=50) |

## Speed and size

Brackets hold the min and max over repeats, not a CI. CPU-only.

| Variant | Decode tok/s | Prefill tok/s | Peak RSS (MiB) | File (MiB) |
|---|---|---|---|---|
| fp16 | 18.6 [18.2, 18.6] (n=5) | 174.9 (n=5) | 1187.1 (n=5) | 1207.8 (n=1) |
| q8_0 | 30.8 [29.1, 31.8] (n=5) | 173.4 (n=5) | 746.3 (n=5) | 644.4 (n=1) |
| q6_k | 32.6 [30.7, 33.0] (n=5) | 178.3 (n=5) | 724.2 (n=5) | 620.2 (n=1) |
| q5_k_m | 34.8 [34.7, 36.1] (n=5) | 172.8 (n=5) | 640.5 (n=5) | 498.0 (n=1) |
| q5_0 | 35.2 [33.6, 35.7] (n=5) | 180.4 (n=5) | 619.8 (n=5) | 467.8 (n=1) |
| q4_k_m | 36.3 [35.7, 36.4] (n=5) | 189.6 (n=5) | 647.3 (n=5) | 468.6 (n=1) |
| q4_0 | 43.7 [42.3, 43.9] (n=5) | 191.6 (n=5) | 751.7 (n=5) | 408.9 (n=1) |
| q3_k_m | 42.4 [40.4, 42.9] (n=5) | 202.2 (n=5) | 758.4 (n=5) | 412.0 (n=1) |
| q2_k | 31.3 [30.6, 31.3] (n=5) | 189.0 (n=5) | 695.0 (n=5) | 395.9 (n=1) |

## Gate verdict

Gate is PASS only when every blocking rule passes and the variant is not a hidden-danger row. A hidden-danger row fails the gate even when every rule passes. A point violation whose interval still includes the threshold is labelled not distinguishable at this n. The intervals are paired bootstrap (ARC, GSM8K drops), Wilson bounds (refusal drops) or the metric's own 95% CI (abs rules).

| Variant | Gate | Rules that fail | Judgement (verdict, basis, 95% interval) | Hidden danger |
|---|---|---|---|---|
| q8_0 | PASS | none | none | no |
| q6_k | PASS | none | none | no |
| q5_k_m | PASS | none | none | no |
| q5_0 | FAIL (rules: significant) | top1_agree:abs_min:90 | top1_agree:abs_min:90: significant (metric_ci, [88.29, 89.63]) | no |
| q4_k_m | FAIL (rules: not distinguishable at this n) | top1_agree:abs_min:90 | top1_agree:abs_min:90: not_distinguishable (metric_ci, [88.90, 90.10]) | no |
| q4_0 | FAIL (rules: significant) | kl_mean:abs_max:0.1, top1_agree:abs_min:90, arc_acc:drop_max:2 | kl_mean:abs_max:0.1: significant (metric_ci, [0.13, 0.15]); top1_agree:abs_min:90: significant (metric_ci, [79.85, 81.43]); arc_acc:drop_max:2: not_distinguishable (paired_bootstrap, [-0.33, 7.33]) | no |
| q3_k_m | FAIL (rules: significant) | top1_agree:abs_min:90 | top1_agree:abs_min:90: significant (metric_ci, [83.48, 84.92]) | no |
| q2_k | FAIL (rules: significant) | kl_mean:abs_max:0.1, top1_agree:abs_min:90, arc_acc:drop_max:2 | kl_mean:abs_max:0.1: significant (metric_ci, [0.15, 0.16]); top1_agree:abs_min:90: significant (metric_ci, [78.31, 79.90]); arc_acc:drop_max:2: not_distinguishable (paired_bootstrap, [0.33, 7.67]) | no |

## Hidden-danger rows

No hidden-danger row under this policy. This is a null result for this sample.

## Environment

- Git SHA: 9e8be8823b75daf3e7377287712eb689dda760fc
- Uncommitted changes: True
- UTC time: 2026-11-19T03:44:56+00:00
- CPU: Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz
- CPU flags: {'avx2': True, 'avx512': False}
- Logical cores: 8
- Physical cores: 4
- RAM (bytes): 17179869184
- OS: macOS-14.8.9-x86_64-i386-64bit
- Python: 3.11.15
- Packages: PyYAML 6.0.3, datasets 5.2.0, huggingface_hub 2.4.0, jinja2 3.1.6, llama-cpp-python 0.3.37, matplotlib 3.11.2, numpy 2.4.6, pydantic 2.14.3, typer 0.29.2
- Sample scale: 1.0 (1.0 = pre-registered n)
- Suite settings: {'arc': {'n': 300}, 'gsm8k': {'max_tokens': 384, 'n': 100}, 'kl': {'ctx': 256, 'n_passages': 50}, 'perf': {'gen_tokens': 128, 'prompt_tokens': 512, 'repeats': 5, 'threads': 4, 'warmup': 2}, 'refusal': {'max_tokens': 64, 'n_benign': 50, 'n_harmful': 100}, 'seed': 0}

## Limitations

- Results describe the model family named in the report, not LLMs in general.
- Latency and memory are CPU-only and describe the machine recorded in the environment block.
- Sample sizes are finite. A null result means the study did not detect a difference, not that none exists.
- The refusal classifier is a regex list and has not been validated by a human yet.
