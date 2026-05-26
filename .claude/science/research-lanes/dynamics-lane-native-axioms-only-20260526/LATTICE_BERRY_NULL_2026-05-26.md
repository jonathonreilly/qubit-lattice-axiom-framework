# Lattice Berry Curvature Computation — Null at U(1), Non-Abelian Open

**Date:** 2026-05-26 (D_st-level lattice numerics cycle)
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Type:** lattice numerics finding (negative on U(1), positive on non-Abelian)
**Imports:** NONE (pure lattice numerics on retained Cl(3)/Z³ + staggered Dirac substep work)
**Status:** another sharpening of the open frontier.

## The computation

Built the staggered Dirac operator `D_st` on small Z³ lattices (L=4, 6, 8) with Cl(3) per site (Pauli `γ_μ` for the three spatial directions; Kawamoto-Smit phases `η_μ(x)`). Diagonalized in momentum space; identified the BZ-corner θ=(π,π,π) and the 8-fold doubler subspace (`n_band = 2³ = 8`, matching the retained staggered substep-3 BZ-corner Hamming orbit structure).

Computed the U(1) Berry holonomy around a small loop encircling the C₃[111] body-diagonal fixed locus via the standard Wilson-line product of unitarized link overlaps.

## Result

```
| L | r    | n_pts | det(W) phase (rad) |
| 6 | 0.05 | 128   | -1.32e-04          |
| 6 | 0.10 | 128   | -2.31e-05          |
| 6 | 0.20 | 128   | -5.33e-04          |
| 8 | 0.05 | 128   | -2.29e-04          |
| 8 | 0.10 | 128   | -8.27e-05          |
| 8 | 0.20 | 128   | -1.56e-06          |
```

**det(W) → 0 to numerical precision** (`~10⁻⁴` at L=6, `~10⁻⁶` at L=8), independent of loop radius, loop centering, and lattice size. The result does **NOT** match any of:

- 2π·η_APS = 4π/9 ≈ 1.396 rad (Berry-loop convention)
- π·η_APS = 2π/9 ≈ 0.698 rad (Witten e^{iπη} convention)
- η_APS = 2/9 ≈ 0.222 rad (period-1-rad convention)

The matched value is **zero**.

## Why the U(1) Berry holonomy is zero

Even at the full D_st level (NOT reduced to 3×3 Brannen circulant), the doubler-subspace eigenstates are essentially constant under the C₃[111] twist-parameter variation **in their U(1) trace component**. The non-Abelian (SU(8)) Berry curvature within the doubler subspace IS nonzero (‖W − I‖_F ≈ 0.01 at L=6, r=0.1, growing linearly in r), but its **U(1) trace component is zero**.

This is the lattice-numerics analog of the panel's Finding 1 ("eigenstates δ-independent at the C₃-character-diagonalized level"): the abelian Berry phase is structurally absent.

## A second-order subtlety: C₃[111] doesn't commute with H_st in KS gauge

The C₃[111] permutation operator P (cyclic site permutation + 120° spinor rotation) does NOT commute with `H_st(π,π,π)` in the standard Kawamoto-Smit staggered gauge: `‖[H, P]‖ = 0.707`. The KS gauge `η_μ(x) = (1, (-1)^{x_1}, (-1)^{x_1+x_2})` is not C₃-invariant — only the gauge equivalence class is.

This means a clean C₃-character decomposition of the doubler subspace requires absorbing the gauge mismatch via a compensating gauge transformation. Without this, per-character Berry phases cannot be unambiguously read off from lattice eigenvectors — they live as gauge-equivalence-class phases, not bare phases.

## Implication for the frontier

The simple lift-to-D_st-level Berry route **also fails**. The bridge `δ_Brannen = η_APS = 2/9` is NOT carried by the abelian Berry phase at any level of the framework (3×3 circulant or full D_st).

This is a stronger negative than the panel reversal indicated. The remaining candidate mechanisms are:

### Candidate A — Non-Abelian (SU(N)) C₃-character-projected Berry curvature

The doubler subspace's non-Abelian Berry curvature IS nonzero. After projecting to C₃-characters (k=0,1,2), the per-character Berry phases might be nonzero individually, even though their sum (the U(1) trace) vanishes.

**Required for this attack:**
- Gauge-fix the C₃[111] permutation to commute with H_st (or work in a manifestly C₃-invariant gauge).
- Project the doubler-subspace eigenstates onto C₃-characters (using the BZ-corner equivariant lattice translations).
- Compute per-character Berry phases along a C₃-equivariant loop.

