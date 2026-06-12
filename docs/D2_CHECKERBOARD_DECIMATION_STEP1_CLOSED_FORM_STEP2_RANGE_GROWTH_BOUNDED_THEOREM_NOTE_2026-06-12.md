# Exact d=2 Checkerboard Decimation: Step 1 Has a Closed Three-Coupling Form (and Is E-Covariant); Step 2 Is Range-Unbounded — Dense, Band-Decaying Couplings, With the Wraparound Truncation of Small Boxes Caught In-Runner (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem (the named d>1 follow-on of the declared-RG-convention notes, in review — cross-referenced, not cited as graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_d2_checkerboard_decimation_range_growth_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_d2_checkerboard_decimation_range_growth_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=23 FAIL=0` — exact dense linear algebra, no truncation anywhere.

## Findings

- **Step 1 is closed-form and exact**: on the square lattice the eliminated checkerboard
  sublattice has diagonal `h_oo = μI` (the d=1 property survives — gated), giving exactly
  `diag′ = μ − 4t²/μ`, rotated-NN `2t²/μ`, axial-NNN `t²/μ`, and **nothing beyond**
  (range bound gated at `10⁻¹²`); retained-site resolvent preserved (`10⁻¹⁰`).
- **Step 1 is E-covariant**: the same coefficients with `μ → μ − E` (gated, `E = 0.3`).
- **Step 2 is range-unbounded — the obstruction is stronger than range growth**: the
  step-1 family's eliminated sublattice carries internal couplings (`h_oo` no longer
  diagonal — gated), so its inverse is dense and the exact second step generates
  couplings at **all** distances. The wraparound probes caught this in-runner: the
  `L = 8` table's apparent `d² ≤ 32` bound (and its magnitudes) were
  **box-truncation artifacts** (`d² = 16`: `9.5×10⁻³` at `L = 8` vs `4.7×10⁻³`
  converged); `L = 12/14` show shells through `d² = 72`, near-shell magnitudes
  converge in `L` (5% gates on `d² = 16/20/32`), and the couplings **decay by
  distance band** (`{16,20} > {32,36,40} > {52} > {72}`, far tail `< 10⁻⁵`;
  within-band ordering anisotropic, disclosed). **No finite-range family closes**
  under this `d = 2` checkerboard convention: any truncated flow needs the measured
  tails as its error budget (the named follow-on).

## Scope

Free `d = 2`, exact, no truncation; step-1 closed form + the measured dense-decaying step-2 structure are the data (finite-`L` tables are `L`-limited — stated). Not claimed: any truncated flow, `d = 2` fixed points, interacting or gauge content.
The named follow-on: controlled-truncation conventions with the measured tails as the
error budget. No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
