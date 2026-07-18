---
claim_id: yt_ward_step3_contact_4fermion_vanishing_narrow_theorem_note_2026-05-17
claim_type_author_hint: bounded_theorem
runner_path: scripts/frontier_yt_ward_step3_contact_4fermion_vanishing.py
audit_authority: independent audit lane only
---

# YT_WARD Step 3 Contact Four-Fermion Vanishing Bounded Theorem

**Date:** 2026-05-17 (source-boundary repair 2026-07-18)
**Type:** bounded_theorem
**Claim scope:** under the cited bare-action specification and standard
tree-level diagram bookkeeping, the absent contact four-fermion operators
have zero bare coefficients, so single-gauge-boson exchange is the complete
leading `g_bare^2/q^2` contribution on the stated projected channel. This
does not establish a Rep-B representation, a physical `H_unit` form factor,
or equality of Rep A and Rep B.
**Status authority:** independent audit lane only.
**Primary runner:**
[`scripts/frontier_yt_ward_step3_contact_4fermion_vanishing.py`](../scripts/frontier_yt_ward_step3_contact_4fermion_vanishing.py)

## Hypotheses

The theorem is bounded by the following cited inputs at their own scopes:

1. The bare action specified in
   [`MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md) contains
   the Wilson plaquette and staggered-Dirac bilinear terms and no bare
   contact four-fermion operator.
2. The composite-scalar statement in
   [`YUKAWA_COLOR_PROJECTION_THEOREM.md`](YUKAWA_COLOR_PROJECTION_THEOREM.md)
   supplies no independent fundamental scalar field in that action.
3. Standard tree-level bookkeeping decomposes a projected amputated
   four-fermion Green's function into single-gauge-boson exchange, a bare
   contact vertex if present, and higher exchange topologies.
4. The color-singlet projection coefficient from
   [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
   is `-1/(2N_c)`, with a separately supplied scalar-sign convention
   `c_S=+1` for the displayed specialization.

These inputs and their broader framework standing are not re-proved here.

## Theorem

Enumerate the finite Clifford x color x isospin basis of possible bare
four-fermion contact structures

```text
(psibar Gamma psi)(psibar Gamma' psi).
```

Because none occurs in the specified bare action, every corresponding bare
coefficient is zero. In particular, on the scalar-singlet projection `O_S`,

```text
Gamma_contact,S^(4) = 0.                                      (T1)
```

At leading order in `g_bare^2/q^2`, higher exchange topologies are of higher
power, so the projected tree-level coefficient is the one-gauge-boson
exchange coefficient

```text
Gamma_S^(4)(q^2;g_bare)
  = -c_S g_bare^2/(2N_c q^2) O_S
    + O(g_bare^4/q^4).                                        (T2)
```

This proves contact vanishing and leading-order Rep-A completeness only.

## Rep-B boundary

Contact vanishing does not prove that a composite two-insertion diagram is a
second complete representation of the same projected 1PI object. Nor does
it prove the normalization or physical interpretation of such an operator.

For reference, if the local H-MATRIX hypothesis from the
[doubly conditional Step-3 theorem](YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md)
is separately supplied, the
[abstract central-positive Hilbert--Schmidt theorem](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
gives the conditional arithmetic coefficient

```text
C_B = 1/(N_c N_iso).
```

This use requires a physical construction to establish positivity,
full-matrix centrality, Hilbert--Schmidt unit norm, and the identification of
the physical form factor with a diagonal matrix expectation. The abstract
theorem supplies none of those physical statements.

Even after H-MATRIX is supplied, equality with `(T2)` requires the separate
SAME-1PI hypothesis. Under both local hypotheses the coefficient difference
is

```text
c_S g_bare^2/(2N_c) - 1/(N_c N_iso),
```

and equality yields the familiar gate equation. Neither H-MATRIX nor
SAME-1PI follows from `(T1)` or `(T2)`.

## What this theorem does not claim

- It does not derive a physical carrier or assign meanings to a
  factorization `n=N_iso N_c`.
- It does not derive a Wick state, free-field residue, Ward normalization,
  gauge-independent physical `H_unit`, `g_bare` selector, top-Yukawa datum,
  or observed quantity.
- It does not derive H-MATRIX, SAME-1PI, `g_bare=1`, or the physical equality
  of Rep A and Rep B.
- It introduces no new framework axiom, admission, primitive, physical
  input, carrier, or premise-registry entry.

## Declared dependencies

- [MINIMAL_AXIOMS_2026-05-03.md](MINIMAL_AXIOMS_2026-05-03.md) for the
  bounded bare-action specification.
- [YUKAWA_COLOR_PROJECTION_THEOREM.md](YUKAWA_COLOR_PROJECTION_THEOREM.md)
  for the bounded composite-scalar inventory.
- [YT_EW_COLOR_PROJECTION_THEOREM.md](YT_EW_COLOR_PROJECTION_THEOREM.md)
  for the color projection coefficient.
- [UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
  only for the optional abstract H-MATRIX corollary.
- [YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md](YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the explicit H-MATRIX/SAME-1PI boundary.

Non-load-bearing historical cross-references are
[G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md](G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md),
which now states only a conditional Rep-B corollary;
[G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md](G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md),
which names the unclosed pinning route; and
[YT_WARD_IDENTITY_DERIVATION_THEOREM.md](YT_WARD_IDENTITY_DERIVATION_THEOREM.md),
the broader parent packet. None supplies H-MATRIX or SAME-1PI here.

## Validation

The runner enumerates all `16 x 16 x 2 x 2 = 1024` contact structures,
checks their absent-action coefficients, reconstructs the SU(3) Fierz
coefficient, verifies leading-order power counting, and recomputes the
conditional Rep-B residual without treating either local bridge as derived.
Expected output is `PASS>0, FAIL=0`.
