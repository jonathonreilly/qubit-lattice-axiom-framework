# checks/r55u_3_criteria.md — Opus 5.5 reviewer (REVIEW55_TUNIF), written 2026-10-28T22:42:35Z UTC, BEFORE r55u_3_interp.py exists

## What is tested
The admissibility correction used by TUNIF Theorem TU-6 (and NLOC Theorem NL-3 step (3)): NORMS Lemma N1-6's nested
multilinear interpolant λ̂ of a coarse scalar μ, as an operator H on the coarse gradient h := d_k μ. Codex
CODEX_REVIEW_TUNIF F6 supplies, and I re-derived by hand, the two bounds
  ||d λ̂||_inf <= s^{-1} ||d_k μ||_inf   and   ||d λ̂||_1 <= s^{d-1} ||d_k μ||_1,   s := L^{k-j} (fine cells per coarse cell),
which are what make the correction harmless to BOTH the sup leg and the column-l1 leg (T-free). Exact rationals only.

## Instances (fixed here)
d in {2, 3}; coarse torus side Tc = 3; s in {3, 9}; mu random rationals on coarse sites (random.Random(7171)), 5 instances
per (d, s), plus the single-site bump mu = delta_0 for each (d, s).

## Pre-registered verdicts
- r55u_3-A (interpolation exact at coarse sites): λ̂ = μ at every coarse site. PASS iff zero discrepancies.
- r55u_3-B (sup bound): max|d λ̂| <= s^{-1} max|d_k μ| in every instance. PASS iff it holds everywhere.
- r55u_3-C (l1 bound): sum|d λ̂| <= s^{d-1} sum|d_k μ| in every instance. PASS iff it holds everywhere.
- r55u_3-D (nestedness, s = 9 only): the s = 9 interpolant restricted to the points = 0 mod 3, re-interpolated with s = 3,
  reproduces the s = 9 interpolant exactly. PASS iff zero discrepancies.
- r55u_3-E (designed-FAIL control): the stronger l1 bound sum|d λ̂| <= s^{d-2} sum|d_k μ| must FAIL in at least one
  instance. Fires iff so (otherwise r55u_3-C is not testing the exponent).
