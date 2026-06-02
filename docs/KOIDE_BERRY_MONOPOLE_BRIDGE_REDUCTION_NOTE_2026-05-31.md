# Koide Berry-Monopole Bridge Reduction: native circulant gives Q=1; Q=2/3 remains the chiral/nonzero-Berry criterion

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** source-side bridge reduction only. The runner verifies a
native `C_3` index map, zero Berry curvature for the native circulant mass, and
a two-band comparison in which a `Gamma_chi`-anticommuting coupling carries
nonzero Berry curvature. It does not derive the existence of that chiral
coupling in the framework, approve an import, or set an audit verdict.
**Primary runner:**
`scripts/frontier_koide_berry_monopole_bridge_reduction_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_berry_monopole_bridge_reduction_2026_05_31.txt`.

## Result (one sentence)

The native circulant generation mass has a choice-free `C_3` index map,
`b`-independent Fourier eigenvectors, and zero Berry curvature, so it lands on
the second-order/per-dimension `Q=1` branch; the observed `Q=2/3` value remains
pinned to the separate chiral/nonzero-Berry coupling criterion rather than being
derived by this native mass.

## What builds, natively

**The index-map is native and choice-free (F1).** The 3 generations are `Lambda^1(C^3)`
with `C_3` the cyclic shift `C`; the `C_3` DFT `F` diagonalizes `C`, and the
Fourier-grade projection `(1/3)Tr(C^-1 H) = b` identifies `b` as the **`C_3`-doublet
Fourier amplitude** of `H = aI + bC + b-bar C^2` (`a` the singlet amplitude). Only
`arg(b)` (Brannen `delta`, `Q`-orthogonal) and orientation are convention.

**The native effective-action order is second (Q=1) -- derived, not assumed (F2).**
On the real circulant coordinate plane
`H = aI + u(C + C^2) + v i(C - C^2)` matching the Fourier-amplitude
coordinates from F1, the Berry curvature of the filled band is **zero**
(plaquette Berry `~1e-16`) by **eigenvector rigidity**: the eigenvectors are the
**`(u,v)`-independent** Fourier modes (verified `|<Fourier_k|eigvec>| = 1`), so
the doublet coordinate shifts eigenvalues without rotating eigenvectors. Zero
Berry supplies the bounded support for the second-order/per-dimension branch;
F4 verifies that branch as `Q=1`.

## The unification (the payoff)

The two-band comparison isolates **one** computable criterion (F3): a coupling
that **anticommutes** with the chiral grading `Gamma_chi` (`= sigma_z`; e.g.
`u sigma_x + v sigma_y`) carries a **nonzero Berry monopole**, while a coupling
that **commutes** with `Gamma_chi` has **zero** Berry. Within the existing
Koide block-weight frontier, this is the criterion that would have to be
supplied to use the `r=1/2` / per-block branch:

> **`first-order / per-block / det_C / equal-block / Q=2/3` requires the
> `Gamma_chi`-anticommuting (chiral) / nonzero-Berry branch**, while
> **`second-order / per-dim / det_R / trace / Q=1` is the native
> `Gamma_chi`-commuting / zero-Berry branch.**

This criterion aligns the previously separate axes -- effective-action order,
the `det_C`-vs-`det_R` reality type (the native Kähler-Dirac `D_KD` is
real-antisymmetric, hence Majorana/Pfaffian/per-dimension), and the
equal-block-vs-trace measure -- around one operator question: chiral vs
non-chiral generation mass. The runner does **not** derive `Q=2/3` from the
bare native `H[b]`; it derives the native zero-Berry branch and demonstrates
the separate chiral/nonzero-Berry criterion that would be needed for the
`Q=2/3` branch. The per-block count is orientation-blind, so this is about the
chiral coupling existing, not a `+i`/`-i` orientation choice.

## The native mass is non-chiral → Q=1

Every native circulant `Lambda^1` mass **commutes** with `Gamma_chi = 2 P_singlet - I`
(itself circulant): `[H, Gamma_chi] = 0`, so `{H, Gamma_chi} != 0` — it **never**
anticommutes (F4). Hence the native branch is zero-Berry and gives `Q=1`, while
`Q=2/3` (`r=1/2`) is a tuned point on the `Gamma_chi`-commuting family unless a
separate chiral/nonzero-Berry mechanism is supplied. The `Q=2/3` value remains
the chiral criterion/import boundary shared with the generation-identification
gate.

## Boundary

This is **not** a derivation of `Q=2/3`; it is a bridge-reduction. The index-map
is native; the native circulant branch is bounded to `Q=1`; and the missing
positive route is pinned to a single computable criterion (chiral mass /
nonzero Berry monopole). On the generation `R^3` factor the chiral grading is
blocked by the bounded
[KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md):
`comm(C) cap anticomm(Gamma_chi) = {0}` for the native circulant algebra. This
does not rule out a chiral factor sourced outside the generation `R^3`.

**The next path** (not foreclosed): `C^3=I` blocks a chiral grading **sourced from the
generation `R^3`**, but does **not** touch one sourced from a tensor factor **distinct**
from the generation `R^3` (a separate-factor / Connes-Lott-type direction). The sharp,
not-yet-computed question: can an **off-generation** factor (a horizontal/`2`-Higgs
factor) supply a `Gamma_chi`-anticommuting coupling `-> ` nonzero Berry monopole `-> `
`Q=2/3` **without** breaking `C^3=I` on the generation factor? (The qubit-factor route is
already shown import-sourced and `r`-non-selective; the spacetime `gamma_5` acts
`C_3`-trivially.)

## Anchors (live-ledger tiers)

Load-bearing authorities:
[KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
[KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md),
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md),
[KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md),
[STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md),
and
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md).

Non-load-bearing lane context: K0-real / real-Wedderburn-block and
orientation-blind count / B-field gate companion work, if landed separately,
can sharpen the same criterion without changing this note's bounded boundary.
