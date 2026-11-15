# checks/ct1_criteria.md — pre-registered criteria for ct1 (CONST-T arithmetic)

Written 2026-10-28, BEFORE `ct1_moser.py` exists. Owner: the (CONST-T) worker. These criteria contain no constant
derived in this session; every number below is either classical (a series sum, a power of 2) or quoted from
REVIEW_SQ_S4 / SQ.md (1e13, 2048, R_0 = 64/128, |∇ζ| ≤ 4/r, p_i = 2·2^i, r_i = R/2 + R2^{-i-3}, i_* = ⌊log_2 R⌋ - 6).

## What ct1 computes

Pure arithmetic on the Moser telescope of SQ.md §15.1 step (6). No physics, no lattice, no BLAS, single thread,
exact `Fraction` where the quantity is rational and `float`/`Decimal` only for logs and powers. No numeric lock
(trivially cheap). Three blocks:

- **Block A — telescope identities.** The series Σ_{i≥0} 1/p_i, Σ_{i≥0} i/p_i, Σ_{i≥0} (i+1)2^{-(i+1)} for
  p_i := 2·2^i, and the β-products Π_{i<i_*} β_i^{m/p_i} with β_i := p_i - 1, for m ∈ {2, 4, 8}.
- **Block B — radius schedules.** For a schedule of gaps (d_i)_{i<i_*} with Σ d_i ≤ budget and min_i d_i ≥ d_min,
  the dimensionless schedule factor F := R² · Π_{i<i_*} d_i^{-2/p_i}. Two schedules:
  - **written**: d_i = R·2^{-i-4}, i_* = ⌊log_2 R⌋ - 6 (SQ.md l.1498-1503, budget R/8, d_min = 4);
  - **optimised**: d_i ∝ 2^{-i} with Σ d_i = R/2 - 4 and i_* the largest index with min gap ≥ d_min.
  F is scanned over R.
- **Block C — assembly.** C_T = √6 · F · (Π β_i^{m/p_i}) · Ĉ with Ĉ the one-step analytic constant, evaluated on a
  table of SUPPLIED values for its factors, plus a one-factor-at-a-time sensitivity.

## PASS / FAIL verdicts (pre-registered)

- **A1.** Σ_{i≥0} 1/p_i = 1/2 · Σ_{i≥0} 2^{-i} = 1 exactly, and Σ_{i≥0} (i+1)2^{-(i+1)} = 2 exactly.
  **PASS** iff both reproduce to within 1e-12 of 1 and 2 under truncation at i = 200.
- **A2.** Π_{i<i_*} β_i^{m/p_i} < 2^{2m} for every i_* ≤ 60 and every m ∈ {2, 4, 8}, and the products increase in i_*.
  **PASS** iff both hold. **FAIL** if any product reaches or exceeds 2^{2m}, which would mean the telescope bound
  2^{2m} used in the write-up is wrong.
- **B1 (the written schedule).** With d_i = R2^{-i-4} and i_* = ⌊log_2 R⌋ - 6, the maximum of F over
  R ∈ {64, 65, …, 2^{18}} is attained at R = 128 and equals 2048 ( = 2^{11} ) to within 1e-9 relative.
  **PASS** iff the argmax is R = 128 and the value is 2048 ± 1e-9 relative. **FAIL** otherwise — in particular a
  value larger than 2048, or an argmax above 128, would contradict REVIEW_SQ_S4 S4-6's reading that the binding
  case is the smallest admissible R.
- **B2 (R_0 = 64 runs zero steps).** At every R ∈ [64, 127] the written schedule has i_* ≤ 1.
  **PASS** iff i_* = 1 for R ∈ [64, 127] and i_* = 0 for R < 64, confirming REVIEW_SQ_S4 S4-6 independently.
- **B3 (the optimised schedule beats the written one).** With budget R/2 - 4 and d_min = 12, the maximum of F over
  R ∈ {32, …, 2^{18}} is **< 128** ( = 2^7 ).
  **PASS** iff max F < 128. **FAIL** iff max F ≥ 128 — in that case the radius schedule is NOT a usable lever and
  the write-up must say so.
- **B4 (proportional allocation is optimal).** For fixed i_* and budget, the allocation d_i ∝ 2^{-i} minimises
  Π d_i^{-2/p_i}. **PASS** iff, on a random sample of 2000 admissible perturbed allocations at each of
  i_* ∈ {2, 3, 4, 5} (budget 1, no d_min constraint), none gives a smaller Π d_i^{-2/p_i} than the proportional one
  (tolerance 1e-12 relative). **FAIL** iff any sample beats it, which would mean the written geometric schedule is
  not the optimum and a better one must be found.
- **C1 (reported, not pass/fail).** The assembled C_T at each row of the parameter table, and the sensitivity. This
  block has no pre-registered verdict because its inputs are constants I must SUPPLY (they are not stated in SQ.md);
  its output is reported with the supplied values named, and the **downstream verdict** against the threshold
  C_T ≲ 1e13 (REVIEW_SQ_S4 S4-16) is read off it in CONST_T.md, where each supplied value is labelled.

## Anything run after the first look at the output is labelled post-hoc

If I add a row, a schedule or a sensitivity probe after seeing output, it is marked `[post-hoc]` in both the script
and CONST_T.md.
