# The Declared RG Convention Is Energy-Covariant: Every E-Slice Collapses to the One Map in the Shifted Quotient Coupling h = t/(μ−E) (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem (the named E≠0 follow-on of the declared-RG-map note, which is in review — cross-referenced, not cited as graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_energy_covariant_rg_collapse_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_energy_covariant_rg_collapse_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=6 FAIL=0` — exact dense linear algebra.

## The claim

For the uniform free chain under `b = 2` odd-sublattice Schur decimation at every
**admissible** instance (`|μ − E|` bounded away from the odd-block spectrum — gated
over the actual sample list, with the singular `μ = E` point probed and excluded;
chart `|h| < 1/√2`), the algebra closes and the shift identity
`μ′ − E = (μ − E)(1 − 2h²)` holds exactly, so in the **shifted quotient coupling**
`h = t/(μ − E)` the flow is **E-independent**: `h′ = h²/(1 − 2h²)` — the same map as
the declared `E = 0` convention. On the admissible domain, the `E = 0` theorem is
the general-`E` theorem.

## Findings (runner `PASS=6`)

- **Closure at `E ≠ 0`** (three energies × four `(t,μ)` points): uniform + NN exactly;
  the shift identity at `4×10⁻¹⁶`; **the collapse at `1.4×10⁻¹⁷`**.
- **Threshold covariance**: `E` inside the band ⟺ `|μ − E| ≤ 2|t|` ⟺ `|h| ≥ 1/2`, spectrally checked
  (gapped below; min-eigenvalue collapse `N = 64 → 128` above — a commensurate
  finite-`N` witness, not the proof).
- **The energy-resolved length**: `ξ_E = 1/arccosh(1/2|h|)` measured against the
  `E`-resolvent decay on `N = 128` (`10⁻³` relative), with the composition
  `ξ_E(h′)/ξ_E(h) → 1/2` near threshold.
- **Quotient and chart inherited**: the sign quotient (staggered-gauge unitary
  equivalence) holds at `E ≠ 0`; the chart boundary is **tested, not just
  disclosed** (`|h′| > 50` just below `1/√2`); evenness verified; the `μ = E`
  singularity detected and excluded by gate.

## Scope

Free sector, 1D, the declared `b = 2` Schur convention, now one map for the whole
energy family in the shifted quotient coupling. Not claimed: interacting, `d = 3`,
gauge sectors, universality beyond the convention. Standard math (method only):
Schur complements; `arccosh` dispersion lengths.

No new axiom, primitive, measure, or weight; `r` untouched. The audit lane grades.
