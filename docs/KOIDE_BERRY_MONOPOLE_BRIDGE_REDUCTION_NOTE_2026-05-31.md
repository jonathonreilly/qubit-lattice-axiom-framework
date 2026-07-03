# Koide Berry-Monopole Bridge Reduction: finite native algebra only; Q-branch selection remains open

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** finite source-side algebra only. The runner verifies a
native `C_3` index map, zero Berry curvature for the native circulant mass, a
two-band comparison in which a `Gamma_chi`-anticommuting coupling carries
nonzero Berry curvature, the native circulant commutation obstruction, and the
standalone algebraic identities `Q(r=1/2)=2/3` and `Q(r=1)=1`. It does **not**
derive any Berry/chirality-to-`r` weighting rule, select a physical `Q` branch,
derive the existence of a framework chiral coupling, approve an import, or set
an audit verdict.
**Primary runner:**
`scripts/frontier_koide_berry_monopole_bridge_reduction_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_berry_monopole_bridge_reduction_2026_05_31.txt`.

## Result (one sentence)

The native circulant generation mass has a choice-free `C_3` index map,
`b`-independent Fourier eigenvectors, and zero Berry curvature, while a separate
toy two-band anticommuting comparator has nonzero Berry curvature; this packet
does not derive a rule that assigns either Berry fact to an `r` weighting or a
physical `Q` branch.

## What builds, natively

**The index-map is native and choice-free (F1).** The 3 generations are `Lambda^1(C^3)`
with `C_3` the cyclic shift `C`; the `C_3` DFT `F` diagonalizes `C`, and the
Fourier-grade projection `(1/3)Tr(C^-1 H) = b` identifies `b` as the **`C_3`-doublet
Fourier amplitude** of `H = aI + bC + b-bar C^2` (`a` the singlet amplitude). Only
`arg(b)` (Brannen `delta`, `Q`-orthogonal) and orientation are convention.

**The native Berry curvature is zero -- derived, not assumed (F2).**
On the real circulant coordinate plane
`H = aI + u(C + C^2) + v i(C - C^2)` matching the Fourier-amplitude
coordinates from F1, the Berry curvature of the filled band is **zero**
(plaquette Berry `~1e-16`) by **eigenvector rigidity**: the eigenvectors are the
**`(u,v)`-independent** Fourier modes (verified `|<Fourier_k|eigvec>| = 1`), so
the doublet coordinate shifts eigenvalues without rotating eigenvectors. This
is the finite native Berry statement. It is not a branch-selection theorem.

## The finite comparison

The two-band comparison isolates **one** finite algebraic distinction (F3): a coupling
that **anticommutes** with the chiral grading `Gamma_chi` (`= sigma_z`; e.g.
`u sigma_x + v sigma_y`) carries a **nonzero Berry monopole**, while a coupling
that **commutes** with `Gamma_chi` has **zero** Berry. The runner also keeps the
separate finite Koide algebra identities `Q(r=1/2)=2/3` and `Q(r=1)=1`.

What remains missing is the bridge theorem that would turn that finite
distinction into a framework-native weighting rule:

> Does the framework derive a Berry/chirality-to-`r` selection rule, and if so
> which admissible operator supplies the physical readout?

This narrowed row may be used as a finite-matrix support packet for that
question. It may not be used as a derivation that zero Berry selects `r=1`, that
nonzero Berry selects `r=1/2`, or that the native circulant mass realizes the
physical `Q=1` branch.

## The native mass is non-chiral

Every native circulant `Lambda^1` mass **commutes** with `Gamma_chi = 2 P_singlet - I`
(itself circulant): `[H, Gamma_chi] = 0`, so `{H, Gamma_chi} != 0` — it **never**
anticommutes (F4). Hence the native circulant algebra supplies the zero-Berry /
commuting side of the finite comparison. It does not by itself select the
physical `Q` branch; a separate retained bridge would have to identify the
physical source/readout and the `r` weighting.

## Boundary

This is **not** a derivation of `Q=2/3` or `Q=1`; it is a finite-matrix support
packet. The index map is native; the native circulant Berry curvature is zero;
an anticommuting two-band comparator has nonzero Berry curvature; and the
Koide `Q(r)` identities are checked as algebra. On the generation `R^3` factor
the anticommuting route is blocked by the bounded
[KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md):
`comm(C) cap anticomm(Gamma_chi) = {0}` for the native circulant algebra. This
does not rule out a chiral factor sourced outside the generation `R^3`.

**The next path** (not foreclosed): `C^3=I` blocks a chiral grading **sourced from the
generation `R^3`**, but does **not** touch one sourced from a tensor factor **distinct**
from the generation `R^3` (a separate-factor / Connes-Lott-type direction). The sharp,
not-yet-computed question: can an **off-generation** factor (a horizontal/`2`-Higgs
factor) supply a `Gamma_chi`-anticommuting coupling, and can an independent
retained theorem relate that coupling to the physical `r` weighting **without**
breaking `C^3=I` on the generation factor? (The qubit-factor route is already
shown import-sourced and `r`-non-selective; the spacetime `gamma_5` acts
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
