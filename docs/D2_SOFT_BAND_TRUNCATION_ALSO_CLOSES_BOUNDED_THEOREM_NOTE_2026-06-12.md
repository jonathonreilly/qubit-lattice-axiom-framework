# Truncation Design in d=2: Even-d² Kept Bands Preserve the Checkerboard Color by Parity (a Lemma — dx²+dy² ≡ dx+dy mod 2), So Both Designs Give H_kd = 0 by Algebra; the Soft Budget Is Smaller at the Measured L = 16/32 (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem (truncation-design follow-on of the d=2 truncated-flow note, in review — cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_d2_soft_band_closure_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_d2_soft_band_closure_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=13 FAIL=0`.

## Findings

Both truncation designs — hard (`d² ∈ {4,8}`) and **soft (`d² ∈ {4,8,16,20}`)** —
leave the kept-to-decimated block exactly zero after truncation (`H_kd = 0`, `L = 16`
and `32`) — and the panel supplied the reason, which reframes this as a **lemma, not
a finding**: `dx² + dy² ≡ dx + dy (mod 2)`, so every **even-`d²`** shell connects
only same-checkerboard-color sites; any even-`d²` kept band therefore cannot couple
the sublattices. The raw post-Schur `H_kd` is nonzero **before** truncation — the
zero is what even-`d²` truncation enforces, by parity. The accumulated three-step resolvent budgets order as **soft < hard at the measured
`L = 16, 32`** (fixed-instance gates — no generic claim; ties appear at some larger
compatible `L` per the panel's wider scan, disclosed); the per-step chart is a
**synthetic checkerboard reassignment** after each Schur step (stated — physical
coarse-lattice geometry is a different object); identity
truncation reproduces the exact pipeline (`10⁻¹²` — a tautological sanity check,
labeled). The named follow-on: resolved by the parity lemma above: ANY even-`d²` band preserves `H_kd = 0`;
the open question is the budget behavior of odd-shell-including designs.

## Scope

Finite-`L`, `E = 0`, free; truncation-design data with measured budgets; no flow
claims. No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
