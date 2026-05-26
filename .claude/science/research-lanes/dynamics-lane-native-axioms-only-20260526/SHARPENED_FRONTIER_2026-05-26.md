# Sharpened Frontier — The Bridge Requires Lifting to Full D_st (Not 3×3 Reduction)

**Date:** 2026-05-26 (post-derivation-attempt sharpening)
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Type:** frontier sharpening (negative attempts → positive structural insight)
**Status:** **the open frontier is sharper than the panel reversal stated, with a concrete next-attack target**.

## What two independent derivation attempts found

Two parallel agents attempted to derive the bridge `δ_Brannen = η_APS = 2/9` from different angles (APS-index theorem; Berry-holonomy direct computation). Both failed in the same way:

### Finding 1 — Berry holonomy is IDENTICALLY ZERO on the 3×3 Brannen circulant

For the family `H(a,b) = a·I + b·C + b̄·C²` parameterized by δ = arg(b):

- The eigenstates of `H(δ)` are **δ-independent**: they are always the three C₃ characters `|k⟩ = (1/√3)(1, ω^k, ω^{2k})` for `k ∈ {0,1,2}`.
- The Berry connection `A_k(δ) = i⟨ψ_k(δ)| ∂_δ |ψ_k(δ)⟩ ≡ 0` identically (because the eigenvectors don't depend on δ).
- Therefore the Berry phase around ANY closed loop in parameter space is `γ_k = 0` for all three irreps.

**Numerically verified to machine precision (~1e-15).**

**Apparent nonzero Berry phases in eigenvalue-ordered basis are artifacts of band-swapping at level crossings, not geometric phase.** Once states are labelled by C₃-character (the only invariant labelling), Berry holonomy is identically zero.

### Finding 2 — The comparison MUST happen at the full `D_st` level

The Brannen circulant is the **C₃-character-diagonalized form** of a larger operator on Cl(3)⊗Z³. The diagonalization to circulant form **destroys** the Berry structure. To compare with `η_APS` (which lives at the equivariant Dirac level), the comparison must be done at the full staggered-Dirac `D_st` level **before** the projection to the 3×3 circulant.

Specifically:
- At D_st level: BZ-corner momentum-dependent eigenstates, non-trivial bundle, Berry curvature potentially non-zero.
- After C₃-character projection: circulant form, trivial bundle, zero Berry phase.

The bridge claim `δ_Brannen = η_APS` is therefore **not even formulable at the 3×3 reduced level** — it must be a claim about the full D_st operator's spectral structure at the body-diagonal Z₃ fixed locus.

### Finding 3 — Hirzebruch signature defect independently gives 2/9

The **Hirzebruch signature-defect formula** (different from APS-η but related):
```
σ_def(p; w_1, w_2) = -(1/p) Σ_{k=1}^{p-1} ∏_j cot(π·k·w_j / p)
```
gives σ_def(3; (1,2)) = **2/9 exactly** (sympy-verified).

So there are now THREE independent native routes producing 2/9 at d=3:
- APS-η equivariant fixed-point formula (cyclotomic, `(ω-1)(ω²-1)=3`)
- Hirzebruch signature defect (cotangent sum)
- Plancherel-Frobenius rational `2/d²` (representation theory)

All three coincide at d=3 and disagree at d≠3 (per `KOIDE_TWO_29_ROUTES_DISTINCT`). This is structural multi-witness consistency.

### Finding 4 — No unit convention is FORCED by retained structure

Three candidate conventions explicitly tested:

| Convention | `δ_Brannen` | Match PDG (δ ≈ 0.222 rad)? |
|---|---|---|
| (a) `δ = 2π·η_APS` (Berry-loop convention) | `4π/9 ≈ 1.396` | NO |
| (b) `δ = η_APS` (period-1-rad convention) | `2/9 ≈ 0.222` | YES |
| (c) `δ = (2π/3)·η_APS` (C₃-orbit period rescaling, per bridge agent) | `4π/27 ≈ 0.465` | NO |
| (d) `δ = π·η_APS` (Witten `e^{iπη}` factor) | `2π/9 ≈ 0.698` | NO |

**Only (b) matches PDG, and it is the period-1-rad convention the retained no-go declared non-canonical.**

The bridge-derivation agent's "C₃ orbit period = 2π/3" claim is **refuted by numerical PDG comparison**.

## The sharpened frontier

The actual open frontier is now:

> **OPEN BRIDGE PROBLEM:** Lift the comparison `δ_Brannen ↔ η_APS` to the full staggered-Dirac D_st level. Specifically: compute the Berry curvature of D_st's eigenstate bundle over the BZ-corner momentum-region containing the body-diagonal Z₃ fixed locus, integrate around a C₃-orbit-fixed-locus encircling loop, and check whether the integrated holonomy equals `2π·η_APS = 4π/9`. If yes, an additional `1/(2π)` rescaling is required to land at PDG δ ≈ 2/9 rad — for which NO retained structure currently provides justification.

This is **substantially sharper** than "the bridge requires a descent normalization". The open work has TWO concrete pieces:

1. **Lift the bridge to D_st level**: compute Berry curvature explicitly at the C₃[111] fixed locus.
2. **Derive the unit-conversion factor**: either show 2π·η = δ_Brannen (Berry convention) or that an alternative `1/(2π)` rescaling is forced.

Both are well-defined math problems. Both are tractable.

## What survives from the panel reversal

- ✓ η(1,2; 3) = 2/9 exactly (cyclotomic, machine-precision verified, three-independent-route witness)
- ✓ L-W does not block the route (η is rational mod ℤ)
- ✓ `NEW_PARITY_IS_CIRCULANT_PHASE` (`retained_bounded`) gives δ a canonical basepoint at δ=0
- ✓ At d≠3 the route gives different values; the d=3 agreement is structurally unique

## What's been retracted

- ✗ "The APS-η route closes δ=2/9" — overstated; the bridge identification is open at the D_st level
- ✗ "The period-1-rad convention is forced by the C₃ orbit" — refuted; the C₃-orbit period gives 4π/27, not 2/9
- ✗ "The bridge has most upstream pieces retained" — only 1 of 7 truly retained; bridge is at best audited_conditional

## What's been newly established by this cycle

- The 3×3 Brannen circulant carries NO Berry holonomy (eigenstates δ-independent)
- The bridge MUST be formulated at the D_st level, not the circulant level
- Three independent formulae give 2/9 at d=3 (APS-η cyclotomic; Hirzebruch cot; Plancherel-Frobenius)
- The unit-reconciliation is genuinely unforced; no convention matches PDG natively except the period-1-rad reading

## Concrete next-attack targets

1. **Construct `D_st` explicitly on a small Z³ lattice** (e.g., 4³ APBC) with Cl(3) per-site carrier. Use existing retained staggered-Dirac substep-1 (Grassmann) + substep-3 (BZ-corner Hamming) machinery.

2. **Identify the body-diagonal Z₃ fixed locus** at BZ corner π=(π,π,π) on this lattice. The hw=1 orbit `L_1 = {e_1, e_2, e_3}` is the locus.

3. **Compute the equivariant Berry curvature** of D_st's eigenstate bundle near the fixed locus.

4. **Integrate around a small encircling loop** to get the Berry holonomy.

5. **Compare** to `2π·η_APS = 4π/9` and to literal `η_APS = 2/9`. Whichever matches numerically is the right convention.

This is a CONCRETE numerical computation. ~1-2 days of careful lattice numerics for the lane to execute.

## Status of the lane

The lane has produced, in this user-directed campaign:

- Foundation work (charter + dependency map + Chain 5 verification)
- A 12-cycle "bounded no-go" that was WRONG
- Panel reversal that was OVERSTATED
- Hostile review that found the overstatement
- Two derivation attempts that found the SHARPER frontier
- A precise concrete next-attack target

This is genuine open-frontier research: the wall structure is now precisely known, the closure routes are enumerated, and the next computation is well-defined. **The δ=2/9 derivation is not done — but the problem is now narrowed to a specific, tractable lattice Berry-curvature computation at the D_st level with a clear unit-reconciliation question.**

## Memory update

The lesson: panel exercise + hostile review + independent derivation attempts work together. Each step refines the frontier. Don't stop at "panel found a route" — drive each route to either closure or sharpened-residual via independent attempts.
