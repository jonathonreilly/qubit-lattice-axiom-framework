---
claim_id: g_bare_h_unit_same_projected_1pi_residue_exhaustion_narrow_theorem_note_2026-06-12
claim_type_author_hint: bounded_theorem
runner_path: scripts/g_bare_h_unit_same_projected_1pi_residue_exhaustion_named_gap_2026_06_12.py
audit_authority: independent audit lane only
---

# Same-Projected Fermion-Kernel Residue: Conditional Named-Gap Theorem

**Date:** 2026-06-12 (source-boundary repair 2026-07-18)
**Type:** bounded_theorem
**Claim scope:** a finite conditional coefficient diagnostic. H-MATRIX fixes
only a form factor; a separate REP-B-RESIDUE condition is required to turn
its square into the Rep-B coefficient. Under both conditions and the declared
continuum/small-momentum Rep-A convention, the formal difference is
`(g_bare^2-1)/6`. SAME-1PI remains a third, separate equality condition.
**Status authority:** independent audit lane only.
**Primary runner:**
[`scripts/g_bare_h_unit_same_projected_1pi_residue_exhaustion_named_gap_2026_06_12.py`](../scripts/g_bare_h_unit_same_projected_1pi_residue_exhaustion_named_gap_2026_06_12.py)
**Result:** named-gap case, not exhaustion proven.

## Authorities and exact roles

- [G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md](G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md)
  names the requested same-projected bridge.
- [G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md](G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md)
  now records the physical Rep-B statement only as a conditional corollary.
- [YT_WARD_IDENTITY_DERIVATION_THEOREM.md](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
  supplies source context for the SU(`N_c`) completeness identity. Its
  physical `H_unit`, exact-lattice-kernel, and full-theory 1PI statements are
  not inherited here.
- [YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md](YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md)
  states H-MATRIX, REP-B-RESIDUE, and SAME-1PI separately.
- [UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
  supplies only the abstract central-positive Hilbert--Schmidt matrix
  implication.

No one of these sources proves that a physical composite has the abstract
matrix hypotheses and physical form-factor identification.

## Local H-MATRIX hypothesis

For the conditional branch only, suppose a separate physical construction
represents the proposed Rep-B operator by `K(g_bare) in End(C^6)` and proves

```text
K(g_bare) >= 0,
[K(g_bare),E_jk] = 0 for every matrix unit,
Tr(K(g_bare)^dagger K(g_bare)) = 1,
F_RepB(g_bare) = <e_j,K(g_bare)e_j>.
```

These are ordinary explicit local hypotheses, not framework axioms,
admissions, physical inputs, carriers, or premise-registry entries. The
current packet does not establish them.

Under H-MATRIX, the abstract theorem gives only

```text
K(g_bare) = I_6/sqrt(6),
F_RepB(g_bare)^2 = 1/6.                                       (F)
```

## Local REP-B-RESIDUE hypothesis

Separately suppose that, in the fermion-only effective-action kernel after
tree-level gauge integration, a physical construction proves the unit
residue/source normalization, equal left and right insertions, and kernel
convention required for

```text
R_B(g_bare) = F_L(g_bare) F_R(g_bare),
F_L(g_bare) = F_R(g_bare) = F_RepB(g_bare).                    (B)
```

REP-B-RESIDUE is an ordinary explicit condition, not a framework premise.
It is not implied by Hilbert--Schmidt normalization and is not derived here.

## Projected coefficient diagnostic

In the declared direct/exchange Fierz coordinates and chosen scalar-Clifford
pairing, the small-momentum continuum-kernel OGE coordinate is supplied as

```text
R_OGE(g_bare) = g_bare^2/(2N_c) = g_bare^2/6                   (A)
```

at `N_c=3` and the supplied scalar sign. Here `q^2` is not asserted to be the
exact Wilson-lattice kernel; lattice momentum, projector, and vertex form
factors remain outside this diagnostic. The OGE graph is a vertex of the
gauge-integrated fermion effective action, not a full-theory 1PI graph.
Combining `(A)` with the conditional input `(B)` gives the formal difference

```text
Delta(g_bare) = R_OGE(g_bare)-R_B
              = (g_bare^2-1)/6.                               (D)
```

This polynomial vanishes at `g_bare=+1` and `g_bare=-1`, but it is not the
zero polynomial. Exact off-point values include

```text
Delta(1/2) = -1/8,
Delta(3/2) = 5/24,
Delta(2)   = 1/2.
```

Therefore H-MATRIX plus REP-B-RESIDUE and the OGE coordinate do not prove
arbitrary-parameter same-kernel exhaustion. Equality of the two coefficients
still requires SAME-1PI as a separately supplied bridge in the fermion-only
effective-action convention.

## Missing-H-MATRIX branch

Without H-MATRIX, write the physical Rep-B form factor as an unconstrained
function `f(g_bare)`. Even if REP-B-RESIDUE is supplied, the available
difference is only

```text
g_bare^2/6 - f(g_bare)^2.
```

The abstract theorem cannot set `f`, because no physical operator has been
shown to satisfy its hypotheses. Thus `(D)` is explicitly conditional and
must not be cited as an unconditional physical residual.

Without REP-B-RESIDUE, H-MATRIX still leaves the physical Rep-B coefficient
as an unconstrained function `r_B(g_bare)`, so the available expression is
only `g_bare^2/6-r_B(g_bare)`.

## Named gap

**Gap name:** same-projected OGE/Rep-B identification with physical matrix
normalization.

Three independent bridges remain open:

1. **H-MATRIX / form-factor bridge:** establish positivity, full
   `End(C^6)` centrality, Hilbert--Schmidt unit norm, and the physical
   diagonal-overlap identification for the proposed composite.
2. **REP-B-RESIDUE bridge:** establish the source/residue normalization,
   two-insertion factorization, and kernel convention that identify the
   coefficient with the form-factor square.
3. **SAME-1PI bridge:** prove that the OGE and Rep-B constructions are two
   complete representations of the same projected four-fermion vertex in the
   fermion-only effective action, without inserting coefficient equality as a
   premise.

The OGE class has the same projected scalar-singlet quantum numbers and the
same leading `q^-2` order, so the current symmetry inventory does not remove
it. Point equality at `g_bare=1` does not establish a polynomial identity.

## Boundary

This note does not derive a Standard-Model carrier, an isospin/color
assignment, a Wick state, a free-field residue, a Ward normalization, a
physical `H_unit`, tree-level gauge independence of a composite, a
`g_bare` selector, a top-Yukawa value, or an observed quantity. It introduces
no new premise or framework authority.

No literature value, observed comparator, fitted selector, or admitted unit
convention is used in the exact finite coefficient diagnostic.

## Validation

The runner reconstructs the abstract six-dimensional centralizer and norm
solution for the conditional branch, distinguishes the squared form factor
from the coefficient supplied by REP-B-RESIDUE, verifies the exact residual
and samples, keeps both missing-H-MATRIX and missing-REP-B-RESIDUE branches
symbolic, and checks that equality is pointwise rather than an
arbitrary-parameter identity. Expected output is `PASS>0, FAIL=0`.
