# ts55_3 — criteria (pre-registered before any script exists)

Written by the TSE55 worker (claude-opus-5-5); UTC stamp in the record line below. Script to be written AFTER this file:
`checks/ts55_3_flow.py`. Exact rationals only.

## What is tested
The level-summation lemmas of TSE55 §3.3–§3.4 (Lemma SUM, Lemma AF-cmp) on synthetic coupling sequences that satisfy the
pairwise flow bracket (FLOW-pw):  b_−(n − j) − R_F ≤ u_j − u_n ≤ b_+(n − j) + R_F  for all 0 ≤ j ≤ n ≤ K,
with b_± := β_±·log L treated as given positive rationals (the lemmas use log L only through b_±), and u_K − R_F ≥ γ⁻² = 1.
Parameters (fixed now): L = 3; (b_−, b_+, R_F) ∈ {(1/4, 1, 1/2), (1/2, 3/2, 1), (1, 1, 0)}; K = 60; u_K = 1 + R_F + 1/3.
Sequences: (i) slowest admissible (u_j − u_{j+1} = b_− for all j); (ii) fastest (= b_+); (iii) 40 random sequences built
level by level with increments drawn from [b_− − R_F/2, b_+ + R_F/2] ∩ (1/12)Z, kept only if the full pairwise bracket holds
(checked over all pairs). Matched levels k ∈ {0, 5, 10, …, 55}.

## Gates
- **S1 (coarse sum, canonical weights).** For s ∈ {2, 3}: Σ_{n=0}^{K−k} u_{k+n}^{−s}L^{−8n} ≤ C_co(s)·u_k^{−s} with
  C_co(s) := 2^s/(1 − L^{−8}) + γ^{2s}·T_s/(1 − L^{−8}), T_s := max over u ≥ u_K of u^s·L^{−8⌈(u/2 − R_F)/b_+⌉} (evaluated exactly:
  on each interval where the ceiling is constant the maximum is at the right end), whenever u_k ≥ 2R_F + 2.
  PASS iff it holds for every sequence, s, k with u_k ≥ 2R_F + 2.
- **S1-F (control, must FAIL): without canonical weights.** Σ_{n=0}^{K−k}u_{k+n}^{−2}·u_k² must exceed 10 for the slowest
  sequence at k = 0 under (b_−, b_+, R_F) = (1/4, 1, 1/2) (expected: it grows like u_k/b_−, i.e. the per-level bound without
  the L^{−8n} factor gives no u_k^{−2} envelope).
- **S2 (AF comparison, coarse side).** Σ_{n=0}^{K−k}|1/u_{k+n} − 1/u_k|·L^{−4n} ≤ C_cmp^{co}·u_k^{−2}, with
  C_cmp^{co} := 2Σ_{n≥0}(b_+n + R_F)L^{−4n} + γ²·V, V := max over u ≥ u_K of u·(b_+(⌈(u/2−R_F)/b_+⌉) + R_F + b_+/(1 − L^{−4}))·
  L^{−4⌈(u/2 − R_F)/b_+⌉}/(1 − L^{−4}), whenever u_k ≥ 2R_F + 2. PASS iff it holds for all sequences and k.
- **S2-F (control, must FAIL):** the same sum must exceed (1/10)·u_k^{−1}·u_k^{−1}·u_k = (1/10)u_k^{−1}·... — precisely: the
  quantity u_k²·Σ_n|1/u_{k+n} − 1/u_k| (no L^{−4n} weight, n up to K − k) must exceed 10·C_cmp^{co} for the slowest sequence at
  k = 0, (1/4, 1, 1/2) — i.e. the canonical weight is what makes the comparison O(u_k^{−2}).
- **S3 (fine side).** For i < k (n = k − i ≥ 1) with the summable test weight ω_n := L^{4n}·2^{−L^n}:
  Σ_{n=1}^{k}|1/u_{k−n} − 1/u_k|·ω_n ≤ 2u_k^{−2}Σ_{n≥1}(b_+n + R_F)ω_n whenever u_k ≥ 2R_F + 2. PASS iff it holds throughout.

## Verdict rule
ts55_3 PASS iff S1, S2, S3 PASS and S1-F, S2-F behave as stated. Otherwise FAIL, recorded as such.

## What this check cannot decide
These are arithmetic lemmas about admissible sequences; the check can fail only if the lemmas' constants or their structural
claim (O(u_k^{−s}) with canonical weights) are wrong. It does not test that Yang–Mills' couplings obey (FLOW-pw).

## Clarification of S2-F (appended 2026-10-29T06:08:21Z, before any ts55_3 script exists; it replaces the garbled first clause of S2-F)
S2-F reads exactly: for the slowest sequence at k = 0 with (b_-, b_+, R_F) = (1/4, 1, 1/2), the unweighted quantity
u_k^2 * Sum_{n=0}^{K-k} |1/u_{k+n} - 1/u_k| must exceed 10 * C_cmp^co. Nothing else in S2-F is a condition.

## Record
- criteria file completed 2026-10-29T06:08:21Z (date -u); no script for ts55_3 exists at this time.
