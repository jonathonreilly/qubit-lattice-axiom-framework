# The Declared RG Convention Is Energy-Covariant: Every E-Slice Collapses to the One Map in the Shifted Quotient Coupling h = t/(μ−E) (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_energy_covariant_rg_collapse_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_energy_covariant_rg_collapse_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=8 FAIL=0` — exact dense linear algebra.

## The claim

For the uniform free chain under `b = 2` odd-sublattice Schur decimation at every
**admissible** instance (`μ != E`, with chart `|h| < 1/√2` for the displayed
projective map), the algebra closes and the shift identity
`μ′ − E = (μ − E)(1 − 2h²)` holds exactly, so in the **shifted quotient coupling**
`h = t/(μ − E)` the flow is **E-independent**: `h′ = h²/(1 − 2h²)` — the same map as
the declared `E = 0` convention. The runner then samples this exact identity
away from the singular point and probes the chart boundary.

## Algebraic core

On the uniform periodic free chain, after splitting even and odd sites, the
odd block at fixed energy is

```text
H_oo - E I = (μ - E) I.
```

For `μ != E`, the Schur complement is therefore

```text
H_eff(E) = H_ee - H_eo ((μ - E) I)^(-1) H_oe.
```

Each retained even site couples through the two neighboring odd sites. Hence
the effective uniform parameters are

```text
μ′ = μ - 2 t²/(μ - E),
t′ = t²/(μ - E).
```

Writing `h = t/(μ - E)` gives

```text
μ′ - E = (μ - E)(1 - 2h²),
h′ = t′/(μ′ - E) = h²/(1 - 2h²).
```

This is the theorem object. The dense runner checks the formula on sampled
finite rings, verifies the singular `μ = E` gate, and records the threshold,
length, sign-quotient, and chart-boundary diagnostics.

## Findings (runner `PASS=8`)

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
