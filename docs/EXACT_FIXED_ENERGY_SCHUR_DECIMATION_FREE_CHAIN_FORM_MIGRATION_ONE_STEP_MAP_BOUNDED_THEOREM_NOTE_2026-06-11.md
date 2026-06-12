# Exact Fixed-Energy Schur Decimation on the Free Staggered Chain: Resolvent-Exact Downfolding, Form Migration (Staggered → Uniform + NN), and the Closed One-Step Map on Disjoint Grids (Bounded)

**Date:** 2026-06-11
**Type:** bounded_theorem (ST4's first positive exact datum; owner-directed "work through the alternatives in order"; panel-narrowed)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_exact_fixed_energy_schur_decimation_free_chain_2026_06_11.py`
**Cache:** `logs/runner-cache/frontier_exact_fixed_energy_schur_decimation_free_chain_2026_06_11.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=6 FAIL=0` (six
consolidated blocks, exact dense linear algebra at `N ≤ 16`, deterministic, memory
trivial).

## The object

The renormalization sub-target (ST4) has had almost no framework-native positive
surface (the shell-averaging coarse-grained helper and the block-spin CP no-go —
cited as the prior surfaces). This note lands its first positive exact datum: the
**fixed-energy Schur-complement decimation (downfolding)** of the odd sublattice on
the free 1D staggered chain,
`h_eff(E) = h_ee − h_eo (h_oo − E)⁻¹ h_oe`, on the `E = 0` slice. **This is an exact
decimation step, not yet an RG transformation**: no rescaling/normalization
convention is performed and no post-migration flow space is declared — composing
this step with a rescaling convention into a genuine RG map is the named open
follow-on, not a claim of this note.

## The findings (runner `PASS=6`)

**(D1) The step is exact for `m ≠ 0`** — no truncation: the retained-site block of
the full resolvent equals the resolvent of `h_eff` to `7×10⁻¹⁶` (`m ∈ {0.3, 1.5}`).
The `m = 0` case is **singular at `E = 0`** and is checked only as a zero-mode-projected
Moore–Penrose diagnostic — a convention, disclosed and kept separate from the `m ≠ 0`
theorem.

**(D2) Form migration, measured — not forced.** The decimated theory is **not** a
staggered chain again: the exact structure at `E = 0` is **uniform on-site potential
`m + 2t²/m` + nearest-neighbor hopping `t²/m`**, with staggered mass **identically
zero** and no longer-range terms generated (`NNN = 0` **exactly, and analytically
necessary**: in the staggered NN chain `h_oo` is diagonal, so `(h_oo − 0)⁻¹` is
diagonal and every downfolded path passes through a single odd site — coarse range
is exactly NN; panel-verified at `N = 12, 16, 20`). The family migrates (staggered →
uniform + NN) at the first step; that measured fact is the datum.

**(D3) The one-step map is an exact closed form** — anti-fitting guarded: obtained on
one parameter grid, **validated on a disjoint grid** (`2×10⁻¹⁶` / `2×10⁻¹⁵`):

```
diag' = m + 2t²/m ,   t' = −t²/m ,   m'_staggered = 0        (E = 0, m ≠ 0)
```

The `E' = −m − 2t²/m` statement is only the **shifted-energy same-form
representation**, not an energy flow. Large `m` gives the **projective decoupling
statement** `|t'/diag'| → 0` (a ratio statement — `diag'` itself diverges, so no
fixed-point language is used). The `m = 0` line is described only by the projected
diagnostic of D1/D6 (zero staggered component), **not** as a preserved critical
flow.

**(D4) Retained-site physics is invariant**: `G[0,2](0)` agrees pre/post decimation to
`8×10⁻¹⁷` across five seeded random `(t, m)` draws.

**(D5) Schur-complement composition (associativity)**: decimating twice equals
decimating by four in one Schur step (`6×10⁻¹⁷`), verified on the representative
instance — the composition property any iterable coarse-graining must have.

**(D6) The checks have teeth**: dropping the Schur correction (keeping `h_ee` only)
fails the exactness check by `O(1)` (`2.7`); and the `m = 0` projected/regulated
checks show **zero staggered component** (the narrow statement; no critical-flow
claim).

## Scope and the path this opens

Free sector, one dimension, one color (precisely: the free Hamiltonian is
`h ⊗ I_color`, so a single color carries the content), `N = 16` (the composition
check reaches `N = 16 → 8 → 4`; panel probes at `N = 12, 20` agree), the `E = 0`
slice (finite-`E` regulator only where `m = 0` is singular). **Not claimed**: an RG
transformation (no rescaling step; no declared post-migration flow space),
interacting RG, `d = 3`, gauge sectors, continuum limits, c-functions, or any
universality statement. The paths this opens, named as motivation only: (i)
composing the exact step with a rescaling convention into a declared flow space —
the genuine RG map; (ii) the same downfolding on a chain whose hopping carries a
**background composite link** (an `H_cov`-type conditional follow-on — not an ST3
antiscreening closure).

- Standard math (method only): Schur complements; resolvent identities;
  Moore–Penrose pseudoinverse on the zero-mode subspace; linearized fixed-point
  analysis.

No new axiom, primitive, measure, or weight; `r` untouched; discrete throughout. The
audit lane grades.
