# Koide: the value reduces to one computable criterion — is the generation mass chiral (nonzero Berry monopole → Q=2/3) or not (Q=1)?

**Date:** 2026-05-31
**Claim type:** bounded_theorem — bridge-reduction (native dynamics bounded to Q=1; the import pinned to one criterion)
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
The audit lane sets status and the per-block-vs-per-dimension convention tier.
**Primary runner:**
`scripts/frontier_koide_berry_monopole_bridge_reduction_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_berry_monopole_bridge_reduction_2026_05_31.txt`.

## Result (one sentence)

Attempting the B-coupling `->` B-field bridge (which would force `Q=2/3`) builds a
native, choice-free index-map and **derives** that the native circulant dynamics gives
`Q=1` (zero Berry, second-order), collapsing the entire charged-lepton Koide-value
question into a single computable operator criterion: **the generation mass is chiral
(`Gamma_chi`-anticommuting, nonzero Berry monopole) `->` `Q=2/3`, or non-chiral
(`Gamma_chi`-commuting circulant, zero Berry) `->` `Q=1`** — and the native mass is
non-chiral.

## What builds, natively

**The index-map is native and choice-free (F1).** The 3 generations are `Lambda^1(C^3)`
with `C_3` the cyclic shift `C`; the `C_3` DFT `F` diagonalizes `C`, and the
Fourier-grade projection `(1/3)Tr(C^-1 H) = b` identifies `b` as the **`C_3`-doublet
Fourier amplitude** of `H = aI + bC + b-bar C^2` (`a` the singlet amplitude). Only
`arg(b)` (Brannen `delta`, `Q`-orthogonal) and orientation are convention.

**The native effective-action order is second (Q=1) — derived, not assumed (F2).**
Integrating out the native circulant Kähler-Dirac fermion, the Berry curvature of the
filled band on the complex-`b` plane is **zero** (plaquette Berry `~1e-16`) by
**eigenvector rigidity**: because `H = aI + Re(b) B + Im(b)(i Jcs)` is circulant, its
eigenvectors are the **`b`-independent** Fourier modes (verified `|<Fourier_k|eigvec>| =
1`), so `b` shifts eigenvalues without rotating eigenvectors. Zero Berry `-> ` no
first-order term `-> ` second-order Ginzburg-Landau `-> ` per-dimension `-> ` `Q=1`.

## The unification (the payoff)

The whole question collapses to **one** computable criterion (F3): a `2`-band coupling
that **anticommutes** with the chiral grading `Gamma_chi` (`= sigma_z`; e.g.
`Re(b) sigma_x + Im(b) sigma_y`) carries a **nonzero Berry monopole**, while a coupling
that **commutes** with `Gamma_chi` has **zero** Berry. So:

> **`first-order / per-block / det_C / equal-block / Q=2/3` `<=>` `Gamma_chi`-anticommuting
> (chiral) coupling `<=>` nonzero Berry monopole**, and
> **`second-order / per-dim / det_R / trace / Q=1` `<=>` `Gamma_chi`-commuting coupling
> `<=>` zero Berry.**

This single criterion **unifies** the previously-separate axes — effective-action order,
the `det_C`-vs-`det_R` reality type (the native Kähler-Dirac `D_KD` is real-antisymmetric
`-> ` Majorana/Pfaffian `-> ` per-dim), and the equal-block-vs-trace measure — into **one
operator pin**: chiral vs non-chiral generation mass. The forward Berry/effective-action
calculation never assumes `Q=2/3` (it derives `F=0 -> Q=1` and `F != 0 -> Q=2/3` from the
bare `H[b]`), so the reduction is **non-circular**. (The per-block *count* is
orientation-blind — prior note — so this is about the chiral coupling **existing**, not a
`+i`/`-i` choice.)

## The native mass is non-chiral → Q=1

Every native circulant `Lambda^1` mass **commutes** with `Gamma_chi = 2 P_singlet - I`
(itself circulant): `[H, Gamma_chi] = 0`, so `{H, Gamma_chi} != 0` — it **never**
anticommutes (F4). Hence native Berry `= 0 -> ` `Q=1`, and `Q=2/3` (`r=1/2`) is a tuned
point on the `Gamma_chi`-commuting family with **no native chiral mechanism** selecting
it. `Q=2/3 = ` the single **chiral import**, shared identically with
generation-identification.

## Boundary

This is **not** a derivation of `Q=2/3`; it is a bridge-reduction. The index-map is
native; the native dynamics is bounded to `Q=1` (derived); and the import is pinned to a
single computable criterion (chiral mass / nonzero Berry monopole). On the generation
`R^3` factor the chiral grading is forbidden: `U(1)_b` is incompatible with `C^3=I`, and
`koide_z3_equivariant_anticommuting_no_go` (retained_bounded) gives
`comm(C) ∩ anticomm(Gamma_chi) = {0}`; the native charges are generation-blind.

**The next path** (not foreclosed): `C^3=I` blocks a chiral grading **sourced from the
generation `R^3`**, but does **not** touch one sourced from a tensor factor **distinct**
from the generation `R^3` (a separate-factor / Connes-Lott-type direction). The sharp,
not-yet-computed question: can an **off-generation** factor (a horizontal/`2`-Higgs
factor) supply a `Gamma_chi`-anticommuting coupling `-> ` nonzero Berry monopole `-> `
`Q=2/3` **without** breaking `C^3=I` on the generation factor? (The qubit-factor route is
already shown import-sourced and `r`-non-selective; the spacetime `gamma_5` acts
`C_3`-trivially.)

## Anchors (live-ledger tiers)

retained / retained_bounded: `koide_z3_equivariant_anticommuting_no_go` (retained_bounded),
`koide_anticommuting_operator_derivation`, `koide_circulant_q_two_thirds_algebraic`,
`koide_q23_block_weight_frontier` (retained_bounded),
`staggered_dirac_substep2_kahler_dirac_equivalence` (retained_bounded),
`cpt_exact_real_anti_hermitian_d`. Complements `KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE`
(canonical) and `KOIDE_ORIENTATION_BLIND_COUNT_B_FIELD_GATE_NOTE`.