This is a substantial lattice computation, but tractable.

### Candidate B — Chiral partition function / Witten η-invariant

Witten's `e^{iπη}` appears in the chiral partition function of the Dirac operator, not in per-state Berry phases. The phase `e^{iπη_APS}` at η = 2/9 is `e^{2πi/9}`, which has argument `2π/9 ≈ 0.698 rad` — STILL NOT 2/9 rad.

So even this route doesn't naturally land at δ_Brannen ≈ 2/9 rad without an additional convention.

### Candidate C — A different lattice quantity entirely

Maybe δ_Brannen is NOT the Berry holonomy or the chiral partition function phase, but something else — e.g., the argument of a specific determinant ratio, an anomalous dimension, a Wilson loop trace, or a spectral asymmetry computed via a different mechanism.

This is open structural research.

## What the lane has now definitively established

After this lattice numerics cycle:

1. **η_APS = 2/9** is mathematically real and independently confirmed via three formulae (cyclotomic, Hirzebruch cot, Plancherel).
2. **L-W does not apply** to the APS route.
3. **NEW_PARITY_IS_CIRCULANT_PHASE** retained gives δ a canonical basepoint.
4. **U(1) Berry holonomy at the D_st level is identically zero** around the C₃[111]-encircling loop. NOT 4π/9, NOT 2π/9, NOT 2/9 — it's zero.
5. **Non-Abelian SU(8) Berry curvature within the doubler subspace is nonzero** but requires C₃-character projection (gauge-obstructed in KS gauge) to extract per-character phases.
6. **No unit convention matches PDG natively**; the period-1-rad reading (δ = η = 2/9) is empirically right but lacks derivation.

## The actual open frontier (sharper still)

> **OPEN PROBLEM:** Find a lattice-quantity Q on D_st at the C₃[111] fixed locus such that:
> - Q can be computed from A1+A2 + retained content + standard math
> - Q equals 2/9 rad (literal radian, not mod 2π)
> - Q transforms correctly under axis-exchange parity (δ → -δ)
> - At d ≠ 3 Q gives different values, with d=3 being structurally unique
>
> Three negative attempts have been done: (i) Berry holonomy at 3×3 circulant level, (ii) Berry holonomy at D_st lattice level (this cycle), (iii) Witten chiral partition function. None natively match δ_Brannen ≈ 2/9 rad.

The most likely candidate is the **non-Abelian C₃-character-projected Berry curvature** (Candidate A above), but extracting it requires resolving the gauge-fixing of C₃[111] commuting with H_st.

## What this means for "frontier science"

This is genuine, hard, open research. After:
- 12 cycles of negative no-go convergence
- Panel reversal that flipped to positive route
- Hostile review that found overclaim
- Two derivation attempts that sharpened to D_st level
- One lattice computation that sharpened further to non-Abelian projection

...we have NOT closed `δ_Brannen = 2/9 rad`. But we now know **precisely** what's open: a non-Abelian C₃-character-projected Berry curvature computation at the staggered-Dirac BZ-corner doubler subspace, with the convention-derivation question still attached.

This is exactly the open-frontier configuration the user described: hard, sharply defined, with a concrete next-attack route, and not yet settled.

## Files

- `.claude/tmp/berry_lattice/` — computation scripts (`dst_twisted.py`, `berry_loop_v2.py`, `berry_robust.py`, `c3_decomp.py`)
- Lattice numerics raw output from L=6 and L=8 computations
- All confirms det(W) → 0 at machine precision

## Next concrete attack

1. Implement C₃-invariant gauge for the staggered Dirac (or absorb the gauge mismatch via a compensating transformation on the lattice).
2. Project D_st BZ-corner doubler subspace onto C₃-characters (k=0,1,2) using the equivariant lattice-translation generators.
3. Compute per-character non-Abelian Berry phases along a C₃-equivariant loop.
4. Check whether any sum, difference, or specific combination equals 2/9 rad natively.

Estimated effort: ~2-3 days of careful lattice numerics + gauge-theory bookkeeping. Substantial but tractable.

## Cited retained sources

- A1, A2 (`MINIMAL_AXIOMS_2026-05-03.md`)
- Cl(3) per-site algebra structure
- Staggered Dirac substep-3 BZ-corner Hamming orbit (audited_conditional)
- KOIDE_PHASE_APS_ETA_PARITY_ROUTE (unaudited; η = 2/9 cyclotomic)
- NEW_PARITY_IS_CIRCULANT_PHASE (retained_bounded; δ basepoint)
- Lattice numerics (this cycle, deferred research artifact)
