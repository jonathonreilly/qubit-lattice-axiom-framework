---
claim_id: g_bare_h_unit_same_projected_1pi_residue_exhaustion_narrow_theorem_note_2026-06-12
claim_type_author_hint: bounded_theorem
runner_path: scripts/g_bare_h_unit_same_projected_1pi_residue_exhaustion_named_gap_2026_06_12.py
audit_authority: independent audit lane only
---

# Same-Projected 1PI Residue Exhaustion: Conditional Named-Gap Theorem

**Date:** 2026-06-12 (source-boundary repair 2026-07-18)
**Type:** bounded_theorem
**Claim scope:** a finite projected coefficient diagnostic. Under a separately
supplied H-MATRIX physical bridge, the Rep-B coefficient is `1/6`; the
projected one-gauge-boson-exchange coefficient is `g_bare^2/6`, so their
difference is `(g_bare^2-1)/6`. The nonzero polynomial names the missing
same-projected 1PI bridge. Without H-MATRIX, the Rep-B coefficient remains
symbolic and even that specialized residual is unavailable.
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
  supplies the bounded projected OGE coefficient and symmetry context at its
  own scope.
- [YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md](YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md)
  states the H-MATRIX and SAME-1PI hypotheses separately.
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

Under H-MATRIX, the abstract theorem gives

```text
K(g_bare) = I_6/sqrt(6),
R_B = F_RepB(g_bare)^2 = 1/6.                                  (B)
```

## Projected coefficient diagnostic

On the separately specified scalar-singlet projection, the OGE coefficient
is

```text
R_OGE(g_bare) = g_bare^2/(2N_c) = g_bare^2/6                   (A)
```

at `N_c=3` and the supplied scalar sign. Combining `(A)` with the conditional
input `(B)` gives the formal difference

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

Therefore H-MATRIX plus the OGE coefficient do not prove arbitrary-parameter
same-projected exhaustion. Equality of the two coefficients still requires
SAME-1PI as a separately supplied bridge.

## Missing-H-MATRIX branch

Without H-MATRIX, write the physical Rep-B form factor as an unconstrained
function `f(g_bare)`. The available difference is only

```text
g_bare^2/6 - f(g_bare)^2.
```

The abstract theorem cannot set `f`, because no physical operator has been
shown to satisfy its hypotheses. Thus `(D)` is explicitly conditional and
must not be cited as an unconditional physical residual.

## Named gap

**Gap name:** same-projected OGE/Rep-B identification with physical matrix
normalization.

Two independent bridges remain open:

1. **H-MATRIX / form-factor bridge:** establish positivity, full
   `End(C^6)` centrality, Hilbert--Schmidt unit norm, and the physical
   diagonal-overlap identification for the proposed composite.
2. **SAME-1PI bridge:** prove that the OGE and Rep-B constructions are two
   complete representations of the same projected amputated 1PI object,
   without inserting coefficient equality as a premise.

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
solution for the conditional branch, verifies the exact residual and samples,
keeps the missing-H-MATRIX function symbolic, and checks that equality is
pointwise rather than an arbitrary-parameter identity. Expected output is
`PASS>0, FAIL=0`.
